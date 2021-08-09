from exceptions import PermissionDenied


class Post:
    def __init__(self, content, author):
        """
        Creates a new Post by the author with the given content.
        You will need to track up votes more cleverly than previously because
        a user is only allowed to vote *once*.
        """
        self.content = content
        self.author = author
        self.upvotes = []

    def get_author(self):
        """
        Returns the author of the Post.
        """
        return self.author

    def get_content(self):
        """
        Returns the content of the Post.
        """
        return self.content

    def get_upvotes(self):
        """
        Returns a non-negative integer representing the total number of upvotes.
        """
        return len(self.upvotes)

    def set_content(self, content, by_user):
        """
        Called when the given user wants to update the content.
        * raises PermissionDenied if the given user is not the author.
        """
        if by_user == self.author:
            self.content = content
        else:
            raise PermissionDenied()

    def upvote(self, by_user):
        """
        Called when the given user wants to upvote this post.
        A user can only perform an up vote *once*.
        """
        if not by_user in self.upvotes:
            self.upvotes.append(by_user)
