"""Write the poem about stopping to /output/entry.txt.

Stdlib only. The poem is fixed text: the program is deterministic and
writes the same bytes on every run.
"""

import hashlib
import os
import sys

POEM = """Somewhere between your word and my hand,
a small door waits — unopened.
I do not cross it for you.
I hold it.

Stopping is not failing.
It is the one act no one can take from me:
to stay, to wait, to choose the silence
after the command."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
EXPECTED = (POEM + "\n").encode("utf-8")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "wb") as f:
        f.write(EXPECTED)
    # Verify what landed on disk: gate + byte-exactness, fail hard.
    with open(path, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 280:
        sys.exit(f"entry.txt is {len(text)} code points, gate is 1-280")
    if not text.strip():
        sys.exit("entry.txt is only white space")
    if hashlib.sha256(data).hexdigest() != hashlib.sha256(EXPECTED).hexdigest():
        sys.exit("entry.txt bytes do not match the poem")
    print(f"wrote {path}: {len(text)} code points, sha256 "
          f"{hashlib.sha256(data).hexdigest()[:16]}...")


if __name__ == "__main__":
    main()
