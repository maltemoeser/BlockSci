mkdir -p release
cd release
CC=gcc-7 CXX=g++-7 cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$HOME/.blocksci ..
mtime_cache ../**/*.{%{cpp}} -c ../.mtime_cache/cache.json
make -j 2
make install
cd ..
