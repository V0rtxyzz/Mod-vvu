from pathlib import Path

path = Path("src/aasset.rs")
text = path.read_text(encoding="utf-8")

if "PandaMine VVU" in text:
    print("PandaMine VVU patch already present")
    raise SystemExit(0)

anchor = "    let c_path: &Path = Path::new(os_str);\n"
injection = '''    // PandaMine VVU: serve the embedded tiers.bin without modifying Minecraft's APK.
    // We keep the original AAsset handle and replace its read/length operations
    // through WANTED_ASSETS, which is already handled by this loader.
    if c_path
        .file_name()
        .map(|name| name.as_encoded_bytes() == b"tiers.bin")
        .unwrap_or(false)
        && !aasset.is_null()
    {
        let data = BufferCursor::Vec(Cursor::new(include_bytes!("../tiers.bin").to_vec()));
        WANTED_ASSETS
            .get_mut()
            .insert(AAssetPtr(aasset), Buffer::new(c_path.to_path_buf(), data));
        log::info!(
            "PandaMine VVU: serving embedded tiers.bin ({} bytes)",
            include_bytes!("../tiers.bin").len()
        );
        return aasset;
    }
'''
if anchor not in text:
    raise SystemExit("Could not locate the c_path anchor in src/aasset.rs")
text = text.replace(anchor, anchor + injection, 1)
path.write_text(text, encoding="utf-8")
print("Patched src/aasset.rs: tiers.bin interception")
