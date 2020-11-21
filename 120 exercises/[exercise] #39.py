import pkg_resources
installedPackages = pkg_resources.working_set
installedPackagesList = sorted(["%s==%s" % (i.key, i.version) for i in installedPackages])

for m in installedPackagesList:
    print(m)
    