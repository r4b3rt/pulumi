import pulumi
import pulumi_simple as simple

aresource = simple.Resource("aresource", value=True)
other = simple.Resource("other", value=True)
