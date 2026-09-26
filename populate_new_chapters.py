#!/usr/bin/env python3
"""
Populate the new math book chapters (130-142) with comprehensive theorems and proofs.
"""

import requests
from openclaw import OpenClawClient
from pathlib import Path

CHAP_DIR = Path("/home/kentagent/math-book/chapters")

# The new chapters to populate with full content
NEW_CHAPTERS = {
    "chapter_130_motives_theory": {
        "title": "Motive Theory - Complete Theorems and Proofs",
        "topics": ["Grothendieck's Motives", "Pure and Mixed Motives", "Beilinson's Conjecture", 
                  "Voevodsky's Motives", "Hodge Conjecture", "Standard Conjectures", "Deligne's Results"]
    },
    "chapter_131_field_theory": {
        "title": "Field Theory Advanced - Complete Theorems and Proofs",
        "topics": ["Normal Closure and Splitting Fields", "Galois Correspondence", 
                  "Primitive Element Theorem", "Irreducibility Theorems", 
                  "Separability Theory", "Inseparable Extensions", "Artin-Schreier Theory"]
    },
    "chapter_132_ring_theory": {
        "title": "Ring Theory Advanced - Complete Theorems and Proofs",
        "topics": ["Noetherian Rings", "Nakayama's Lemma", "Hilbert Basis Theorem", 
                  "Prime Avoidance", "Chinese Remainder Theorem", "Krull's Theorem", 
                  "Zorn's Lemma", "Commutative Noetherian Structure"]
    },
    "chapter_133_algebraic_topology": {
        "title": "Algebraic Topology - Complete Theorems and Proofs",
        "topics": ["Homotopy Groups", "Hurewicz Theorem", "Whitehead Theorem", 
                  "Universal Coefficient Theorem", "Poincaré Duality", 
                  "Cobordism Theory", "Spectral Sequences", "Serre Spectral Sequence"]
    },
    "chapter_134_homological_algebra": {
        "title": "Homological Algebra - Complete Theorems and Proofs",
        "topics": ["Derived Categories", "Kunneth Formula", "Spectral Sequences", 
                  "Universal Coefficient Theorem", "Tor and Ext", 
                  "Long Exact Sequences", "Abelian Categories", "Homological Dimension"]
    },
    "chapter_135_representation_theory": {
        "title": "Representation Theory - Complete Theorems and Proofs",
        "topics": ["Maschke's Theorem", "Jacobson's Density Theorem", 
                  "Clifford's Theorem", "Brauer's Main Theorems", 
                  "Modular Representation Theory", "Irreducible Characters", 
                  "Weyl's Complete Reducibility", "Cartan-Wielit Theorem"]
    },
    "chapter_136_geometric_rep_theory": {
        "title": "Geometric Representation Theory - Complete Theorems and Proofs",
        "topics": ["Geometric Invariant Theory", "Mumford's Stability", 
                  "Hilbert-Mumford Criterion", "Moduli Spaces", 
                  "Donaldson-Thomas Invariants", "Wall Crossing Theory", 
                  "Geometric Langlands Conjecture"]
    },
    "chapter_137_geometric_faa": {
        "title": "Geometric Functional Analysis - Complete Theorems and Proofs",
        "topics": ["Banach-Steinhaus Theorem", "Uniform Boundedness Principle", 
                  "James' Theorem", "Dvoretzky-Rogers Theorem", 
                  "Krein-Milman Theorem", "Baire Category Theorem", 
                  "Grothendieck's Open Mapping Theorem", "Hahn-Banach Theorem"]
    },
    "chapter_138_arithmetic_geometry": {
        "title": "Arithmetic Geometry - Complete Theorems and Proofs",
        "topics": ["Mordell-Weil Theorem", "Weil Conjectures", 
                  "Lang-Weil Bounds", "Faltings' Theorem", "Hasse-Weil L-functions", 
                  "Tate's Local Class Field Theory", "Kummer's Theory", 
                  "Serre-Tate Theory"]
    },
    "chapter_139_noncommutative_geometry": {
        "title": "Noncommutative Geometry - Complete Theorems and Proofs",
        "topics": ["Spectral Triples", "Connes' Theorems", "Heisenberg Uncertainty", 
                  "Noncommutative Tori", "Dirac Operators", "Quantum Groups", 
                  "Chern Character", "KK-theory"]
    },
    "chapter_140_differential_geometry": {
        "title": "Differential Geometry - Complete Theorems and Proofs",
        "topics": ["Riemannian Metrics", "Levi-Civita Connection", 
                  "Gauss-Bonnet Theorem", "Chern-Weil Theory", 
                  "Holonomy Groups", "Parallel Transport", 
                  "Exotic Spheres", "Ricci Curvature Flows"]
    },
    "chapter_141_lie_groups": {
        "title": "Lie Groups and Algebras - Complete Theorems and Proofs",
        "topics": ["Exponential Map", "Ado's Theorem", "Lie's Third Theorem", 
                  "Cartan's Classification", "Killing Form", 
                  "Invariant Subalgebras", "Symmetric Spaces", 
                  "Iwasawa Decomposition", "Peter-Weyl Theorem"]
    },
    "chapter_142_galois_theory": {
        "title": "Galois Theory - Complete Theorems and Proofs",
        "topics": ["Primitive Element Theorem", "Separability in characteristic p", 
                  "Artin-Schreier Theory", "Inseparable Extensions", 
                  "Solvability of Galois Groups", "Class Field Theory"]
    }
}


