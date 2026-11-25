import pytest
import graphics.eye_cornea as mod

CASES = [
    ("cornea_double_refract", (1,)),
    ("pupil_parallax_depth", (1,)),
    ("iris_seam_continuous", (1,)),
    ("per_eye_material", (1,)),
    ("reflection_timing", (1,)),
    ("lod_normal_rebuild_eye", (1,)),
    ("load_eye", (1,)),
    ("shade_eye", (1,)),
    ("resolve_eye", (1,)),
    ("present_eye", (1,)),
    ("validate_eye", (1,)),
    ("metrics_eye", (1,)),
    ("audit_eye", (1,)),
    ("fallback_eye", (1,)),
    ("determinism_eye", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
