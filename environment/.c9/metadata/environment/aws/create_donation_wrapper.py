{"filter":false,"title":"create_donation_wrapper.py","tooltip":"/aws/create_donation_wrapper.py","undoManager":{"mark":32,"position":32,"stack":[[{"start":{"row":0,"column":0},"end":{"row":49,"column":0},"action":"insert","lines":["import boto3","import json","from botocore.exceptions import ClientError","","# Initialize a boto3 client for AWS Lambda","lambda_client = boto3.client('lambda', region_name='us-east-1')","","# Lambda function details","FUNCTION_NAME = 'get_categories'","RUNTIME = 'python3.11'","ROLE_ARN = 'arn:aws:iam::701068225110:role/LabRole' # User the LearnerLab LabRole","HANDLER = 'get_categories_code.lambda_handler'","S3_BUCKET = 'assignmentlambdabucket'","S3_KEY = 'get_categories_code.zip'  # The zip file containing your Lambda function code","","def create_lambda_function():","    try:","        response = lambda_client.create_function(","            FunctionName=FUNCTION_NAME,","            Runtime=RUNTIME,","            Role=ROLE_ARN,","            Handler=HANDLER,","            Code={","                'S3Bucket': S3_BUCKET,","                'S3Key': S3_KEY","            },","            Description='Lambda function to get categories from RDS.',","            Environment={","                'Variables': {","                    'RDS_HOST': 'foodsharehub.c1wc4i62kq5k.us-east-1.rds.amazonaws.com',","                    'RDS_USER': 'cadadmin',","                    'RDS_PASSWORD': 'cadpassword',","                    'RDS_DB_NAME': 'foodsharehub'","                }","            }","        )","        ","        print(json.dumps(response, indent=4))","        return response","    except ClientError as e:","        print(f\"An error occurred: {e}\")","        return None","","# Call the function to create the Lambda","create_lambda_response = create_lambda_function()","if create_lambda_response:","    print(f\"Created Lambda function: {create_lambda_response['FunctionName']}\")","else:","    print(\"Failed to create Lambda function\")",""],"id":1}],[{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"remove","lines":["t"],"id":2},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"remove","lines":["e"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":["g"]}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["c"],"id":3},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["r"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["e"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["a"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["t"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"remove","lines":["s"],"id":4},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"remove","lines":["e"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"remove","lines":["i"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"remove","lines":["r"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"remove","lines":["o"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"remove","lines":["g"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"remove","lines":["e"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"remove","lines":["t"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["a"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["c"]}],[{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["d"],"id":5},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["o"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["n"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["a"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["t"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["i"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["o"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["n"]}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"remove","lines":["t"],"id":6},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"remove","lines":["e"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"remove","lines":["g"]}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["c"],"id":7},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["r"]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["e"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["a"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["t"]},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"remove","lines":["s"],"id":8},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"remove","lines":["e"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["i"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["r"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"remove","lines":["o"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"remove","lines":["g"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"remove","lines":["e"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"remove","lines":["t"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["a"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"remove","lines":["c"]}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["d"],"id":9},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["o"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["n"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["a"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["t"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["i"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["o"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["n"]}],[{"start":{"row":26,"column":44},"end":{"row":26,"column":67},"action":"remove","lines":["get categories from RDS"],"id":10}],[{"start":{"row":26,"column":44},"end":{"row":26,"column":45},"action":"insert","lines":["c"],"id":11},{"start":{"row":26,"column":45},"end":{"row":26,"column":46},"action":"insert","lines":["r"]},{"start":{"row":26,"column":46},"end":{"row":26,"column":47},"action":"insert","lines":["e"]},{"start":{"row":26,"column":47},"end":{"row":26,"column":48},"action":"insert","lines":["a"]},{"start":{"row":26,"column":48},"end":{"row":26,"column":49},"action":"insert","lines":["t"]},{"start":{"row":26,"column":49},"end":{"row":26,"column":50},"action":"insert","lines":["e"]}],[{"start":{"row":26,"column":50},"end":{"row":26,"column":51},"action":"insert","lines":[" "],"id":12},{"start":{"row":26,"column":51},"end":{"row":26,"column":52},"action":"insert","lines":["d"]},{"start":{"row":26,"column":52},"end":{"row":26,"column":53},"action":"insert","lines":["o"]},{"start":{"row":26,"column":53},"end":{"row":26,"column":54},"action":"insert","lines":["n"]},{"start":{"row":26,"column":54},"end":{"row":26,"column":55},"action":"insert","lines":["a"]},{"start":{"row":26,"column":55},"end":{"row":26,"column":56},"action":"insert","lines":["t"]},{"start":{"row":26,"column":56},"end":{"row":26,"column":57},"action":"insert","lines":["i"]},{"start":{"row":26,"column":57},"end":{"row":26,"column":58},"action":"insert","lines":["o"]},{"start":{"row":26,"column":58},"end":{"row":26,"column":59},"action":"insert","lines":["n"]}],[{"start":{"row":32,"column":49},"end":{"row":32,"column":50},"action":"insert","lines":[","],"id":13}],[{"start":{"row":32,"column":50},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":33,"column":0},"end":{"row":33,"column":20},"action":"insert","lines":["                    "]},{"start":{"row":33,"column":20},"end":{"row":33,"column":21},"action":"insert","lines":["‘"]},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"insert","lines":["’"]}],[{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"remove","lines":["’"],"id":15},{"start":{"row":33,"column":20},"end":{"row":33,"column":21},"action":"remove","lines":["‘"]}],[{"start":{"row":33,"column":20},"end":{"row":33,"column":22},"action":"insert","lines":["''"],"id":16}],[{"start":{"row":33,"column":21},"end":{"row":33,"column":35},"action":"insert","lines":["S3_BUCKET_NAME"],"id":17}],[{"start":{"row":33,"column":36},"end":{"row":33,"column":37},"action":"insert","lines":[" "],"id":18}],[{"start":{"row":33,"column":36},"end":{"row":33,"column":37},"action":"remove","lines":[" "],"id":19}],[{"start":{"row":33,"column":36},"end":{"row":33,"column":37},"action":"insert","lines":[":"],"id":20}],[{"start":{"row":33,"column":37},"end":{"row":33,"column":38},"action":"insert","lines":[" "],"id":21}],[{"start":{"row":33,"column":38},"end":{"row":33,"column":40},"action":"insert","lines":["''"],"id":22}],[{"start":{"row":33,"column":39},"end":{"row":33,"column":61},"action":"insert","lines":["assignmentlambdabucket"],"id":23}],[{"start":{"row":33,"column":62},"end":{"row":33,"column":63},"action":"insert","lines":[","],"id":24}],[{"start":{"row":33,"column":62},"end":{"row":33,"column":63},"action":"remove","lines":[","],"id":25}],[{"start":{"row":11,"column":29},"end":{"row":11,"column":30},"action":"remove","lines":["e"],"id":26},{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"remove","lines":["d"]},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"remove","lines":["o"]},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"remove","lines":["c"]},{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"remove","lines":["_"]},{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"remove","lines":["s"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"remove","lines":["e"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"remove","lines":["i"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"remove","lines":["r"]},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"remove","lines":["o"]},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"remove","lines":["g"]},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"remove","lines":["e"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"remove","lines":["t"]},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"remove","lines":["a"]},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"remove","lines":["c"]},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"remove","lines":["_"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"remove","lines":["t"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"remove","lines":["e"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"remove","lines":["g"]}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["c"],"id":27},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["r"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["e"]},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":["a"]}],[{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["t"],"id":28},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["e"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":["_"]},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"insert","lines":["d"]}],[{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":["o"],"id":29},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["n"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["a"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"insert","lines":["t"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"insert","lines":["i"]},{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"insert","lines":["o"]},{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"insert","lines":["n"]}],[{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"insert","lines":["_"],"id":30},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"insert","lines":["c"]},{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"insert","lines":["o"]},{"start":{"row":11,"column":29},"end":{"row":11,"column":30},"action":"insert","lines":["d"]},{"start":{"row":11,"column":30},"end":{"row":11,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":33,"column":54},"end":{"row":33,"column":55},"action":"remove","lines":["a"],"id":31},{"start":{"row":33,"column":53},"end":{"row":33,"column":54},"action":"remove","lines":["d"]},{"start":{"row":33,"column":52},"end":{"row":33,"column":53},"action":"remove","lines":["b"]},{"start":{"row":33,"column":51},"end":{"row":33,"column":52},"action":"remove","lines":["m"]},{"start":{"row":33,"column":50},"end":{"row":33,"column":51},"action":"remove","lines":["a"]},{"start":{"row":33,"column":49},"end":{"row":33,"column":50},"action":"remove","lines":["l"]}],[{"start":{"row":33,"column":49},"end":{"row":33,"column":50},"action":"insert","lines":["f"],"id":32},{"start":{"row":33,"column":50},"end":{"row":33,"column":51},"action":"insert","lines":["o"]},{"start":{"row":33,"column":51},"end":{"row":33,"column":52},"action":"insert","lines":["o"]},{"start":{"row":33,"column":52},"end":{"row":33,"column":53},"action":"insert","lines":["d"]},{"start":{"row":33,"column":53},"end":{"row":33,"column":54},"action":"insert","lines":["s"]},{"start":{"row":33,"column":54},"end":{"row":33,"column":55},"action":"insert","lines":["h"]},{"start":{"row":33,"column":55},"end":{"row":33,"column":56},"action":"insert","lines":["a"]},{"start":{"row":33,"column":56},"end":{"row":33,"column":57},"action":"insert","lines":["r"]},{"start":{"row":33,"column":57},"end":{"row":33,"column":58},"action":"insert","lines":["e"]},{"start":{"row":33,"column":58},"end":{"row":33,"column":59},"action":"insert","lines":["h"]}],[{"start":{"row":33,"column":59},"end":{"row":33,"column":60},"action":"insert","lines":["u"],"id":33},{"start":{"row":33,"column":60},"end":{"row":33,"column":61},"action":"insert","lines":["b"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":41},"end":{"row":11,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":562,"mode":"ace/mode/python"}},"timestamp":1707135688468,"hash":"dfb320654327bbe91088940eed4159c51de98e68"}