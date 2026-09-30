from pathlib import Path

path = Path('src/aasset.rs')
text = path.read_text(encoding='utf-8')

marker = '''    // This is meant to strip the new "asset" folder path so we can be compatible with other versions\n'''

injection = r'''    // PandaMine VVU: replace the APK's tiers.bin with the copy embedded in this mod.
    // The original Android pack requires copying tiers.bin into the APK's assets/assets/
    // directory. Here we keep Minecraft untouched and replace the bytes at AAsset level.
    if os_filename.as_encoded_bytes() == b"tiers.bin" {
        if aasset.is_null() {
            log::warn!("PandaMine VVU: tiers.bin was requested but the original AAsset is null");
            return aasset;
        }

        static PANDA_VVU_TIERS: &[u8] = include_bytes!("../tiers.bin");
        let mut wanted_lock = WANTED_ASSETS.lock().unwrap();
        wanted_lock.insert(
            AAssetPtr(aasset),
            Cursor::new(PANDA_VVU_TIERS.to_vec()),
        );
        log::info!("PandaMine VVU: serving embedded tiers.bin ({} bytes)", PANDA_VVU_TIERS.len());
        return aasset;
    }

    // This is meant to strip the new "asset" folder path so we can be compatible with other versions
'''

if injection.replace('\\n', '\n') in text or 'PandaMine VVU: replace the APK' in text:
    print('Patch already present')
    raise SystemExit(0)

if marker not in text:
    raise SystemExit('Could not find the insertion marker in src/aasset.rs')

text = text.replace(marker, injection, 1)
path.write_text(text, encoding='utf-8')
print('Patched src/aasset.rs')
