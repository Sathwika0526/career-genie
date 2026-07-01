from app.services.resume_parser import parse_resume
import json

result = parse_resume("data/resumes/Sathwika_Rupireddy_Topgolf_DataEngineerII.pdf")

print(json.dumps(result, indent=2))