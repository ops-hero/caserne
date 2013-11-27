# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "precise64-caserne"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.network :hostonly, "192.168.3.205"
  #config.vm.network :bridged
  config.ssh.forward_agent = true

  # Share an additional folder to the guest VM. The first argument is
  # an identifier, the second is the path on the guest to mount the
  # folder, and the third is the path on the host to the actual folder.
  config.vm.share_folder "v-code", "/code", "~/Projects/ops-hero/code"

  # put the insecure key back in the machine, so we can use it to connect locally.
  config.vm.share_folder "v-vagrant", "/home/vagrant/.vagrant.d", "~/.vagrant.d/"
  config.vm.share_folder "v-ssh", "/home/vagrant/.my-ssh", "~/.ssh/"

  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = "cookbooks"


    chef.json.merge!({
      :python => { :version => "2.7" },
      :redis => { :bind => "0.0.0.0" },
      :trebuchet => { :output_dir => "/var/packages" }
    })

    # https://github.com/opscode/cookbooks
    chef.add_recipe "apt"
    chef.add_recipe "build-essential"  
    
    # https://github.com/phlipper/chef-redis
    chef.add_recipe "redis"

    # https://github.com/opscode-cookbooks/python
    chef.add_recipe "python"

    chef.add_recipe "ops-hero"   
    chef.add_recipe "ops-hero::caserne" 

  end

end
