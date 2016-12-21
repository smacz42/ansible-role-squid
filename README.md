# Ansible Role: squid

## Description

Installs a squid web proxy and configures it to be an accelerator (reverse proxy) for various sites. Can accommodate one IP address, and one or more subdirectories. Defaults to HTTPS and terminates TLS connection.

## Requirements


## Role Variables

```yaml
variable: value # comment
```

## Dependencies



## Example Playbook

```yaml
- name: Configure squid reverse proxy
  hosts: all
  gather_facts: yes

  roles:
    - { role: squid }
```

## License

Licensed under the MIT License. See the LICENSE file for details.

## Author Information

This role was created in YYYY by [Andrew Cz](https://hobbithole.blue), a student at The Ohio State University.
