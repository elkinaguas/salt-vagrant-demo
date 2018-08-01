# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  os = "bento/ubuntu-16.04"
  net_ip = "192.168.50"

  config.vm.define :master, primary: true do |master_config|
    master_config.vm.provider "virtualbox" do |vb|
        #vb.memory = "2048"
        vb.memory = "1024"
        vb.cpus = 1
        vb.name = "master"
    end
      master_config.vm.box = "#{os}"
      master_config.vm.host_name = 'saltmaster.local'
      master_config.vm.network "private_network", ip: "#{net_ip}.10"
      master_config.vm.synced_folder "saltstack/salt/", "/srv/salt"
      master_config.vm.synced_folder "saltstack/pillar/", "/srv/pillar"

      master_config.vm.provision :salt do |salt|
        salt.master_config = "saltstack/etc/master"
        salt.master_key = "saltstack/keys/master_minion.pem"
        salt.master_pub = "saltstack/keys/master_minion.pub"
        salt.minion_key = "saltstack/keys/master_minion.pem"
        salt.minion_pub = "saltstack/keys/master_minion.pub"
        salt.seed_master = {
                            "minion1" => "saltstack/keys/minion1.pub",
                            "minion2" => "saltstack/keys/minion2.pub"
                           }

        salt.install_type = "stable"
        salt.install_master = true
        salt.no_minion = true
        salt.verbose = true
        salt.colorize = true
        salt.bootstrap_options = "-P -c /tmp"
      end
    end


    [
      ["minion1",    "#{net_ip}.11",    "512",    os ],
      ["minion2",    "#{net_ip}.12",    "512",    os ],
    ].each do |vmname,ip,mem,os|
      config.vm.define "#{vmname}" do |minion_config|
        minion_config.vm.provider "virtualbox" do |vb|
            vb.memory = "#{mem}"
            vb.cpus = 1
            vb.name = "#{vmname}"
        end
        if "#{vmname}" == "minion1"
          minion_config.vm.network :forwarded_port, guest: 22, host: 2251, id: 'ssh'
        end
        if "#{vmname}" == "minion2"
          minion_config.vm.network :forwarded_port, guest: 22, host: 2252, id: 'ssh'
        end
        minion_config.vm.box = "#{os}"
        minion_config.vm.hostname = "#{vmname}"
        minion_config.vm.network "private_network", ip: "#{ip}"

        minion_config.vm.provision :salt do |salt|
          salt.minion_config = "saltstack/etc/#{vmname}"
          salt.minion_key = "saltstack/keys/#{vmname}.pem"
          salt.minion_pub = "saltstack/keys/#{vmname}.pub"
          salt.install_type = "stable"
          salt.verbose = true
          salt.colorize = true
          salt.bootstrap_options = "-P -c /tmp"
        end
      end
    end
    
    [
      ["ub1",    "192.168.3.2",    "512",    os ],
      ["ub2",    "192.168.4.2",    "512",    os ],
      ["ub3",    "192.168.5.2",    "512",    os ],
    ].each do |vmname,ip,mem,os|
      config.vm.define "#{vmname}" do |minion_config|
        minion_config.vm.provider "virtualbox" do |vb|
            vb.memory = "#{mem}"
            vb.cpus = 1
            vb.name = "#{vmname}"
        end
        minion_config.vm.box = "#{os}"
        minion_config.vm.hostname = "#{vmname}"
        minion_config.vm.network "private_network", ip: "#{ip}", virtualbox__intnet: "1-#{vmname}"
        
        if "#{vmname}" == "ub1"
          minion_config.vm.network :forwarded_port, guest: 22, host: 2241, id: 'ssh'
          minion_config.vm.provision "shell", 
              run: "always",
              inline: "route add default gw 192.168.3.1"
        end
        if "#{vmname}" == "ub2"
          minion_config.vm.network :forwarded_port, guest: 22, host: 2242, id: 'ssh'
          minion_config.vm.provision "shell", 
              run: "always",
              inline: "route add default gw 192.168.4.1"
        end
        if "#{vmname}" == "ub3"
          minion_config.vm.network :forwarded_port, guest: 22, host: 2243, id: 'ssh'
          minion_config.vm.provision "shell", 
              run: "always",
              inline: "route add default gw 192.168.5.1"
        end

        minion_config.vm.provision :salt do |salt|
          salt.minion_config = "saltstack/etc/#{vmname}"
          salt.minion_key = "saltstack/keys/#{vmname}.pem"
          salt.minion_pub = "saltstack/keys/#{vmname}.pub"
          salt.install_type = "stable"
          salt.verbose = true
          salt.colorize = true
          salt.bootstrap_options = "-P -c /tmp"
        end
      end
    end

  end
