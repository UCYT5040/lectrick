import importlib
import pkgutil
from pathlib import Path

package_dir = Path(__file__).resolve().parent
for (_, module_name, _) in pkgutil.iter_modules([str(package_dir)]):
    importlib.import_module(f"{__name__}.{module_name}")

_TILE_REGISTRY = {}


def _register_tile_subclasses():
    for module in pkgutil.iter_modules([str(Path(__file__).resolve().parent)]):
        module_name = module.name
        module = importlib.import_module(f"{__name__}.{module_name}")
        for cls in module.__dict__.values():
            if isinstance(cls, type) and hasattr(cls, 'TILE_TYPE'):
                _TILE_REGISTRY[cls.TILE_TYPE] = cls


_register_tile_subclasses()


def create_tile(tile_type, *args, **kwargs):
    if tile_type not in _TILE_REGISTRY:
        raise ValueError(f"Tile type '{tile_type}' is not registered.")

    return _TILE_REGISTRY[tile_type](*args, **kwargs)


def get_sample_chars():
    return [
        (tile_cls.TILE_TYPE, tile_cls.SAMPLE_CHARS)
        for tile_cls in _TILE_REGISTRY.values()
        if hasattr(tile_cls, 'SAMPLE_CHARS')
    ]


def list_tile_types():
    return list(_TILE_REGISTRY.keys())


__all__ = [create_tile]  # Prevent exporting other functions or classes
