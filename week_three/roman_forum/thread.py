from exceptions import PermissionDenied


class Thread:
    def __init__(self, title, first_post):
        """
        Creates a new thread with a title and an initial first post.
        The author of the first post at the time of thread creation is the owner of the thread.
        The owner cannot change once the thread is created.
        """
        self.title = title
        self.owner = first_post.author
        self.tags = []
        self.posts = [first_post]

    def get_owner(self):
        """
        Returns the owner of the thread.
        """
        return self.owner

    def get_title(self):
        """
        Returns the title of the thread.
        """
        return self.title

    def get_tags(self):
        """
        Returns a sorted list of unique tags.
        """
        return sorted(self.tags)

    def get_posts(self):
        """
        Returns a list of Post objects in this thread, in the order they were published.
        """
        return self.posts

    def publish_post(self, post):
        """
        Adds the given Post object into the list of Posts in this thread.
        """
        self.posts.append(post)

    def remove_post(self, post, by_user):
        """
        Allows the given user to remove the Post from this thread.
        Does nothing if the Post is not in this thread.
        * raises PermissionDenied if the given user is not the author of the post.
        """
        postToRemove = None
        for currentPost in self.posts:
            if currentPost.author == post.author and currentPost.content == post.content:
                postToRemove = currentPost

        if postToRemove:
            if postToRemove.author == by_user:
                self.posts.remove(postToRemove)
            else:
                raise PermissionDenied()

    def set_title(self, title, by_user):
        """
        Allows the given user to edit the thread title.
        * raises PermissionDenied if the given user is not the owner of the thread.
        """
        if by_user == self.owner:
            self.title = title
        else:
            raise PermissionDenied()

    def set_tags(self, tag_list, by_user):
        """
        Allows the given user to replace the thread tags (list of strings).
        * raises PermissionDenied if the given user is not the owner of the thread.
        """
        if by_user == self.owner:
            uniqueTags = []
            for tag in tag_list:
                if not tag in uniqueTags:
                    uniqueTags.append(tag)
            self.tags = uniqueTags
        else:
            raise PermissionDenied()
