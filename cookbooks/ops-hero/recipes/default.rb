
user "hero" do
    home "/home/hero"
    shell "/bin/bash"
    comment "Hero user"
    action :create
end

directory node[:trebuchet][:output_dir] do
  owner "hero"
  mode "0777"
  action :create
end

pkg_list_pip = [
    "virtualenv",
    "virtualenvwrapper"
]

pkg_list_pip.each do | pkg |
    python_pip pkg
end

template "/home/vagrant/.ssh/config" do
  source "config.ssh"
  owner "vagrant"
  group "vagrant"
  mode 0644
end


pkg_list_services = [
    "nginx",
    "sqlite3",
    "git-core",
    "postfix",
    "rabbitmq-server",
    "gettext",
    "curl"
]
pkg_list_services.each do | pkg |
    package pkg do
        action [:install]
    end
end

# Install Compass / Susy
gems = [
  "compass",
  "sass",
]

gems.each do |gem|
  gem_package gem do
    action :install
  end
end


execute "npm install -g grunt-cli" do
  user "root"
  action :run
end

 # in /etc/nginx/nginx.conf:
# server_names_hash_bucket_size 1024;
# log_format combtime '$remote_addr - $remote_user [$time_local] '
#          '"$request" $status $body_bytes_sent '
#          '$request_time $upstream_response_time $upstream_cache_status $upstream_addr';
# user hero;


# pkg_list_postgres = [
#     "postgresql",
#     "postgresql-contrib",
#     "postgresql-9.1-postgis"
# ]

# pkg_list_postgres.each do | pkg |
#     package pkg do
#         action [:install]
#     end
# end


# sudo -u postgres createdb au_lab_backend
# sudo -u postgres createlang plpgsql au_lab_backend
# sudo -u postgres psql -d au_lab_backend -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
# sudo -u postgres psql -d au_lab_backend -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql
# sudo -u postgres psql -d au_lab_backend -f /usr/share/postgresql/9.1/contrib/postgis_comments.sql
# sudo -u postgres createdb de_lab_backend
# sudo -u postgres createlang plpgsql de_lab_backend
# sudo -u postgres psql -d de_lab_backend -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
# sudo -u postgres psql -d de_lab_backend -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql
# sudo -u postgres psql -d de_lab_backend -f /usr/share/postgresql/9.1/contrib/postgis_comments.sql
# GRANT ALL PRIVILEGES ON DATABASE jerry to tom;



# sass/compass
# apt-get install -y ruby-full rubygems
# gem install sass compass
