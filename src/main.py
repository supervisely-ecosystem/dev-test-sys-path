import sys

print("PYTHONPATH:")
for p in sys.path:
    print(p)

print()
import src.a
import b.b
import src.c.c


# local run 
# export PYTHONPATH="$PYTHONPATH:/Users/maxim/work/sly_apps/dev/dev-test-sys-path" && python src/main.py