# Ansible Role: `squid`

## Description

These tasks are set up to take Squid-Cache and turn it into a reverse proxy.

There are several cool things this setup does:

* Preserves directory path during
    * Old domain name to new domain name redirects
    * Http to https redirects
* Certain subdirectories are forwarded to separate web servers
    * / => blog
    * /gitlist => git repo
    * /bu-node => bitcoin unlimited node web stats
    * /nextcloud => nextcloud server
* Https termination
    * Passed [SSLLabs](https://www.ssllabs.com/) with a score of 'A'

## Requirements

* RHEL only

## Role Variables

```yaml
variable: value # comment
```

## Tags

### Role-Specific tags:

* `squid`
* `squid_install`
* `squid_config`

### Global tags:

* `install`
* `config`
* `update`

## Dependencies

## Example Playbook

```yaml
- name: Common roles
  hosts: all
  remote_user: root
  #no_log: true

  roles:
    - common
    - iptables
    - squid
```

## License

MIT / BSD

## Author Information

This role was created in 2017 by [Andrew Cz](https://andrewcz.com), a student at The Ohio State University.
