from django.shortcuts import render
from data.models import Workflow
from upload.forms import WorkflowForm
# Create your views here.
def add_workflow(request):
    form = WorkflowForm()
    if request.method == 'POST':
        form = WorkflowForm(request.POST, request.FILES)

        # Have we been provided with a valid form
        if form.is_valid():

            workflowFile = form.cleaned_data['json']
            file_data = workflowFile.read().decode('utf-8')
            form.instance.json = file_data
			# Save the new category to the database
            form.save(commit=True)
			# Now that the category is saved
			# We could give a confirmation message
			# But since the most recent category added is on the index page
			# Then we can direct the user back to the index page
            msg = "Se ha anadido el workflow correctamente"
            return render(request, 'upload/add_workflow.html', {'msg': msg})
        else:
			# The supplied form contained errors -
			# just print them to the terminal
            print(form.errors)
	# Will handle the bad form, new form, or no form supplied cases.
	# Render the form with error messages (if any
    return render(request, 'upload/add_workflow.html', {'form': form})