def get_api_client():
    """Get OpenClaw API client"""
    try:
        client = OpenClawClient()
        return client
    except Exception as e:
        print(f"Error initializing API client: {e}")
        return None


def generate_mathematical_content(topic, chapter_name):
    """Generate theorem content using OpenClaw API"""
    def generate():
        messages = [
            {
                "role": "system",
                "content": f"You are an expert mathematician. Generate comprehensive theorems and proofs for '{chapter_name}' covering '{topic}'. Output ONLY Markdown with LaTeX math, nothing else. Include: theorem statement, full proof with details, and relevant examples."
            },
            {
                "role": "user",
                "content": f"""Generate complete theorems and proofs for {topic} in {chapter_name}.

Requirements:
1. Provide 3-5 core theorems with full statements
2. Include complete, rigorous proofs for each theorem
3. Use proper LaTeX math notation ($) and display math ($$)
4. Include definitions, lemmas, and corollaries where appropriate
5. Add relevant examples and applications
6. Format as a proper mathematical text suitable for a textbook

Output ONLY the mathematical content, no conversational text."""
            }
        ]
        
        try:
            response = client.chat.completions.create(
                model="qwen3.5:4b",
                messages=messages,
                max_tokens=8000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[ERROR: {str(e)}]"
    
    # Run Python code to call API
    code = f"""
import requests
from openclaw import OpenClawClient

try:
    client = OpenClawClient()
    api_url = client.get_api_url()
except Exception:
    api_url = 'http://localhost:11434/api'

messages = [
    {{
        "role": "system",
        "content": f"You are an expert mathematician. Generate comprehensive theorems and proofs for '{{chapter_name}}' covering '{{topic}}'. Output ONLY Markdown with LaTeX math, nothing else. Include: theorem statement, full proof with details, and relevant examples."
    }},
    {{
        "role": "user",
        "content": f"Generate complete theorems and proofs for {topic} in {chapter_name}. Include 3-5 core theorems with full statements, complete rigorous proofs, proper LaTeX math notation, definitions, lemmas, corollaries, examples and applications. Format as a proper mathematical textbook text."
    }}
]

try:
    response = client.chat.completions.create(
        model="qwen3.5:4b",
        messages=messages,
        max_tokens=8000
    )
    return response.choices[0].message.content
except Exception as e:
    return f"[ERROR: {str(e)}]"
"""
    
    # Execute the code
    result = subprocess.run(['python3', '-c', code], capture_output=True, text=True)
    return result.stdout


def write_chapter(filepath, title, content):
    """Write chapter content to file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"This chapter provides comprehensive treatment of advanced mathematical topics with complete theorems and proofs.\n\n")
        f.write(content)


def main():
    client = get_api_client()
    if client is None:
        print("Could not initialize API client. Continuing with placeholder content.")
    
    print("=" * 60)
    print("Populating new math book chapters (130-142)...")
    print("=" * 60)
    
    for filepath, chapter_data in NEW_CHAPTERS.items():
        print(f"\nProcessing {chapter_data['title']}...")
        topic = ", ".join(chapter_data['topics'][:2])
        print(f"  Topics: {topic}")
        
        content = generate_mathematical_content(topic, chapter_data['title'])
        
        write_chapter(CHAP_DIR / filepath, chapter_data['title'], content)
        print(f"  Written: {filepath}")
    
    print("\n" + "=" * 60)
    print(f"Completed: {len(NEW_CHAPTERS)} new chapters written")
    print("=" * 60)


if __name__ == '__main__':
    main()
