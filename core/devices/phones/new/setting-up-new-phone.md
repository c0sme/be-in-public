- Revoke all SSH keys used in your previous phone
  - Github

- Login to the Google accounts specified in `core/primary-assets.md`
- Install and setup Firefox
  - setup browser data sync
- Install and setup F-Droid
- Install Termux from F-Droid
  - https://f-droid.org/en/packages/com.termux
  - setup Git in Termux
    ```bash
    # apt upgrade -y -o Dpkg::Options::="--force-confold"
    pkg upgrade
    # apt install -y -o Dpkg::Options::="--force-confold" git openssh nano
    pkg install git openssh nano
    termux-setup-storage

    mkdir -p ~/storage/shared/Documents/repositories
    touch ~/storage/shared/Documents/repositories/.nomedia

    echo "
    export EDITOR=\"nano\"

    cd ~/storage/shared/Documents/repositories" >> ~/.bashrc

    ssh-keygen -t ed25519 -C "pbartmr@gmail.com"
    cat /data/data/com.termux/files/home/.ssh/id_ed25519.pub
    
    git config --global user.email "pbartmr@gmail.com"
    git config --global user.name "Bartolomeu Rodrigues"
    git config --global pager.diff false
    git config --global --add safe.directory '*'
    git config --global pull.rebase false

    cd ~/storage/shared/Documents/repositories
    git clone "git@github.com:Bartmr/my-notes.git"
    git clone "git@github.com:Bartmr/be-in-public.git"

    pkg install --no-install-recommends python python-pip
    
    bash be-in-public/scripts/install-dependencies.mobile.sh
    bash be-in-public/core/git/clone-repos.mobile.sh
    ```
    
- Install Obsidian
  - Open as vaults
    - my-notes
    - be-in-public
    - ne-xe
- Install Google Play Books
- Install Kindle
- Install Feedly
- Install Pocket
- `tech/social-media`
- install Google Calendar 
- install Google Contacts 
