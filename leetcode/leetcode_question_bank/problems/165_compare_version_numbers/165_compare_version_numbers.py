class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if version1 and version2:
            v1_revisions = version1.split(".")
            v2_revisions = version2.split(".")

            if v1_revisions and v2_revisions:
                if len(v1_revisions) < len(v2_revisions):
                    for i in range(len(v1_revisions)):
                        r1 = int(v1_revisions[i])
                        r2 = int(v2_revisions[i])
                        if r1 < r2:
                            return -1
                        elif r1 > r2:
                            return 1
                    for j in range(i+1, len(v2_revisions)):
                        r2 = int(v2_revisions[j])
                        if 0 < r2:
                            return -1
                        elif 0 > r2:
                            return 1
                    return 0
                elif len(v1_revisions) > len(v2_revisions):
                    for i in range(len(v2_revisions)):
                        r1 = int(v1_revisions[i])
                        r2 = int(v2_revisions[i])
                        if r1 < r2:
                            return -1
                        elif r1 > r2:
                            return 1
                    for j in range(i+1, len(v1_revisions)):
                        r1 = int(v1_revisions[j])
                        if r1 < 0:
                            return -1
                        elif r1 > 0:
                            return 1
                    return 0
                else:
                    for i in range(len(v1_revisions)):
                        r1 = int(v1_revisions[i])
                        r2 = int(v2_revisions[i])
                        if r1 < r2:
                            return -1
                        elif r1 > r2:
                            return 1
                    return 0
