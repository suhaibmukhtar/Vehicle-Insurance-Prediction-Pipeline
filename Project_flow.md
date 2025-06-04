## How to perform SSH Authentication on Github
### Clone the repo
1. <b>Clone the github repository</b>: 
```
git clone "repo-url"
```
### Generate SSH key
2. <b>Generate SSh Key using below command</b>
```
ssh-keygen -t rsa -b 4096 -C "suhaibmukhtar2@gmail.com"
```
"This will generate two keys public and private key"<br>
3. <b> Add the id_rsa.pub key inside the SSH keys of github</b>
#### Procedure to Add SSH key on Github
Go to GitHub → Settings → SSH and GPG Keys
→ Click New SSH Key
→ Paste your key, give it a name like “Windows-Laptop”
→ Click Add SSH Key

4. <b>Test SSH Connection</b>
```
ssh -T git@github.com
```
#### Response
"Hi suhaibmukhtar! You've successfully authenticated, but GitHub does not provide shell access.<br>
5. <b>Clone a Repo via SSH</b>
```"
git clone git@github.com:username/repo-name.git
```
<b>Optional: Set SSH as Default for Git Remotes</b>
```
git remote set-url origin git@github.com:username/repo-name.git
```
<b>Check</b>
```
git remote -v
```
## Step to follow after SSH
<ol>
    <li>Create the Project template by executing 'template.py' file.</li>
    <li>Write code on 'setup.py' and project.toml to import local packages</li>
</ol>
