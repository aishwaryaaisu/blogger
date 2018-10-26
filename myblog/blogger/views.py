from django.shortcuts import render,HttpResponse,redirect
from blogger.models import blogpost,Comment


def home(request):
	posts=blogpost.objects.all()
	# for posts in posts:
	# 	print(posts)
	# # print(type(posts))

	return render(request,"home.html",{"posts":posts})


def post_page(request, post_id):
	mypost=blogpost.objects.get(pk=post_id)
	comments=Comment.objects.filter(post=mypost)

	
	context={"post":mypost,"comments":comments}
	return render(request,"post.html",context)

def post_comment(request,post_id):
	if request.method=="POST":
		comment=request.POST['comment']
		print(comment)

		user=request.user
		print(user)
		post=blogpost.objects.get(pk=post_id)
		comment1=Comment(post=post,text=comment,user=user)
		comment1.save()
		return redirect(f"/post/{post_id}")

	





