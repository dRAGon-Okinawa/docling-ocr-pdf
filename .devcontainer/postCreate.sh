curl -o /usr/local/bin/cog -L https://github.com/replicate/cog/releases/latest/download/cog_`uname -s`_`uname -m | sed "s/aarch64/arm64/"`
chmod +x /usr/local/bin/cog