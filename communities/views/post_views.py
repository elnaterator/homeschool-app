from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpRequest
from ..models.post_models import Post, Comment
from ..utils import html_response


def posts(request: HttpRequest):

    if request.method == "GET":
        posts = Post.objects.all()
        context = {
            "posts": posts,
        }
        return html_response("posts", request, context)

    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            new_post = Post.objects.create(
                title=title, content=content, created_by=request.user
            )
            new_post.save()
        else:
            return HttpResponse(status=400, content="Bad Request")

    else:
        return HttpResponse(status=405, content="Method Not Allowed")
    

def post(request: HttpRequest, post_id: int):

    if request.method == "GET":
        post_id = request.GET.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        context = {"post": post}
        return html_response("post", request, context)

    elif request.method == "PUT":
        post_id = request.PUT.get("post_id")
        title = request.PUT.get("title")
        content = request.PUT.get("content")
        if post_id and (title or content):
            post = get_object_or_404(Post, pk=post_id)
            if title:
                post.title = title
            if content:
                post.content = content
            post.save()
        return html_response("post", request, context)

    elif request.method == "DELETE":
        post_id = request.DELETE.get("post_id")
        if post_id:
            post = get_object_or_404(Post, pk=post_id)
            post.delete()
        return html_response("posts", request, context)

    else:
        return HttpResponse(status=405, content="Method Not Allowed")
    

def post_comments(request: HttpRequest, post_id: int):
    
    if request.method == "GET":
        post = get_object_or_404(Post, pk=post_id)
        comments = post.comments.all()
        context = {"comments": comments}
        return html_response("comments", request, context)

    elif request.method == "POST":
        content = request.POST.get("content")
        if post_id and content:
            post = get_object_or_404(Post, pk=post_id)
            new_comment = Comment.objects.create(post=post, user=request.user, content=content)
            new_comment.save()
        else:
            return HttpResponse(status=400, content="Bad Request")

    else:
        return HttpResponse(status=405, content="Method Not Allowed")
    

def post_comment(request: HttpRequest, comment_id: int):
    
    if request.method == "GET":
        comment = get_object_or_404(Comment, pk=comment_id)
        context = {"comment": comment}
        return html_response("comment", request, context)

    elif request.method == "PUT":
        content = request.PUT.get("content")
        if content:
            comment = get_object_or_404(Comment, pk=comment_id)
            comment.content = content
            comment.save()
        return html_response("comment", request, context)

    elif request.method == "DELETE":
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.delete()
        return html_response("comments", request, context)

    else:
        return HttpResponse(status=405, content="Method Not Allowed")
