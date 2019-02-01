cd "$TRAVIS_BUILD_DIR"
mkdir -p release
cd release
CC=gcc-7 CXX=g++-7 cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$HOME/.local ..
mtime_cache ../**/*.{%{cpp}} -c ../.mtime_cache/cache.json
make -j 2
make install
cd "$TRAVIS_BUILD_DIR"
