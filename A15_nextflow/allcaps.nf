params.str = "Hello World"

workflow {
	//run the convert_to_caps() method
	convert_to_caps() | view
}

process convert_to_caps {
	output:
	stdout

	script:
	"""
	echo "Converting to caps..."
	echo ${params.str} | tr '[a-z]' '[A-Z]'
	"""

}
