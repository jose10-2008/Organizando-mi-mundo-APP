from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "organizando-mi-mundo" / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from organizando_mi_mundo.main import main

if __name__ == "__main__":
    main()
