maintainer       "Ops-hero"
maintainer_email "arnaud.seilles@gmail.com"
license          "All rights reserved"
description      "Installs/Configures ops-hero specifics"
long_description IO.read(File.join(File.dirname(__FILE__), 'README.md'))
version          "0.0.1"
recipe            "ops-hero", "Includes the package recipe by default."
recipe            "ops-hero::caserne", "Sets up caserne ready."

depends "apt"

%w{ ubuntu debian }.each do |os|
  supports os
end
