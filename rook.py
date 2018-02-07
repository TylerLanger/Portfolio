rookx=int(input("input current rook x position: "))
rooky=int(input("input current rook y position: "))
desiredx=int(input("input desired rook y position: "))
desiredy=int(input("input desired rook X position: "))

if rookx==desiredx and rooky!=desiredy: #if no x change
    print("YES")
elif rookx!=desiredx and rooky==desiredy: #if no y change
    print("YES")
elif rookx!=desiredx and rooky!=desiredy: #if x and y change
    print("NO")
elif rookx==desiredx and rooky==desiredy: #if no change
    print("ALREADY HERE")
    
