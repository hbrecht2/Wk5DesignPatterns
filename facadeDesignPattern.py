class BlogFacade(object):
    def showPostandComments(self):
        self.newPost = newPost()
        title = self.newPost.getTitle()
        article = self.newPost.getArticle()
        
        self.newComment = newComment()
        comment = self.newComment.getComment()
        
        print ("\n{}\n{}\n\nComments:\n{}".format(title, article, comment))
            
class newPost(object):
    def getTitle(self):
        title = input("What is the title of your new blog post?")
        return title
    
    def getArticle(self):
        articleContent = input("\nEnter article content here:")
        return articleContent
    

class newComment(object):
    def getComment(self):
        comment = input("\nShare feedback with the author here..")
        return comment
    
def main():
    blogPost = BlogFacade()
    blogPost.showPostandComments()
    
main()