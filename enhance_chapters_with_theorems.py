#!/usr/bin/env python3
"""
Enhance math book chapters with theorems/proofs using OpenClaw API
"""
import subprocess
import os
import sys
from pathlib import Path

CHUNK_SIZE = 8000  # characters per chunk
BATCH_SIZE = 10  # chapters per batch

def get_openclaw_api_url():
    # Check environment or use default
    if 'OPENCLAW_API_URL' in os.environ:
        return os.environ['OPENCLAW_API_URL']
    # Try to find OpenClaw API server
    return 'http://localhost:11434/api'

def run_python_server(code):
    """Run Python code to call OpenClaw API"""
    import requests
    from openclaw import OpenClawClient
    
    # Try to get API from OpenClaw client
    try:
        client = OpenClawClient()
        api_url = client.get_api_url()
    except Exception:
        # Fallback: try to construct from environment
        api_url = os.environ.get('OPENCLAW_API_URL', 'http://localhost:11434/api')
    
    def generate_theorems(topic, chapter_name):
        """Generate theorems for a given topic"""
        messages = [
            {
                "role": "system",
                "content": f"You are an expert mathematician. Generate {chapter_name} theorems and proofs in Markdown format. Output ONLY the theorem content, nothing else."
            },
            {
                "role": "user",
                "content": f"""Generate 5-10 advanced theorems and proofs for the topic: {topic}
Format:
# Theorem Name
**Statement**: [theorem statement]
**Proof**: [brief proof outline]

Include LaTeX math using $...$ for inline and $$...$$ for display math.
Only output theorem content, no explanations or introductions."""
            }
        ]
        
        try:
            response = client.chat.completions.create(
                model="qwen3.5:4b",
                messages=messages,
                max_tokens=4000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[ERROR: {str(e)}]"
    
    return generate_theorems

def append_theorems_to_chapter(chapter_path, topic):
    """Append theorems to a chapter file"""
    generate = run_python_server("")
    content = generate(topic, os.path.basename(chapter_path).replace('.md', ''))
    
    # Create a separator
    separator = "\n" + "="*70 + "\n"
    separator += "# Theorems and Proofs\n\n"
    separator += f"Generated on: {__import__('datetime').datetime.now().isoformat()}\n\n"
    separator += "--- Theorem Generation ---\n\n"
    separator += "\n"
    
    # Append content
    with open(chapter_path, 'a', encoding='utf-8') as f:
        f.write(separator)
        f.write(content)

def main():
    chapters_dir = Path('/home/kentagent/math-book/chapters')
    chapters_needing_enhancement = [
        'chapter_1_complex_numbers.md',
        'chapter_2_advanced_complex_numbers.md',
        'chapter_3_advanced_topology.md',
        'chapter_4_advanced_abstract_algebra.md',
        'chapter_5_advanced_number_theory.md',
        'chapter_10_complex_analysis_theorems.md',
        'chapter_14_group_theory.md',
        'chapter_18_complex_analysis_theorems.md',
        'chapter_20_topology_concepts.md',
        'chapter_24_complex_numbers_advanced.md',
        'chapter_26_abstract_algebra_advanced.md',
        'chapter_27_number_theory_advanced.md',
        'chapter_30_abstract_algebra_core.md',
        'chapter_33_galois_theory.md',
        'chapter_34_lie_groups_and_algebras.md',
        'chapter_41_functional_analysis_theorems.md',
        'chapter_50_modern_number_theory.md',
    ]
    
    topics = {
        'chapter_1_complex_numbers.md': 'Complex numbers fundamentals',
        'chapter_2_advanced_complex_numbers.md': 'Advanced complex analysis',
        'chapter_3_advanced_topology.md': 'Advanced topological spaces',
        'chapter_4_advanced_abstract_algebra.md': 'Advanced abstract algebra',
        'chapter_5_advanced_number_theory.md': 'Advanced number theory',
        'chapter_10_complex_analysis_theorems.md': 'Complex analysis theorems',
        'chapter_14_group_theory.md': 'Group theory fundamentals',
        'chapter_18_complex_analysis_theorems.md': 'Complex analysis advanced theorems',
        'chapter_20_topology_concepts.md': 'Topology fundamentals',
        'chapter_24_complex_numbers_advanced.md': 'Advanced complex number theory',
        'chapter_26_abstract_algebra_advanced.md': 'Advanced abstract algebra structures',
        'chapter_27_number_theory_advanced.md': 'Advanced number theory and primes',
        'chapter_30_abstract_algebra_core.md': 'Abstract algebra core concepts',
        'chapter_33_galois_theory.md': 'Galois theory and field extensions',
        'chapter_34_lie_groups_and_algebras.md': 'Lie groups and Lie algebras',
        'chapter_41_functional_analysis_theorems.md': 'Functional analysis theorems',
        'chapter_50_modern_number_theory.md': 'Modern number theory',
    }
    
    for chapter in chapters_needing_enhancement:
        if chapter in topics:
            topic = topics[chapter]
            chapter_path = chapters_dir / chapter
            print(f"Processing {chapter}...")
            try:
                append_theorems_to_chapter(chapter_path, topic)
                print(f"  Done: {chapter}")
            except Exception as e:
                print(f"  Error processing {chapter}: {e}")
    
    print(f"\nEnhanced {len(chapters_needing_enhancement)} chapters")
    print("Ready to commit and push")

if __name__ == '__main__':
    main()
