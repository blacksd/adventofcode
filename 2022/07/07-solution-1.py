from anytree import AnyNode, RenderTree, PostOrderIter

current_dir = None
root = None
with open("07-input.txt") as f:
    lines = f.readlines()
    for line in lines:
        sanitized_line = line.strip()
        if sanitized_line[0] == "$":
            if sanitized_line[2:4] == "cd":
                # Branch: change dir

                new_current_dir = sanitized_line[5:]
                # if .., go up one level
                # meaning, look for its parent and set it as the new cd
                if new_current_dir == "..":
                    current_dir = current_dir.parent
                # otherwise, this becomes the new cd
                # I need to set a parent relationship
                else:
                    if current_dir is not None:
                        # there's a parent, set it
                        current_dir = AnyNode(
                            id=new_current_dir,
                            parent=current_dir,
                            files={},
                            total_size=0,
                        )
                    else:
                        # this is root!
                        root = AnyNode(id=new_current_dir, files={}, total_size=0)
                        current_dir = root
            else:
                # ls
                next
        else:
            if sanitized_line[0:3] == "dir":
                next
            else:
                # file, finally
                file_name = sanitized_line.split(" ")[1]
                file_length = int(sanitized_line.split(" ")[0])
                current_dir.files.update({file_name: file_length})

for node in PostOrderIter(root):
    node_size = sum(node.files.values())
    node.total_size += node_size
    if node.parent is not None:
        node.parent.total_size += node.total_size

print(RenderTree(root))

total = 0
for node in PostOrderIter(root, filter_=lambda n: n.total_size < 100000):
    total += node.total_size

print(f"The sum of the directories with files that add up to at most 100000 is {total}")
