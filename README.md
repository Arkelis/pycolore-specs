# Pycolore COPR Repository SPEC files

This repository contains spec files used for building packages on Fedora COPR service.

There is one COPR repo for each packaged software and a repository containing them all :

* [`arkelis/Pycolore`](https://copr.fedorainfracloud.org/coprs/arkelis/Pycolore/)
* [`arkelis/gitkraken`](https://copr.fedorainfracloud.org/coprs/arkelis/gitkraken/) : provides [GitKraken](https://www.gitkraken.com)
* [`arkelis/yaru`](https://copr.fedorainfracloud.org/coprs/arkelis/yaru/) : provides [Yaru](https://github.com/ubuntu/yaru) Gnome Shell and GTK+ theme, which was known as Ubuntu Community Theme.

## Usage

In order to use this repos (for example Pycolore) :

```
# dnf copr enable arkelis/Pycolore
```

And install a package (for example GitKraken) :

```
# dnf install gitkraken
```

## Build status

| Package | Build status |
|:--------|:-------------|
| Yaru Theme | [![Copr build status](https://copr.fedorainfracloud.org/coprs/arkelis/yaru/package/yaru/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/arkelis/yaru/package/yaru/) |
| GitKraken | [![Copr build status](https://copr.fedorainfracloud.org/coprs/arkelis/gitkraken/package/gitkraken/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/arkelis/gitkraken/package/gitkraken/) |

Informations en français sur ce dépôt : [pycolore.fr](https://www.pycolore.fr/depot-dnf/)
