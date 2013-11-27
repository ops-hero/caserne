pkg_list_python = [
    "libpq-dev",
    "vim",
    "python-profiler",
    "libmemcached-dev",
    "python-crypto",
    "build-essential",
    "libxml2-dev",
    "libxslt-dev",
    "libevent-dev",
    "swig",
    "python2.7-m2crypto"
]

pkg_list_python.each do | pkg |
    package pkg do
        action [:install]
    end
end

