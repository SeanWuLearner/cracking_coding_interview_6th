
def build_order(projects, dependencies):
    def rm_dep_projects(prj):
        nonlocal dep_by
        nonlocal dep_on
        nonlocal output
        for p in dep_by[prj]:
            dep_on[p].discard(prj)
            if len(dep_on[p]) == 0:
                del dep_on[p]
                output.append(p)
                rm_dep_projects(p)

    dep_by = dict()
    dep_on = dict()
    no_dep = set(projects)

    # build table
    for prj in projects:
        dep_by[prj] = set()
        dep_on[prj] = set()

    for dep in dependencies:
        dep_by[dep[0]].add(dep[1])
        dep_on[dep[1]].add(dep[0])
        no_dep.discard(dep[1])

    output = []
    for prj in no_dep:
        del dep_on[prj]
        output.append(prj)
        rm_dep_projects(prj)

    # check if all projects are done.
    if len(dep_on) != 0:
        output = None

    print(output)
    return output

def is_valid_order(builds, deps):
    '''Check validity used by test func (brute-force) '''
    done = set()
    for prj in builds:
        for dep in deps:
            if dep[1] == prj:
                if dep[0] not in done:
                    return False
        done.add(prj)
    return True

def test_func():
    projects = { 'a', 'b', 'c', 'd', 'e', 'f'}
    dependencies = [
        ['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']
    ]
    builds = build_order(projects, dependencies)
    assert True == is_valid_order(builds, dependencies)

    ## test case 2: circular dependency.
    projects = { 'a', 'b', 'c', 'd', 'e', 'f'}
    dependencies = [
        ['b','a'], ['c', 'b'], ['d', 'c'], ['a','d']
    ]
    assert None == build_order(projects, dependencies)
