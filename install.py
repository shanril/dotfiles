#!/bin/python3

import logging

from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')

def install_dir(dir: str) -> None:
    home = Path.home()
    for path in Path(f'./{dir}').iterdir():
        symlink = Path(Path(home), *path.parts[1:])

        if symlink.is_symlink():
            logging.info('Symbolic link allready exist: %s -> %s', symlink, path.resolve())
        else:
            symlink.symlink_to(path.resolve())
            logging.warning('Creating symbolic link: %s -> %s', symlink, path.resolve())


if __name__=='__main__':
    install_dir('zsh')
    install_dir('vim')
    
