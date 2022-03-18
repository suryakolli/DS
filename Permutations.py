def permute(self, A):
		soln = []
        
    if len(A) == 1:
        return [A[:]]

    for i in range(len(A)):
        curr = A.pop(0)

        perms = self.permute(A)

        for perm in perms:
            perm.append(curr)

        soln.extend(perms)

        A.append(curr)


    return soln
