from invoke import task
import os

# @task(help={
#     'ip': 'IP to listen on, defaults to *',
#     'extra': 'Port to listen on, defaults to 8888',
# })
@task
def lab(ctx, ip='*', port=8888):
    """Launch Jupyter lab
    """
    cmd = ['jupyter lab', '--ip={}'.format(ip), '--port={}'.format(port)]
    ctx.run(' '.join(cmd))


# @task(help={
#     'ip': 'IP to listen on, defaults to *',
#     'extra': 'Port to listen on, defaults to 8888',
# })
@task
def notebook(ctx, ip='*', port=8888):
    """Launch Jupyter notebook
    """
    cmd = ['jupyter notebook', '--ip={}'.format(ip), '--port={}'.format(port)]
    ctx.run(' '.join(cmd))

@task
def getdata(ctx):
    """Get kaggle data from source & save to data/raw
    """
    cmd = ['python',
           os.path.join('{{ cookiecutter.project_module_name }}',
                         'data',
                         'make_dataset.py')
          ]
    ctx.run(' '.join(cmd))