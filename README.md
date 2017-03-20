# Custom Test Tool

## Setup

  * Make yourself a virtualenv, or just install system wide the packages listed
in `./requirements.txt`.

```
virtualenv --python=python3 env
source env/bin/activate
pip install -r requirements.txt
```
  * That file can help you a lot not providing every argument every time you run
the script:

```
$ cat ~/.cttrc
[ctt]
server: https://my.lava.instan.ce/RPC2
username: <lava_username>
token: MyAwEsOmELAVAtOkEn
stream: /anonymous/test/
ssh_server: 192.168.1.3
ssh_username: user-with-write-access-somewhere
api_token: my-awesome-token
rootfs_path: /root/buildroot-ci/out/
```

  * `server` is the LAVA API address.
  * `username` is the LAVA username you will use to send jobs.
  * `token` is the LAVA token corresponding to the previous username.
  * `stream` is the LAVA bundle stream to store the jobs results.
  * `ssh_server` is used to upload custom files on the server running LAVA.
  * `ssh_username` is the username you will use to upload file to the server.
  * `api_token` is needed to access KernelCI's API.
  * `rootfs_path` is where you store your rootfs. It can be a path local to the
server your sending the job, as long as it actually contains valid rootfs.

## Examples

Before any work, don't forget to reactivate your virtualenv to setup the Python
environment: `source env/bin/activate`

`./ctt.py -h`

Will give you exhaustive help on any option.

`./ctt.py -l`

Will give you list of supported boards.

`./ctt.py -b sun8i-h3-orangepi-pc beaglebone-black --send`

Will launch the default job on the OrangePi PC and Beaglebone Black. The default
job consists in running the test suite using the latest mainline kernel provided
by Kernel CI

`./ctt.py -b sun8i-h3-orangepi-pc beaglebone-black --send --upload --kernel ../path/to/my/kernel/zImage`

Will do quite the same but will upload a custom kernel instead of using KernelCI's one.

The same way you can use `--rootfs`, `--dtb`, `--modules` to override the
corresponding files.

Be careful when you upload multiple time the same file name, since the storage
is made on a per-user basis: you risk to override your own previous file.   
To prevent this, just name your file differently.

## Adding a new board

If you wish to add a new board to the custom test tool, it must already be in
LAVA (required), as well as being supported by kernel CI's images (optionnal,
you can manually provide your own files).

Then just edit the `boards.py` file. It contains just a Python dictionnary, and
it's thus easy to add a new board:

```python
'beaglebone-black': { # The key is free to choose. Usally the DT name is a good
                      # choice, but it's not mandatory
    'name': 'BeagleBone Black', # A pretty name for displaying, also free
    'device_type': 'beaglebone-black', # This is the device-type as named is the
                                       # LAVA configuration
    'defconfigs': ['arm-multi_v7_defconfig'], # This is a list of defconfigs
                                              # built by Kernel CI.
                                              # This value can be found at
                                              # https://storage.kernelci.org/mainline/v4.11.xxx-XXXXXX
                                              # for example.
    'dt': 'am335x-boneblack', # This is the DT name as found in the kernel,
                              # without the extension.
    'rootfs': 'rootfs_armv7.cpio.gz', # The name of the rootfs you want to use.
                                      # It must be available under the
                                      # --rootfs-path option (or rootfs_path in
                                      # the .cctrc file).
    'test_plan': 'boot', # What LAVA test to you want tu run (only boot is
                         # supported)
    'tests': ['first_test.sh', 'mmc.sh'], # A list of test that can be (and
                                          # will) be launched on the board.
                                          # They will be run from the
                                          # /tests/tests/ folder in the rootfs.
    },
```

