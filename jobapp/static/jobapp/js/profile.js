$(document).ready(function(){
    // callbacks
    // id selector to grab data -- $("#job1_description").val()
    // make post request here passing in data to pranav's url

	$("#UpdateProfileButton").click(function() { //when I click the update profile button at the bottom of the profile page //
        console.log("hi");
        csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        referrer_fname = $('#referrer_fname').val(); //left side is creating a javascript variable, right side is taking the data from the inputs //
        referrer_lname = $('#referrer_lname').val();
        referrer_job_title = $('#referrer_job_title').val();
        referrer_company_name = $('#referrer_company_name').val();
        referrer_location = $('#referrer_location').val();

        job1_job_id = $('#job1_job_id').val();
        job1_job_title = $('#job1_job_title').val();
        job1_company_name = $('#job1_company_name').val();
        job1_job_description = $('#job1_job_description').val();
        job1_location = $('#job1_location').val();
        job1_salary_min = $('#job1_salary_min').val();
        job1_salary_max = $('#job1_salary_max').val();
       	job1_careerlevel = $('input:radio[name=job1_careerlevel]:checked').val()
        job1_additional_comments = $('#job1_additional_comments').val();
        job1_glassdoor_link = $('#job1_glassdoor_link').val();

        job2_job_id = $('#job2_job_id').val();
		job2_job_title = $('#job2_job_title').val();
		job2_company_name = $('#job2_company_name').val();
        job2_job_description = $('#job2_job_description').val();
        job2_location = $('#job2_location').val();
        job2_salary_min = $('#job2_salary_min').val();
        job2_salary_max = $('#job2_salary_max').val();
       	job2_careerlevel = $('input:radio[name=job2_careerlevel]:checked').val()
        job2_additional_comments = $('#job2_additional_comments').val();
        job2_glassdoor_link = $('#job2_glassdoor_link').val();

        job3_job_id = $('#job3_job_id').val();
		job3_job_title = $('#job3_job_title').val();
		job3_company_name = $('#job3_company_name').val();
        job3_job_description = $('#job3_job_description').val();
        job3_location = $('#job3_location').val();
        job3_salary_min = $('#job3_salary_min').val();
        job3_salary_max = $('#job3_salary_max').val();
       	job3_careerlevel = $('input:radio[name=job3_careerlevel]:checked').val()
        job3_additional_comments = $('#job3_additional_comments').val();
        job3_glassdoor_link = $('#job3_glassdoor_link').val();

        //send this data to the backend to replace whatever is in the database right now//

        //create a dictionary where left side is the backend side and right side is front end; this will help the backend parse through the dictionary// 

        $('#UpdateProfileButtonLoader').removeClass("hide"); // display loader

	    $.post( "/update_user/", {

	    	csrfmiddlewaretoken: csrfmiddlewaretoken,

	    	company: referrer_company_name, 
	    	fname: referrer_fname, 
	    	lname: referrer_lname,
	    	job_title: referrer_job_title,
            location: referrer_location,

	    	job_id1: job1_job_id,
	    	job_title1: job1_job_title,
	    	location1: job1_location,
	    	job_companyname1: job1_company_name,
	    	job_description1: job1_job_description,
	    	location1: job1_location,
	    	salary_min1: job1_salary_min,
	    	salary_max1: job1_salary_max,
	    	career_level1: job1_careerlevel,
	    	additional_comments1: job1_additional_comments,
	    	glassdoor_link1: job1_glassdoor_link,

	    	job_id2: job2_job_id,
	    	job_title2: job2_job_title,
	    	location2: job2_location,
	    	job_companyname2: job2_company_name,
	    	job_description2: job2_job_description,
	    	location2: job2_location,
	    	salary_min2: job2_salary_min,
	    	salary_max2: job2_salary_max,
	    	career_level2: job2_careerlevel,
	    	additional_comments2: job2_additional_comments,
	    	glassdoor_link2: job2_glassdoor_link,

	    	job_id3: job3_job_id,
	    	job_title3: job3_job_title,
	    	location3: job3_location,
	    	job_companyname3: job3_company_name,
	    	job_description3: job3_job_description,
	    	location3: job3_location,
	    	salary_min3: job3_salary_min,
	    	salary_max3: job3_salary_max,
	    	career_level3: job3_careerlevel,
	    	additional_comments3: job3_additional_comments,
	    	glassdoor_link3: job3_glassdoor_link,

	    }).done(function( data ) {
	    	console.log("Data Loaded: ", data); //make a nice alert later on //
            if (data.response == 1) {
                // hide ajax loader gif img here
                $('#UpdateProfileButtonDanger').addClass("hide"); // hide
                $('#UpdateProfileButtonSuccess').removeClass("hide"); // show
                $('#UpdateProfileButtonLoader').addClass("hide"); // hide loader
            }
            else {
                $('#UpdateProfileButtonSuccess').addClass("hide");
                $('#UpdateProfileButtonDanger').removeClass("hide");
                $('#UpdateProfileButtonLoader').addClass("hide"); // hide loader
            }
  		});
  	})
})

	    	//note: to find and replace all, press escape, apple find, type, find all, type what you want to replace //
