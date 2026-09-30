from pathlib import Path

path = Path("src/aasset.rs")
text = path.read_text(encoding="utf-8")

if "PandaMine VVU" in text:
    print("PandaMine VVU patch already present")
    raise SystemExit(0)

# QYCottage/mtbinloader2-levi v0.1.10-beta has an AAssetManager_open hook
# whose stable anchor is the c_path calculation immediately before the path
# stripping logic. We inject the replacement there instead of depending on a
# long comment block that can change between commits.
anchor = "    let c_path: &Path = Path::new(os_str);\n"
injection = '''    // PandaMine VVU: serve the embedded tiers.bin without modifying Minecraft's APK.\n    // The original PandaMine pack is installed by replacing this asset.\n    // The Levi mod keeps Minecraft untouched and substitutes the bytes at the\n    // AAsset layer instead.\n    if os_filename.as_encoded_bytes() == b"tiers.bin" && !aasset.is_null() {\n        let data = BufferCursor::Vec(Cursor::new(include_bytes!("../tiers.bin").to_vec()));\n        WANTED_ASSETS\n            .get_mut()\n            .insert(AAssetPtr(aasset), Buffer::new(c_path.to_path_buf(), data));\n        log::info!(\n            "PandaMine VVU: serving embedded tiers.bin ({} bytes)",\n            include_bytes!("../tiers.bin").len()\n        );\n        return aasset;\n    }\n'''

if anchor not in text:
    raise SystemExit(
        "Could not locate the stable c_path anchor in src/aasset.rs. "
        "The mtbinloader2-levi base source changed and needs a new adapter."
    )

text = text.replace(anchor, anchor + injection, 1)
path.write_text(text, encoding="utf-8")
print("Patched src/aasset.rs using the c_path anchor")
