
boards = {
        'alpine-db': {
            'name': 'Alpine DB', # A pretty name, just to name it
            'device_type': 'alpine-db', # The device-type that LAVA knows
            'defconfigs': ['arm-multi_v7_defconfig'], # This are the defconfigs you want to use with this board
                                                      # It must be available in kernel CI mainline subtree
            'dt': 'alpine-db', # The DT name (without extension)
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        #'alpine-v2-evp': { # Offline
        #    'name': 'alpine-v2-evp',
        #    'device_type': 'alpine-v2-evp',
        #    'defconfigs': ['arm64-defconfig'],
        #    'dt': 'al/alpine-v2-evp',
        #    'rootfs': 'rootfs_aarch64.cpio.gz',
        #    'test_plan': 'boot',
        #    'tests': ['first_test.sh'],
        #    },
        'armada-370-db': {
            'name': 'armada-370-db',
            'device_type': 'armada-370-db',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'armada-370-db',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh', 'crypto.sh', 'sata.sh'],
            },
        'armada-370-rd': {
            'name': 'Armada 370 RD',
            'device_type': 'armada-370-rd',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'armada-370-rd',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh', 'crypto.sh'],
            },
        'armada-3720-db': {
            'name': 'Armada 3720 DB',
            'device_type': 'armada-3720-db',
            'defconfigs': ['arm64-defconfig'],
            'dt': 'marvell/armada-3720-db',
            'rootfs': 'rootfs_aarch64.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        #'armada-3720-espressobin': { # Offline
        #    'name': 'Armada 3720 Espressobin',
        #    'device_type': 'armada-3720-espressobin',
        #    'defconfigs': ['arm64-defconfig'],
        #    'dt': 'marvell/armada-3720-espressobin',
        #    'rootfs': 'rootfs_aarch64.cpio.gz',
        #    'test_plan': 'boot',
        #    'tests': ['first_test.sh'],
        #    },
        'armada-375-db': { # Offline
            'name': 'armada-375-db',
            'device_type': 'armada-375-db',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'armada-375-db',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh', 'crypto.sh'],
            },
        'armada-385-db-ap': {
            'name': 'Armada 385 DB AP',
            'device_type': 'armada-385-db-ap',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'armada-385-db-ap',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh', 'crypto.sh'],
            },
        'armada-388-clearfog': {
            'name': 'Armada 388 Clearfog',
            'device_type': 'armada-388-clearfog',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'armada-388-clearfog',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh', 'crypto.sh'],
            },
        'armada-388-gp': {
            'name': 'Armada 388 GP',
            'device_type': 'armada-388-gp',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'armada-388-gp',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh', 'crypto.sh'],
            },
        #'armada-7040-db': { # Offline
        #    'name': 'armada-7040-db',
        #    'device_type': 'armada-7040-db',
        #    'defconfigs': ['arm64-defconfig'],
        #    'dt': 'armada-7040-db',
        #    'rootfs': 'rootfs_aarch64.cpio.gz',
        #    'test_plan': 'boot',
        #    'tests': ['first_test.sh'],
        #    },
        #'armada-8040-db': { # Offline
        #    'name': 'armada-8040-db',
        #    'device_type': 'armada-8040-db',
        #    'defconfigs': ['arm64-defconfig'],
        #    'dt': 'armada-8040-db',
        #    'rootfs': 'rootfs_aarch64.cpio.gz',
        #    'test_plan': 'boot',
        #    'tests': ['first_test.sh'],
        #    },
        'armada-398-db': {
            'name': 'Armada 398 DB',
            'device_type': 'armada-398-db',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'armada-398-db',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'armada-xp-db': { # NFS boot
            'name': 'Armada XP DB',
            'device_type': 'armada-xp-db',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'armada-xp-db',
            'rootfs': 'rootfs_armv7.tar.gz',
            'test_plan': 'boot-nfs',
            'tests': ['first_test.sh', 'crypto.sh'],
            },
        'armada-xp-gp': { # NFS boot
            'name': 'Armada XP GP',
            'device_type': 'armada-xp-gp',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'armada-xp-gp',
            'rootfs': 'rootfs_armv7.tar.gz',
            'test_plan': 'boot-nfs',
            'tests': ['first_test.sh', 'crypto.sh'],
            },
        'armada-xp-linksys-mamba': {
            'name': 'armada-xp-linksys-mamba',
            'device_type': 'armada-xp-linksys-mamba',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'armada-xp-linksys-mamba',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh', 'crypto.sh'],
            },
        'armada-xp-openblocks-ax3-4': {
            'name': 'Armada XP Openblocks AX3 4',
            'device_type': 'armada-xp-openblocks-ax3-4',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'armada-xp-openblocks-ax3-4',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh', 'crypto.sh'],
            },
        #'at91-sama5d2_xplained': { # Offline
        #    'name': 'at91-sama5d2_xplained',
        #    'device_type': 'at91-sama5d2_xplained',
        #    'defconfigs': ['arm-multi_v7_defconfig'],
        #    'dt': 'at91-sama5d2_xplained',
        #    'rootfs': 'rootfs_armv7.cpio.gz',
        #    'test_plan': 'boot',
        #    'tests': ['first_test.sh'],
        #    },
        'at91-sama5d4_xplained': {
            'name': 'AT91 sama5d4 Xplained',
            'device_type': 'at91-sama5d4_xplained',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'at91-sama5d4_xplained',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'at91rm9200ek': {
            'name': 'at91rm9200ek',
            'device_type': 'at91rm9200ek',
            'defconfigs': ['arm-at91_dt_defconfig'],
            'dt': 'at91rm9200ek',
            'rootfs': 'rootfs_armv4.tar.gz',
            'test_plan': 'boot-nfs',
            'tests': ['first_test.sh'],
            },
        'at91sam9261ek': {
            'name': 'at91sam9261ek',
            'device_type': 'at91sam9261ek',
            'defconfigs': ['arm-multi_v5_defconfig'],
            'dt': 'at91sam9261ek',
            'rootfs': 'rootfs_armv5.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'at91sam9m10g45ek': {
            'name': 'at91sam9m10g45ek',
            'device_type': 'at91sam9m10g45ek',
            'defconfigs': ['arm-multi_v5_defconfig'],
            'dt': 'at91sam9m10g45ek',
            'rootfs': 'rootfs_armv5.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'at91sam9x25ek': {
            'name': 'at91sam9x25ek',
            'device_type': 'at91sam9x25ek',
            'defconfigs': ['arm-multi_v5_defconfig'],
            'dt': 'at91sam9x25ek',
            'rootfs': 'rootfs_armv5.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'at91sam9x35ek': {
            'name': 'at91sam9x35ek',
            'device_type': 'at91sam9x35ek',
            'defconfigs': ['arm-multi_v5_defconfig'],
            'dt': 'at91sam9x35ek',
            'rootfs': 'rootfs_armv5.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'beagle-xm': {
            'name': 'beagle-xm',
            'device_type': 'beagle-xm',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'omap3-beagle-xm',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'beaglebone-black': {
            'name': 'BeagleBone Black',
            'device_type': 'beaglebone-black',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'am335x-boneblack',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh', 'mmc.sh'],
            'tests_multinode': ['network.yaml'],
            },
        #'berlin2q-marvell-dmp': { # No configuration in LAVA
        #    'name': 'berlin2q-marvell-dmp',
        #    'device_type': 'berlin2q-marvell-dmp',
        #    'defconfigs': ['arm-multi_v7_defconfig'],
        #    'dt': 'berlin2q-marvell-dmp',
        #    'rootfs': 'rootfs_armv7.cpio.gz',
        #    'test_plan': 'boot',
        #    'tests': ['first_test.sh'],
        #    },
        'imx6q-nitrogen6x': {
            'name': 'imx6q nitrogen6x',
            'device_type': 'imx6q-nitrogen6x',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'imx6q-nitrogen6x',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'kirkwood-db-88f6282': {
            'name': 'kirkwood-db-88f6282',
            'device_type': 'kirkwood-db-88f6282',
            'defconfigs': ['arm-mvebu_v5_defconfig'],
            'dt': 'kirkwood-db-88f6282',
            'rootfs': 'rootfs_armv5.tar.gz',
            'test_plan': 'boot-nfs',
            'tests': ['first_test.sh'],
            },
        'kirkwood-openblocks_a7': {
            'name': 'kirkwood-openblocks_a7',
            'device_type': 'kirkwood-openblocks_a7',
            'defconfigs': ['arm-mvebu_v5_defconfig'],
            'dt': 'kirkwood-openblocks_a7',
            'rootfs': 'rootfs_armv5.tar.gz',
            'test_plan': 'boot-nfs',
            'tests': ['first_test.sh', 'second_test.sh'],
            },
        'optimus-a80': {
            'name': 'optimus-a80',
            'device_type': 'optimus-a80',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'sun9i-a80-optimus',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'orion5x-rd88f5182-nas': {
            'name': 'orion5x-rd88f5182-nas',
            'device_type': 'orion5x-rd88f5182-nas',
            'defconfigs': ['arm-multi_v5_defconfig'],
            'dt': 'orion5x-rd88f5182-nas',
            'rootfs': 'rootfs_armv5.tar.gz',
            'test_plan': 'boot-nfs',
            'tests': ['first_test.sh'],
            },
        'sama5d3': {
            'name': 'sama5d3 Xplained',
            'device_type': 'sama53d',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'at91-sama5d3_xplained',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh', 'mmc.sh', 'usb.sh'],
            'tests_multinode': ['network.yaml'],
            },
        #'sama5d31ek': { # Offline (doesn't exists?)
        #    'name': 'sama5d31ek',
        #    'device_type': 'sama5d31ek',
        #    'defconfigs': ['arm-multi_v7_defconfig'],
        #    'dt': 'sama5d31ek',
        #    'rootfs': 'rootfs_armv7.cpio.gz',
        #    'test_plan': 'boot',
        #    'tests': ['first_test.sh'],
        #    },
        'sama5d34ek': {
            'name': 'sama5d34ek',
            'device_type': 'sama5d34ek',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'sama5d34ek',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        #'sama5d35ek': { # Offline (doesn't exists?)
        #    'name': 'sama5d35ek',
        #    'device_type': 'sama5d35ek',
        #    'defconfigs': ['arm-multi_v7_defconfig'],
        #    'dt': 'sama5d35ek',
        #    'rootfs': 'rootfs_armv7.cpio.gz',
        #    'test_plan': 'boot',
        #    'tests': ['first_test.sh'],
        #    },
        'sama5d36ek': { # Boots with some traces
            'name': 'sama5d36ek',
            'device_type': 'sama5d36ek',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'sama5d36ek',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'sama5d4ek': {
            'name': 'sama5d4ek',
            'device_type': 'sama5d4ek',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'sama5d4ek',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'sun5i-r8-chip': {
            'name': 'sun5i r8 chip',
            'device_type': 'sun5i-r8-chip',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'sun5i-r8-chip',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'sun6i-a31-app4-evb1': {
            'name': 'sun6i-a31-app4-evb1',
            'device_type': 'sun6i-a31-app4-evb1',
            'defconfigs': ['arm-sunxi_defconfig'],
            'dt': 'sun6i-a31-app4-evb1',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'sun8i-a23-evb': {
            'name': 'sun8i-a23-evb',
            'device_type': 'sun8i-a23-evb',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'sun8i-a23-evb',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        #'sun8i-a33-sinlinx-sina33': { # Offline
        #    'name': 'sun8i-a33-sinlinx-sina33',
        #    'device_type': 'sun8i-a33-sinlinx-sina33',
        #    'defconfigs': ['arm-multi_v7_defconfig'],
        #    'dt': 'sun8i-a33-sinlinx-sina33',
        #    'rootfs': 'rootfs_armv7.cpio.gz',
        #    'test_plan': 'boot',
        #    'tests': ['first_test.sh'],
        #    },
        'sun8i-a83t-allwinner-h8homlet-v2': {
            'name': 'sun8i-a83t-allwinner-h8homlet-v2',
            'device_type': 'sun8i-a83t-allwinner-h8homlet-v2',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'sun8i-a83t-allwinner-h8homlet-v2',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        'sun8i-h3-orangepi-pc': {
            'name': 'OrangePi PC',
            'device_type': 'sun8i-h3-orangepi-pc',
            'defconfigs': ['arm-multi_v7_defconfig'],
            'dt': 'sun8i-h3-orangepi-pc',
            'rootfs': 'rootfs_armv7.cpio.gz',
            'test_plan': 'boot',
            'tests': ['first_test.sh'],
            },
        }

