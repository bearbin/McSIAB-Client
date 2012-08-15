def ask_question(questionText, answerTypeAllowed = 0, allowedAnswers = None, acceptedAnswerText = "Answer accepted.", typeErrorText = "Your answer was of the wrong type.", badAnswerText = "Your answer was not one of the allowed answers.", genericErrorText = "An error occured."):
	
	# answerTypeAllowed : What type of answers to allow. Defaults to any type.
	# questionText      : What question the user is asked. This is required.
	# allowedAnswers    : What values are allowed. Defaults to any.
	# typeErrorText     : The text printed if the input was of the wrong type.
	# badAnswerText     : What is printed when the answer is not on eof the specified allowed ones.
	# genericErrorText  : What happens when an error occurs.
	#
	# answerTypeAllowed Values:
	# 0 : Any type.
	# 1 : String
	# 2 : Integer
	# 3 : Float
	# 4 : Boolean 
	
	if answerTypeAllowed not in range(5):
		print "There was an error with internal coding :("
		return
	while 1:
		userInput = raw_input(questionText)
		if allowedAnswers is not None:		
			if answerTypeAllowed == 0:
				if userInput in allowedAnswers:
					print acceptedAnswerText
					return userInput
				else:
					print badAnswerText
					raw_input("Press enter to continue. ")
					continue
			elif answerTypeAllowed == 1:
				if str(userInput) in allowedAnswers:
					print acceptedAnswerText
					return str(userInput)
				else:
					print badAnswerText
					raw_input("Press enter to continue. ")
					continue
			elif answerTypeAllowed == 2:
				try:
					int(userInput)
				except ValueError:
					print typeErrorText
					raw_input("Press enter to continue. ")
					continue
				if int(userInput) in allowedAnswers:
					print acceptedAnswerText
					return int(userInput)
				else:
					print badAnswerText
					raw_input("Press enter to continue. ")
					continue
			elif answerTypeAllowed == 3:
				try:
					float(userInput)
				except ValueError:
					print typeErrorText
					raw_input("Press enter to continue. ")
					continue
				if float(userInput) in allowedAnswers:
					print acceptedAnswerText
					return float(userInput)
				else:
					print badAnswerText
					raw_input("Press enter to continue. ")
					continue
			elif answerTypeAllowed == 4:
				if str(userInput).lower() in ['y', 'n', 'yes', 'no', '0', '1', 'true', 'false']:
					if str(userInput).lower() in ['y', 'yes', '1', 'true']:
						print acceptedAnswerText
						return True
					else:
						print acceptedAnswerText
						return False
				else:
					print typeErrorText
					raw_input("Press enter to continue. ")
					continue
			else:
				print genericErrorText
				raw_input("Press enter to continue. ")
				continue
		elif allowedAnswers is None:
			if answerTypeAllowed == 0:
				print acceptedAnswerText
				return userInput
			elif answerTypeAllowed == 1:
				print acceptedAnswerText
				return str(userInput)
			elif answerTypeAllowed == 2:
				try:
					int(userInput)
				except ValueError:
					print typeErrorText
					raw_input("Press enter to continue. ")
					continue
				print acceptedAnswerText
				return int(userInput)
			elif answerTypeAllowed == 3:
				try:
					float(userInput)
				except ValueError:
					print typeErrorText
					raw_input("Press enter to continue. ")
					continue
				print acceptedAnswerText
				return float(userInput)
			elif answerTypeAllowed == 4:
				if str(userInput).lower() in ['y', 'n', 'yes', 'no', '0', '1', 'true', 'false']:
					if str(userInput).lower() in ['y', 'yes', '1', 'true']:
						print acceptedAnswerText
						return True
					else:
						print acceptedAnswerText
						return False
				else:
					print typeErrorText
					raw_input("Press enter to continue. ")
					continue
			else:
				print genericErrorText
				raw_input("Press enter to continue. ")
				continue
		else:
			print genericErrorText
			raw_input("Press enter to continue. ")
			continue
