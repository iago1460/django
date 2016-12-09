from invoke import task


@task(default=True)
def make(ctx):
    ctx.run('python manage.py makemessages --ignore=venv/* --all')


@task
def compile(ctx):
    ctx.run('python manage.py compilemessages')


@task(make)
def push_to_transifex(ctx):
    ctx.run('tx push --source')


@task(post=[compile])
def pull_from_transifex(ctx):
    ctx.run('tx pull --translations --all')
