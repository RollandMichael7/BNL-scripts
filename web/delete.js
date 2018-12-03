// number of paused PVs before deletion
var numPaused = 0;
// array of paused PV names
var pausedPVs = [];

// print to paragraph element
function print(s) {
	$("#output").append("\t" + s);
}

// list all PVs that match regex, indicating whether they are paused
function listPVs() {
	var regex = $("#regex").val();
	$("#output").text("\tContacting server...\n");
	$.ajax({
		url: '../bpl/getAllPVs',
		dataType: 'json',
		data: { 
			limit: 30000, 
			pv: regex 
		},
		type: 'GET',
		success: function(names) {
			if (names.length < 1) {
				print("No PVs matched the regex.");
				return
			}
			console.log(names);
			$.ajax({
				url: '../bpl/getPausedPVsReport',
				dataType: 'json',
				type: 'GET',
				success: function(data) {
					$("#output").text("");
					console.log(data);
					confirmPause(names, data, 1);
					print("\n\n");
					print(names.length + " PV(s) found, " + numPaused + " currently paused.");
					$('#outputArea').scrollTop($('#outputArea')[0].scrollHeight - $('#outputArea')[0].clientHeight); // scroll to bottom
				},
				error: function() {
					print("ERROR: Could not pause PVs.");
				}
			});
		},
		error: function() {
			// TODO: be more specific about error
			$("#output").text("There was an error.");
		}
	});
}

// pause all PVs matching regex
function pausePVs() {
	var regex = $("#regex").val();
	$("#output").text("\tContacting server...\n");
	$.ajax({
		url: '../bpl/pauseArchivingPV',
		dataType: 'json',
		data: {
			pv: regex
		},
		type: 'GET',
		success: function(data) {
			console.log(data);
			print("Paused PVs.");
		},
		error: function(data) {
			console.log(data);
			print("ERROR: Could not pause PVs");
		}
	});
}

// delete all PVs matching regex that are currently paused
function deletePVHandler() {
	var regex = $("#regex").val();
	$("#output").text("\tContacting server...\n");
	$.ajax({
		url: '../bpl/getAllPVs',
		dataType: 'json',
		data: { 
			limit: 30000, 
			pv: regex 
		},
		type: 'GET',
		success: function(names) {
			if (names.length < 1) {
				print("No PVs matched the regex.");
				return
			}
			console.log(names);
			$("#output").text("");
			if (confirm("You are about to delete up to " + names.length + " PVs. Are you sure you want to continue?")) {
				print("Confirming PVs are paused...\n");
				$.ajax({
					url: '../bpl/getPausedPVsReport',
					dataType: 'json',
					type: 'GET',
					success: function(report) {
						console.log(report);
						var ret = confirmPause(names, report, 0);
						if (ret == -1)
							return;
						print("There are " + numPaused + " paused PVs that match the regex.\n\n");
						if (numPaused == 0)
							return;
						var type = $("#deleteType").val();
						var doDelete = "";
						if (type === "stop")
							doDelete="false";
						else if (type === "delete")
							doDelete="true";
						else {
							print("could not determine delete type");
							return;
						}
						for (var i=0; i<numPaused; i++) {
							$.ajax({
								url: '../bpl/deletePV',
								dataType: 'json',
								data: {
									pv: pausedPVs[i],
									deleteData: doDelete
								},
								type: 'GET',
								success: function(data) {
									console.log(data);
									print(data["desc"] + "\n");
								},
								error: function(data) {
									console.log(data);
									print("ERROR: Could not delete\n");
								}
							});
						}
					},
					error: function() {
						print("ERROR: Could not find paused PVs.");
					}
				});
			}
			else {
				print("Operation aborted.");
			}
		},
		error: function() {
			// TODO: be more specific about error
			$("#output").text("There was an error.");
		}
	});
}

// using the JSONs returned from listAllPVs and getPausedPVsReport,
// determine which PVs matching regex are currently paused (and thus eligible for deletion)
// if doPrint is true, print each PV name in color according to whether it is paused
function confirmPause(names, pausedData, doPrint) {
	if (!(Boolean(doPrint)) && pausedData.length < 1) {
	 	print("There are no currently paused PVs.");
	 	return -1;
	}	
	numPaused = 0;
	pausedPVs = [];
	var pausedNames = [];
	var newNames = [];
	// compare names case-insensitively, but original name is stored
	// in list of names for deletion
	for (var i=0; i<names.length; i++)
		newNames[i] = names[i].toUpperCase();
	for (var i=0; i<pausedData.length; i++) {
		pausedNames[i] = pausedData[i]["pvName"].toUpperCase();
	}
	for (var i=0; i<newNames.length; i++) {
		if (pausedNames.includes(newNames[i])) {
			if(Boolean(doPrint))
				print('<span class="good">' + names[i] + '</span>\n');
			pausedPVs[numPaused] = names[i];
			numPaused++;
		}
		else {
			if (Boolean(doPrint))
				print('<span class="bad">' + names[i] + '</span>\n');
		}
	}
	return 0;
}

// list the names of all currently paused PVs
function pauseReport() {
	$("#output").text("");
	$.ajax({
		url: '../bpl/getPausedPVsReport',
		dataType: 'json',
		type: 'GET',
		success: function(data) {
			console.log(data);
			for (var i=0; i<data.length; i++) {
				print(data[i]["pvName"] + "\n");
			}
			print("\n");
			print("There are " + data.length + " PVs currently paused.");
		},
		error: function() {
			// TODO: be more specific about error
			$("#output").text("There was an error.");
		}
	});
}
