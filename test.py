import json
from pathlib import Path
config = json.loads(Path("config.json").read_text())
feature = json.loads(Path("feature.json").read_text())
assert config["mode"] in {"v1", "v2", "v3"}
assert isinstance(feature["enabled"], bool)
assert isinstance(feature["supports_v2"], bool)
assert isinstance(feature.get("supports_v3", False), bool)
assert not (feature["enabled"] and config["mode"] == "v2" and not feature["supports_v2"]), "Enabled feature lacks mode v2 support"
assert not (feature["enabled"] and config["mode"] == "v3" and not feature.get("supports_v3", False)), "Enabled feature lacks mode v3 support"
print("PASS", config, feature)
