import hashlib
from pathlib import Path
import shutil


#This is the isolated function, just hash calculation
def calulate_file_hash(route: Path) -> str:
    sha256 = hashlib.sha256()

    with open(route, "rb") as archivo_binario:
        while True:
            block = archivo_binario.read(4096)
            if not block:
                break
            sha256.update(block)

    return sha256.hexdigest()  # Return Hash in terminal