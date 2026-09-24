def score_prompt_complexity(prompts):
    result = []

    for prompt in prompts:
        complexity = len(set(prompt["tags"]))

        result.append({
            "text": prompt["text"],
            "complexity": complexity
        })

    result.sort(key=lambda x: x["complexity"], reverse=True)

    return result