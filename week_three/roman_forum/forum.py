from post import Post
from thread import Thread


class Forum:
    def __init__(self):
        """
        Perform initialisation of a new Forum object, as needed.
        """
        self.threads = []

    def get_threads(self):
        """
        Returns a list of Threads in the Forum, in the order that they were published.
        """
        return self.threads

    def publish(self, title, content, author):
        """
        Creates a new Thread with the given title and adds it to the Forum.
        The content and author are provided to allow you to create the first Post object.
        Threads are stored in the order that they are published.
        Returns the new Thread object.
        """
        newThread = Thread(title, Post(content, author))
        self.threads.append(newThread)
        return newThread

    def search_by_tag(self, tag):
        """
        Searches all forum Threads for any that contain the given tag.
        Returns a list of matching Thread objects in the order they were published.
        """
        matchingThreads = []
        for thread in self.threads:
            if tag in thread.tags:
                matchingThreads.append(thread)
        return matchingThreads

    def search_by_author(self, author):
        """
        Searches all forum Threads for Posts by the given author.
        Returns a list of matching Post objects in any order you like.
        """
        matchingPosts = []
        for thread in self.get_threads():
            for post in thread.get_posts():
                if post.author == author:
                    matchingPosts.append(post)
        return matchingPosts
