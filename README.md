# Experimental results for [Boost Bloom Library](https://github.com/boostorg/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for several configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-march=native`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.42</td>
    <td align="right">6.89</td>
    <td align="right">5.52</td>
    <td align="right">15.86</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.12</td>
    <td align="right">24.12</td>
    <td align="right">22.03</td>
    <td align="right">24.68</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.02</td>
    <td align="right">19.60</td>
    <td align="right">19.37</td>
    <td align="right">19.48</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.46</td>
    <td align="right">19.60</td>
    <td align="right">19.44</td>
    <td align="right">19.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.55</td>
    <td align="right">29.27</td>
    <td align="right">22.99</td>
    <td align="right">28.30</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.39</td>
    <td align="right">21.10</td>
    <td align="right">20.95</td>
    <td align="right">21.03</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.00</td>
    <td align="right">20.87</td>
    <td align="right">20.75</td>
    <td align="right">20.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.37</td>
    <td align="right">32.76</td>
    <td align="right">22.32</td>
    <td align="right">31.29</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.02</td>
    <td align="right">21.90</td>
    <td align="right">21.78</td>
    <td align="right">21.85</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.56</td>
    <td align="right">21.93</td>
    <td align="right">21.82</td>
    <td align="right">21.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.34</td>
    <td align="right">43.14</td>
    <td align="right">22.60</td>
    <td align="right">36.24</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">22.34</td>
    <td align="right">22.24</td>
    <td align="right">22.29</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.82</td>
    <td align="right">22.45</td>
    <td align="right">22.38</td>
    <td align="right">22.42</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.96</td>
    <td align="right">28.30</td>
    <td align="right">28.29</td>
    <td align="right">28.28</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.00</td>
    <td align="right">19.47</td>
    <td align="right">19.27</td>
    <td align="right">19.35</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.51</td>
    <td align="right">19.65</td>
    <td align="right">19.44</td>
    <td align="right">19.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.55</td>
    <td align="right">32.72</td>
    <td align="right">32.84</td>
    <td align="right">32.81</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.40</td>
    <td align="right">21.14</td>
    <td align="right">20.99</td>
    <td align="right">21.04</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.03</td>
    <td align="right">21.17</td>
    <td align="right">21.04</td>
    <td align="right">21.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.45</td>
    <td align="right">35.52</td>
    <td align="right">35.64</td>
    <td align="right">35.64</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.03</td>
    <td align="right">21.91</td>
    <td align="right">21.78</td>
    <td align="right">21.86</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.56</td>
    <td align="right">21.98</td>
    <td align="right">21.88</td>
    <td align="right">21.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.24</td>
    <td align="right">40.01</td>
    <td align="right">39.87</td>
    <td align="right">40.00</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.40</td>
    <td align="right">22.43</td>
    <td align="right">22.33</td>
    <td align="right">22.39</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.82</td>
    <td align="right">22.49</td>
    <td align="right">22.41</td>
    <td align="right">22.43</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">9.98</td>
    <td align="right">23.20</td>
    <td align="right">21.57</td>
    <td align="right">24.12</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.98</td>
    <td align="right">19.58</td>
    <td align="right">19.34</td>
    <td align="right">19.45</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.90</td>
    <td align="right">19.59</td>
    <td align="right">19.38</td>
    <td align="right">19.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">14.89</td>
    <td align="right">27.48</td>
    <td align="right">22.38</td>
    <td align="right">27.22</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.35</td>
    <td align="right">21.14</td>
    <td align="right">20.99</td>
    <td align="right">21.05</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.07</td>
    <td align="right">21.49</td>
    <td align="right">21.32</td>
    <td align="right">21.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">17.62</td>
    <td align="right">31.10</td>
    <td align="right">21.92</td>
    <td align="right">29.85</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">21.93</td>
    <td align="right">21.82</td>
    <td align="right">21.89</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.51</td>
    <td align="right">21.89</td>
    <td align="right">21.77</td>
    <td align="right">21.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">21.83</td>
    <td align="right">35.92</td>
    <td align="right">22.10</td>
    <td align="right">32.36</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.37</td>
    <td align="right">22.43</td>
    <td align="right">22.32</td>
    <td align="right">22.35</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.94</td>
    <td align="right">22.34</td>
    <td align="right">22.26</td>
    <td align="right">22.30</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">9.96</td>
    <td align="right">28.87</td>
    <td align="right">28.86</td>
    <td align="right">28.85</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.99</td>
    <td align="right">19.62</td>
    <td align="right">19.40</td>
    <td align="right">19.47</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.43</td>
    <td align="right">19.63</td>
    <td align="right">19.37</td>
    <td align="right">19.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">14.74</td>
    <td align="right">32.88</td>
    <td align="right">32.94</td>
    <td align="right">32.91</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.34</td>
    <td align="right">21.18</td>
    <td align="right">21.04</td>
    <td align="right">21.11</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.07</td>
    <td align="right">21.45</td>
    <td align="right">21.31</td>
    <td align="right">21.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">17.40</td>
    <td align="right">36.22</td>
    <td align="right">36.16</td>
    <td align="right">36.25</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">21.95</td>
    <td align="right">21.82</td>
    <td align="right">21.88</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.50</td>
    <td align="right">21.86</td>
    <td align="right">21.75</td>
    <td align="right">21.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">21.60</td>
    <td align="right">42.02</td>
    <td align="right">42.02</td>
    <td align="right">42.05</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.38</td>
    <td align="right">22.40</td>
    <td align="right">22.30</td>
    <td align="right">22.35</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.95</td>
    <td align="right">22.36</td>
    <td align="right">22.27</td>
    <td align="right">22.29</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.02</td>
    <td align="right">21.20</td>
    <td align="right">15.86</td>
    <td align="right">23.04</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.55</td>
    <td align="right">22.82</td>
    <td align="right">16.11</td>
    <td align="right">24.35</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.26</td>
    <td align="right">23.36</td>
    <td align="right">23.21</td>
    <td align="right">23.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.87</td>
    <td align="right">22.46</td>
    <td align="right">16.84</td>
    <td align="right">24.67</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.03</td>
    <td align="right">25.99</td>
    <td align="right">17.77</td>
    <td align="right">27.17</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.69</td>
    <td align="right">23.20</td>
    <td align="right">22.71</td>
    <td align="right">22.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.11</td>
    <td align="right">24.74</td>
    <td align="right">17.71</td>
    <td align="right">26.64</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.07</td>
    <td align="right">27.80</td>
    <td align="right">18.70</td>
    <td align="right">28.06</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.78</td>
    <td align="right">28.58</td>
    <td align="right">4.80</td>
    <td align="right">25.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.39</td>
    <td align="right">25.92</td>
    <td align="right">16.95</td>
    <td align="right">27.27</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.66</td>
    <td align="right">28.39</td>
    <td align="right">19.29</td>
    <td align="right">28.68</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.83</td>
    <td align="right">29.06</td>
    <td align="right">4.79</td>
    <td align="right">26.31</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.03</td>
    <td align="right">21.91</td>
    <td align="right">21.71</td>
    <td align="right">21.80</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.51</td>
    <td align="right">23.80</td>
    <td align="right">23.63</td>
    <td align="right">23.68</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.26</td>
    <td align="right">23.37</td>
    <td align="right">23.18</td>
    <td align="right">23.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.85</td>
    <td align="right">30.40</td>
    <td align="right">30.32</td>
    <td align="right">30.36</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.02</td>
    <td align="right">32.28</td>
    <td align="right">32.17</td>
    <td align="right">32.23</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.69</td>
    <td align="right">23.20</td>
    <td align="right">22.74</td>
    <td align="right">22.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.14</td>
    <td align="right">26.10</td>
    <td align="right">26.08</td>
    <td align="right">26.08</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.08</td>
    <td align="right">29.11</td>
    <td align="right">29.10</td>
    <td align="right">29.10</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.76</td>
    <td align="right">27.53</td>
    <td align="right">27.43</td>
    <td align="right">27.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.26</td>
    <td align="right">27.36</td>
    <td align="right">27.27</td>
    <td align="right">27.28</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.68</td>
    <td align="right">30.44</td>
    <td align="right">30.35</td>
    <td align="right">30.34</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.82</td>
    <td align="right">27.90</td>
    <td align="right">27.84</td>
    <td align="right">27.87</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">4.68</td>
    <td align="right">21.38</td>
    <td align="right">16.21</td>
    <td align="right">23.16</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.45</td>
    <td align="right">22.83</td>
    <td align="right">16.13</td>
    <td align="right">24.31</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.94</td>
    <td align="right">23.23</td>
    <td align="right">23.04</td>
    <td align="right">23.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.09</td>
    <td align="right">22.48</td>
    <td align="right">16.65</td>
    <td align="right">24.51</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">6.82</td>
    <td align="right">26.03</td>
    <td align="right">17.56</td>
    <td align="right">26.82</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.56</td>
    <td align="right">23.10</td>
    <td align="right">22.96</td>
    <td align="right">23.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">8.55</td>
    <td align="right">24.45</td>
    <td align="right">17.92</td>
    <td align="right">26.57</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">18.72</td>
    <td align="right">28.11</td>
    <td align="right">19.04</td>
    <td align="right">29.33</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.28</td>
    <td align="right">28.54</td>
    <td align="right">4.58</td>
    <td align="right">26.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.08</td>
    <td align="right">26.34</td>
    <td align="right">16.95</td>
    <td align="right">27.44</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.53</td>
    <td align="right">28.63</td>
    <td align="right">18.97</td>
    <td align="right">28.55</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.30</td>
    <td align="right">29.03</td>
    <td align="right">4.56</td>
    <td align="right">26.38</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">4.67</td>
    <td align="right">22.07</td>
    <td align="right">21.84</td>
    <td align="right">21.91</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.48</td>
    <td align="right">23.74</td>
    <td align="right">23.60</td>
    <td align="right">23.65</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.97</td>
    <td align="right">23.22</td>
    <td align="right">23.01</td>
    <td align="right">23.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.11</td>
    <td align="right">30.41</td>
    <td align="right">30.29</td>
    <td align="right">30.34</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">6.83</td>
    <td align="right">32.24</td>
    <td align="right">32.14</td>
    <td align="right">32.21</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.57</td>
    <td align="right">23.13</td>
    <td align="right">22.94</td>
    <td align="right">23.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">8.57</td>
    <td align="right">26.26</td>
    <td align="right">26.14</td>
    <td align="right">26.15</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.13</td>
    <td align="right">29.17</td>
    <td align="right">28.99</td>
    <td align="right">29.03</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.26</td>
    <td align="right">27.51</td>
    <td align="right">27.43</td>
    <td align="right">27.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.09</td>
    <td align="right">27.04</td>
    <td align="right">26.98</td>
    <td align="right">27.03</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.52</td>
    <td align="right">30.14</td>
    <td align="right">30.15</td>
    <td align="right">30.12</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.29</td>
    <td align="right">27.92</td>
    <td align="right">27.86</td>
    <td align="right">27.90</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.19</td>
    <td align="right">22.52</td>
    <td align="right">22.36</td>
    <td align="right">22.42</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.62</td>
    <td align="right">25.01</td>
    <td align="right">24.83</td>
    <td align="right">24.92</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.79</td>
    <td align="right">24.43</td>
    <td align="right">24.24</td>
    <td align="right">24.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.32</td>
    <td align="right">24.06</td>
    <td align="right">23.95</td>
    <td align="right">24.01</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.47</td>
    <td align="right">24.02</td>
    <td align="right">23.82</td>
    <td align="right">23.89</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.81</td>
    <td align="right">25.93</td>
    <td align="right">25.82</td>
    <td align="right">25.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.53</td>
    <td align="right">27.65</td>
    <td align="right">4.57</td>
    <td align="right">25.33</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.61</td>
    <td align="right">28.47</td>
    <td align="right">6.86</td>
    <td align="right">27.92</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.80</td>
    <td align="right">27.68</td>
    <td align="right">6.78</td>
    <td align="right">27.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.60</td>
    <td align="right">28.12</td>
    <td align="right">4.55</td>
    <td align="right">25.78</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.44</td>
    <td align="right">30.69</td>
    <td align="right">6.88</td>
    <td align="right">29.23</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.66</td>
    <td align="right">29.83</td>
    <td align="right">6.88</td>
    <td align="right">28.87</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.19</td>
    <td align="right">22.53</td>
    <td align="right">22.35</td>
    <td align="right">22.43</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.62</td>
    <td align="right">25.02</td>
    <td align="right">24.86</td>
    <td align="right">24.91</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.78</td>
    <td align="right">24.42</td>
    <td align="right">24.29</td>
    <td align="right">24.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.33</td>
    <td align="right">24.08</td>
    <td align="right">23.96</td>
    <td align="right">24.02</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.50</td>
    <td align="right">23.98</td>
    <td align="right">23.80</td>
    <td align="right">23.89</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.81</td>
    <td align="right">25.98</td>
    <td align="right">25.82</td>
    <td align="right">25.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.53</td>
    <td align="right">26.67</td>
    <td align="right">26.58</td>
    <td align="right">26.63</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.60</td>
    <td align="right">28.29</td>
    <td align="right">28.22</td>
    <td align="right">28.27</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.76</td>
    <td align="right">27.77</td>
    <td align="right">27.72</td>
    <td align="right">27.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.61</td>
    <td align="right">27.08</td>
    <td align="right">27.00</td>
    <td align="right">27.05</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.34</td>
    <td align="right">29.08</td>
    <td align="right">28.98</td>
    <td align="right">28.97</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.63</td>
    <td align="right">28.23</td>
    <td align="right">28.23</td>
    <td align="right">28.22</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.92</td>
    <td align="right">22.27</td>
    <td align="right">22.10</td>
    <td align="right">22.19</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.42</td>
    <td align="right">25.05</td>
    <td align="right">24.89</td>
    <td align="right">24.95</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.63</td>
    <td align="right">24.44</td>
    <td align="right">24.20</td>
    <td align="right">24.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.02</td>
    <td align="right">23.80</td>
    <td align="right">23.66</td>
    <td align="right">23.72</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.43</td>
    <td align="right">23.99</td>
    <td align="right">23.82</td>
    <td align="right">23.91</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.57</td>
    <td align="right">25.91</td>
    <td align="right">25.77</td>
    <td align="right">25.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.41</td>
    <td align="right">27.67</td>
    <td align="right">4.35</td>
    <td align="right">25.46</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.32</td>
    <td align="right">28.42</td>
    <td align="right">6.61</td>
    <td align="right">27.78</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.42</td>
    <td align="right">27.71</td>
    <td align="right">6.38</td>
    <td align="right">27.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.49</td>
    <td align="right">28.12</td>
    <td align="right">4.36</td>
    <td align="right">25.56</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.92</td>
    <td align="right">30.98</td>
    <td align="right">6.48</td>
    <td align="right">29.16</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.73</td>
    <td align="right">30.20</td>
    <td align="right">6.50</td>
    <td align="right">28.78</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.90</td>
    <td align="right">22.35</td>
    <td align="right">22.12</td>
    <td align="right">22.19</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.46</td>
    <td align="right">25.10</td>
    <td align="right">24.86</td>
    <td align="right">24.95</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.64</td>
    <td align="right">24.44</td>
    <td align="right">24.25</td>
    <td align="right">24.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.02</td>
    <td align="right">23.84</td>
    <td align="right">23.64</td>
    <td align="right">23.74</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.42</td>
    <td align="right">24.02</td>
    <td align="right">23.80</td>
    <td align="right">23.89</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.58</td>
    <td align="right">25.88</td>
    <td align="right">25.76</td>
    <td align="right">25.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.44</td>
    <td align="right">26.71</td>
    <td align="right">26.61</td>
    <td align="right">26.66</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.32</td>
    <td align="right">28.21</td>
    <td align="right">28.16</td>
    <td align="right">28.19</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.44</td>
    <td align="right">27.64</td>
    <td align="right">27.55</td>
    <td align="right">27.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.49</td>
    <td align="right">27.08</td>
    <td align="right">26.98</td>
    <td align="right">27.03</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.95</td>
    <td align="right">29.00</td>
    <td align="right">28.90</td>
    <td align="right">28.90</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.72</td>
    <td align="right">28.20</td>
    <td align="right">28.22</td>
    <td align="right">28.21</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.43</td>
    <td align="right">20.50</td>
    <td align="right">16.54</td>
    <td align="right">22.95</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.76</td>
    <td align="right">24.38</td>
    <td align="right">21.04</td>
    <td align="right">26.78</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.34</td>
    <td align="right">23.65</td>
    <td align="right">21.76</td>
    <td align="right">25.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.79</td>
    <td align="right">22.82</td>
    <td align="right">15.56</td>
    <td align="right">24.36</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.53</td>
    <td align="right">26.44</td>
    <td align="right">17.80</td>
    <td align="right">28.67</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.11</td>
    <td align="right">26.94</td>
    <td align="right">22.34</td>
    <td align="right">27.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.65</td>
    <td align="right">25.18</td>
    <td align="right">15.74</td>
    <td align="right">27.07</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.94</td>
    <td align="right">27.57</td>
    <td align="right">18.67</td>
    <td align="right">29.77</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.30</td>
    <td align="right">29.39</td>
    <td align="right">20.47</td>
    <td align="right">29.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.86</td>
    <td align="right">25.51</td>
    <td align="right">16.42</td>
    <td align="right">27.49</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.60</td>
    <td align="right">28.01</td>
    <td align="right">18.39</td>
    <td align="right">29.95</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.58</td>
    <td align="right">32.69</td>
    <td align="right">23.15</td>
    <td align="right">31.17</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.41</td>
    <td align="right">20.69</td>
    <td align="right">20.51</td>
    <td align="right">20.58</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.77</td>
    <td align="right">25.57</td>
    <td align="right">25.39</td>
    <td align="right">25.47</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.33</td>
    <td align="right">26.77</td>
    <td align="right">26.80</td>
    <td align="right">26.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.77</td>
    <td align="right">23.36</td>
    <td align="right">23.17</td>
    <td align="right">23.24</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.54</td>
    <td align="right">28.03</td>
    <td align="right">27.90</td>
    <td align="right">27.96</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.05</td>
    <td align="right">29.42</td>
    <td align="right">29.02</td>
    <td align="right">29.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.64</td>
    <td align="right">24.69</td>
    <td align="right">24.57</td>
    <td align="right">24.63</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.95</td>
    <td align="right">29.44</td>
    <td align="right">29.31</td>
    <td align="right">29.37</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.17</td>
    <td align="right">30.92</td>
    <td align="right">31.21</td>
    <td align="right">31.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.85</td>
    <td align="right">26.10</td>
    <td align="right">26.00</td>
    <td align="right">26.04</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.59</td>
    <td align="right">30.38</td>
    <td align="right">30.30</td>
    <td align="right">30.35</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.66</td>
    <td align="right">34.52</td>
    <td align="right">34.45</td>
    <td align="right">34.54</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.40</td>
    <td align="right">20.80</td>
    <td align="right">16.39</td>
    <td align="right">23.46</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.22</td>
    <td align="right">24.37</td>
    <td align="right">20.81</td>
    <td align="right">26.75</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.23</td>
    <td align="right">24.10</td>
    <td align="right">21.68</td>
    <td align="right">24.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.11</td>
    <td align="right">23.27</td>
    <td align="right">15.77</td>
    <td align="right">24.99</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.60</td>
    <td align="right">26.75</td>
    <td align="right">17.39</td>
    <td align="right">28.46</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.76</td>
    <td align="right">27.12</td>
    <td align="right">21.47</td>
    <td align="right">27.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.10</td>
    <td align="right">25.54</td>
    <td align="right">15.52</td>
    <td align="right">26.91</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.34</td>
    <td align="right">27.68</td>
    <td align="right">18.63</td>
    <td align="right">29.64</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.04</td>
    <td align="right">29.06</td>
    <td align="right">19.62</td>
    <td align="right">29.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.25</td>
    <td align="right">25.49</td>
    <td align="right">16.35</td>
    <td align="right">27.73</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.59</td>
    <td align="right">28.32</td>
    <td align="right">18.03</td>
    <td align="right">30.09</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.47</td>
    <td align="right">33.22</td>
    <td align="right">19.79</td>
    <td align="right">31.50</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.40</td>
    <td align="right">21.18</td>
    <td align="right">20.96</td>
    <td align="right">21.06</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.26</td>
    <td align="right">25.60</td>
    <td align="right">25.45</td>
    <td align="right">25.51</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.06</td>
    <td align="right">26.10</td>
    <td align="right">26.73</td>
    <td align="right">26.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.09</td>
    <td align="right">23.84</td>
    <td align="right">23.67</td>
    <td align="right">23.77</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.64</td>
    <td align="right">28.10</td>
    <td align="right">27.95</td>
    <td align="right">28.00</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.81</td>
    <td align="right">30.00</td>
    <td align="right">29.78</td>
    <td align="right">30.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.08</td>
    <td align="right">25.03</td>
    <td align="right">24.91</td>
    <td align="right">24.96</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.34</td>
    <td align="right">29.23</td>
    <td align="right">29.15</td>
    <td align="right">29.20</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.09</td>
    <td align="right">31.33</td>
    <td align="right">31.39</td>
    <td align="right">31.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.26</td>
    <td align="right">26.55</td>
    <td align="right">26.45</td>
    <td align="right">26.50</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.59</td>
    <td align="right">30.36</td>
    <td align="right">30.27</td>
    <td align="right">30.32</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.12</td>
    <td align="right">34.97</td>
    <td align="right">34.90</td>
    <td align="right">34.98</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">57.98</td>
    <td align="right">29.91</td>
    <td align="right">17.48</td>
    <td align="right">43.15</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.65</td>
    <td align="right">32.02</td>
    <td align="right">25.88</td>
    <td align="right">31.85</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.56</td>
    <td align="right">26.54</td>
    <td align="right">26.17</td>
    <td align="right">26.37</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.76</td>
    <td align="right">26.59</td>
    <td align="right">26.06</td>
    <td align="right">26.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">47.71</td>
    <td align="right">69.41</td>
    <td align="right">31.93</td>
    <td align="right">52.60</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.09</td>
    <td align="right">38.54</td>
    <td align="right">36.33</td>
    <td align="right">37.37</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.90</td>
    <td align="right">36.56</td>
    <td align="right">34.24</td>
    <td align="right">35.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">84.99</td>
    <td align="right">119.77</td>
    <td align="right">39.86</td>
    <td align="right">82.72</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.70</td>
    <td align="right">54.12</td>
    <td align="right">51.27</td>
    <td align="right">52.60</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.81</td>
    <td align="right">54.04</td>
    <td align="right">51.20</td>
    <td align="right">52.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">123.93</td>
    <td align="right">166.52</td>
    <td align="right">46.69</td>
    <td align="right">111.86</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.91</td>
    <td align="right">68.13</td>
    <td align="right">65.68</td>
    <td align="right">66.97</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.78</td>
    <td align="right">69.61</td>
    <td align="right">67.22</td>
    <td align="right">68.45</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">17.03</td>
    <td align="right">40.38</td>
    <td align="right">40.14</td>
    <td align="right">40.24</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">6.08</td>
    <td align="right">27.44</td>
    <td align="right">27.06</td>
    <td align="right">27.29</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.89</td>
    <td align="right">26.77</td>
    <td align="right">26.31</td>
    <td align="right">26.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">49.76</td>
    <td align="right">88.86</td>
    <td align="right">87.40</td>
    <td align="right">88.13</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.94</td>
    <td align="right">37.96</td>
    <td align="right">35.67</td>
    <td align="right">36.99</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.33</td>
    <td align="right">36.46</td>
    <td align="right">34.38</td>
    <td align="right">35.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">84.86</td>
    <td align="right">142.92</td>
    <td align="right">141.94</td>
    <td align="right">142.55</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.41</td>
    <td align="right">54.50</td>
    <td align="right">51.71</td>
    <td align="right">53.05</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">19.16</td>
    <td align="right">55.90</td>
    <td align="right">53.05</td>
    <td align="right">54.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">122.91</td>
    <td align="right">173.75</td>
    <td align="right">173.26</td>
    <td align="right">173.56</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.60</td>
    <td align="right">68.03</td>
    <td align="right">65.73</td>
    <td align="right">67.11</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.86</td>
    <td align="right">69.71</td>
    <td align="right">67.30</td>
    <td align="right">68.69</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.54</td>
    <td align="right">31.81</td>
    <td align="right">25.62</td>
    <td align="right">31.65</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.54</td>
    <td align="right">26.56</td>
    <td align="right">26.12</td>
    <td align="right">26.31</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.16</td>
    <td align="right">27.09</td>
    <td align="right">26.58</td>
    <td align="right">26.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">44.92</td>
    <td align="right">66.13</td>
    <td align="right">31.16</td>
    <td align="right">50.88</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.87</td>
    <td align="right">38.29</td>
    <td align="right">36.14</td>
    <td align="right">37.11</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.91</td>
    <td align="right">38.46</td>
    <td align="right">36.19</td>
    <td align="right">37.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">78.37</td>
    <td align="right">114.23</td>
    <td align="right">38.53</td>
    <td align="right">78.32</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.89</td>
    <td align="right">54.13</td>
    <td align="right">51.26</td>
    <td align="right">52.81</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.65</td>
    <td align="right">55.03</td>
    <td align="right">52.00</td>
    <td align="right">53.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">115.32</td>
    <td align="right">154.92</td>
    <td align="right">45.85</td>
    <td align="right">105.29</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.70</td>
    <td align="right">67.83</td>
    <td align="right">65.43</td>
    <td align="right">66.71</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">25.30</td>
    <td align="right">69.74</td>
    <td align="right">67.25</td>
    <td align="right">68.67</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.34</td>
    <td align="right">38.87</td>
    <td align="right">38.77</td>
    <td align="right">38.83</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.22</td>
    <td align="right">26.08</td>
    <td align="right">25.62</td>
    <td align="right">25.86</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.88</td>
    <td align="right">26.42</td>
    <td align="right">26.00</td>
    <td align="right">26.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">46.36</td>
    <td align="right">89.46</td>
    <td align="right">88.06</td>
    <td align="right">88.84</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.23</td>
    <td align="right">38.88</td>
    <td align="right">36.77</td>
    <td align="right">37.70</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.51</td>
    <td align="right">36.52</td>
    <td align="right">34.16</td>
    <td align="right">35.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">79.81</td>
    <td align="right">147.47</td>
    <td align="right">146.61</td>
    <td align="right">147.11</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.85</td>
    <td align="right">54.02</td>
    <td align="right">51.18</td>
    <td align="right">52.73</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.91</td>
    <td align="right">55.78</td>
    <td align="right">52.90</td>
    <td align="right">54.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">115.37</td>
    <td align="right">183.04</td>
    <td align="right">182.62</td>
    <td align="right">182.83</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.74</td>
    <td align="right">68.28</td>
    <td align="right">65.83</td>
    <td align="right">67.27</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">25.21</td>
    <td align="right">69.25</td>
    <td align="right">66.87</td>
    <td align="right">68.20</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.92</td>
    <td align="right">28.96</td>
    <td align="right">17.79</td>
    <td align="right">30.12</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">6.36</td>
    <td align="right">28.33</td>
    <td align="right">17.70</td>
    <td align="right">29.76</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.67</td>
    <td align="right">31.06</td>
    <td align="right">30.46</td>
    <td align="right">30.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">12.43</td>
    <td align="right">37.71</td>
    <td align="right">21.23</td>
    <td align="right">38.75</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.31</td>
    <td align="right">45.84</td>
    <td align="right">23.57</td>
    <td align="right">44.13</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.55</td>
    <td align="right">39.22</td>
    <td align="right">36.79</td>
    <td align="right">37.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.47</td>
    <td align="right">55.91</td>
    <td align="right">26.64</td>
    <td align="right">53.97</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">34.97</td>
    <td align="right">61.91</td>
    <td align="right">30.18</td>
    <td align="right">58.72</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.07</td>
    <td align="right">64.60</td>
    <td align="right">16.61</td>
    <td align="right">47.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.38</td>
    <td align="right">71.09</td>
    <td align="right">29.24</td>
    <td align="right">67.36</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.54</td>
    <td align="right">79.06</td>
    <td align="right">35.88</td>
    <td align="right">72.69</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.92</td>
    <td align="right">80.39</td>
    <td align="right">18.75</td>
    <td align="right">56.58</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.32</td>
    <td align="right">27.65</td>
    <td align="right">27.03</td>
    <td align="right">27.34</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.14</td>
    <td align="right">30.11</td>
    <td align="right">29.57</td>
    <td align="right">29.89</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.17</td>
    <td align="right">29.18</td>
    <td align="right">28.71</td>
    <td align="right">28.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">12.41</td>
    <td align="right">44.68</td>
    <td align="right">42.32</td>
    <td align="right">43.53</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.35</td>
    <td align="right">51.57</td>
    <td align="right">48.15</td>
    <td align="right">49.72</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.58</td>
    <td align="right">39.70</td>
    <td align="right">37.14</td>
    <td align="right">38.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.93</td>
    <td align="right">61.49</td>
    <td align="right">60.52</td>
    <td align="right">60.97</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.07</td>
    <td align="right">66.10</td>
    <td align="right">65.16</td>
    <td align="right">65.69</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.29</td>
    <td align="right">70.36</td>
    <td align="right">66.97</td>
    <td align="right">68.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.27</td>
    <td align="right">81.17</td>
    <td align="right">80.20</td>
    <td align="right">80.75</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.51</td>
    <td align="right">86.25</td>
    <td align="right">85.44</td>
    <td align="right">85.89</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.95</td>
    <td align="right">86.21</td>
    <td align="right">83.60</td>
    <td align="right">84.88</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.17</td>
    <td align="right">28.65</td>
    <td align="right">17.71</td>
    <td align="right">30.07</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">6.48</td>
    <td align="right">28.40</td>
    <td align="right">17.73</td>
    <td align="right">29.69</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.76</td>
    <td align="right">31.57</td>
    <td align="right">31.01</td>
    <td align="right">31.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.55</td>
    <td align="right">38.80</td>
    <td align="right">21.36</td>
    <td align="right">39.49</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.33</td>
    <td align="right">46.08</td>
    <td align="right">23.53</td>
    <td align="right">43.06</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.78</td>
    <td align="right">40.51</td>
    <td align="right">38.54</td>
    <td align="right">39.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.08</td>
    <td align="right">55.96</td>
    <td align="right">27.16</td>
    <td align="right">53.15</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.25</td>
    <td align="right">63.49</td>
    <td align="right">29.16</td>
    <td align="right">60.95</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">18.39</td>
    <td align="right">65.31</td>
    <td align="right">16.48</td>
    <td align="right">47.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.27</td>
    <td align="right">72.26</td>
    <td align="right">27.99</td>
    <td align="right">66.76</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.92</td>
    <td align="right">79.19</td>
    <td align="right">34.01</td>
    <td align="right">71.95</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.28</td>
    <td align="right">80.62</td>
    <td align="right">18.54</td>
    <td align="right">56.95</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">5.88</td>
    <td align="right">27.86</td>
    <td align="right">27.14</td>
    <td align="right">27.33</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.66</td>
    <td align="right">31.62</td>
    <td align="right">31.15</td>
    <td align="right">31.42</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.18</td>
    <td align="right">30.78</td>
    <td align="right">30.29</td>
    <td align="right">30.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.54</td>
    <td align="right">45.74</td>
    <td align="right">43.77</td>
    <td align="right">44.68</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.40</td>
    <td align="right">55.42</td>
    <td align="right">52.19</td>
    <td align="right">53.61</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.55</td>
    <td align="right">39.25</td>
    <td align="right">37.25</td>
    <td align="right">38.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.15</td>
    <td align="right">67.68</td>
    <td align="right">63.44</td>
    <td align="right">63.85</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.06</td>
    <td align="right">67.88</td>
    <td align="right">66.30</td>
    <td align="right">67.18</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">18.39</td>
    <td align="right">70.89</td>
    <td align="right">67.33</td>
    <td align="right">69.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.23</td>
    <td align="right">84.29</td>
    <td align="right">82.55</td>
    <td align="right">83.48</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.88</td>
    <td align="right">86.65</td>
    <td align="right">85.85</td>
    <td align="right">88.10</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.17</td>
    <td align="right">85.12</td>
    <td align="right">82.60</td>
    <td align="right">83.96</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.57</td>
    <td align="right">30.02</td>
    <td align="right">29.45</td>
    <td align="right">29.69</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.79</td>
    <td align="right">30.68</td>
    <td align="right">30.18</td>
    <td align="right">30.31</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.88</td>
    <td align="right">30.68</td>
    <td align="right">30.26</td>
    <td align="right">30.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.45</td>
    <td align="right">43.26</td>
    <td align="right">40.43</td>
    <td align="right">41.83</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.44</td>
    <td align="right">41.28</td>
    <td align="right">39.14</td>
    <td align="right">40.15</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.45</td>
    <td align="right">45.33</td>
    <td align="right">41.74</td>
    <td align="right">43.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.68</td>
    <td align="right">64.01</td>
    <td align="right">16.50</td>
    <td align="right">46.91</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.49</td>
    <td align="right">66.08</td>
    <td align="right">23.28</td>
    <td align="right">53.66</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.51</td>
    <td align="right">62.69</td>
    <td align="right">22.46</td>
    <td align="right">51.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.71</td>
    <td align="right">79.36</td>
    <td align="right">18.60</td>
    <td align="right">57.72</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">31.67</td>
    <td align="right">84.99</td>
    <td align="right">25.90</td>
    <td align="right">63.90</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.00</td>
    <td align="right">86.01</td>
    <td align="right">26.02</td>
    <td align="right">64.24</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.33</td>
    <td align="right">29.56</td>
    <td align="right">29.14</td>
    <td align="right">29.31</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">7.32</td>
    <td align="right">33.75</td>
    <td align="right">32.96</td>
    <td align="right">33.45</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.53</td>
    <td align="right">31.95</td>
    <td align="right">31.19</td>
    <td align="right">31.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.48</td>
    <td align="right">42.82</td>
    <td align="right">40.10</td>
    <td align="right">41.39</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.48</td>
    <td align="right">41.43</td>
    <td align="right">39.27</td>
    <td align="right">40.43</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.66</td>
    <td align="right">47.93</td>
    <td align="right">44.67</td>
    <td align="right">46.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.75</td>
    <td align="right">69.51</td>
    <td align="right">65.83</td>
    <td align="right">70.51</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.02</td>
    <td align="right">68.37</td>
    <td align="right">66.32</td>
    <td align="right">70.41</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.66</td>
    <td align="right">68.37</td>
    <td align="right">66.54</td>
    <td align="right">67.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.48</td>
    <td align="right">86.04</td>
    <td align="right">83.52</td>
    <td align="right">84.83</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">31.29</td>
    <td align="right">85.19</td>
    <td align="right">84.39</td>
    <td align="right">84.78</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">30.69</td>
    <td align="right">85.06</td>
    <td align="right">84.32</td>
    <td align="right">84.70</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.76</td>
    <td align="right">28.79</td>
    <td align="right">28.31</td>
    <td align="right">28.58</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.12</td>
    <td align="right">32.70</td>
    <td align="right">31.67</td>
    <td align="right">32.07</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.59</td>
    <td align="right">30.59</td>
    <td align="right">29.95</td>
    <td align="right">30.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.94</td>
    <td align="right">42.96</td>
    <td align="right">40.25</td>
    <td align="right">41.59</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.27</td>
    <td align="right">40.98</td>
    <td align="right">38.81</td>
    <td align="right">39.86</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.64</td>
    <td align="right">47.51</td>
    <td align="right">43.90</td>
    <td align="right">45.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.28</td>
    <td align="right">64.11</td>
    <td align="right">16.18</td>
    <td align="right">47.03</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.14</td>
    <td align="right">62.11</td>
    <td align="right">22.10</td>
    <td align="right">50.36</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.37</td>
    <td align="right">62.44</td>
    <td align="right">22.14</td>
    <td align="right">51.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.30</td>
    <td align="right">78.69</td>
    <td align="right">18.15</td>
    <td align="right">55.53</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">30.38</td>
    <td align="right">85.21</td>
    <td align="right">27.00</td>
    <td align="right">65.20</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.73</td>
    <td align="right">84.94</td>
    <td align="right">25.72</td>
    <td align="right">65.55</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.18</td>
    <td align="right">29.56</td>
    <td align="right">28.93</td>
    <td align="right">29.21</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.15</td>
    <td align="right">31.68</td>
    <td align="right">30.86</td>
    <td align="right">31.31</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.52</td>
    <td align="right">32.25</td>
    <td align="right">31.38</td>
    <td align="right">31.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.95</td>
    <td align="right">42.91</td>
    <td align="right">40.23</td>
    <td align="right">41.55</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.48</td>
    <td align="right">41.57</td>
    <td align="right">39.43</td>
    <td align="right">41.78</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.89</td>
    <td align="right">47.97</td>
    <td align="right">44.76</td>
    <td align="right">46.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.25</td>
    <td align="right">69.80</td>
    <td align="right">66.20</td>
    <td align="right">68.05</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.29</td>
    <td align="right">67.41</td>
    <td align="right">65.82</td>
    <td align="right">70.70</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.52</td>
    <td align="right">66.82</td>
    <td align="right">65.25</td>
    <td align="right">66.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.31</td>
    <td align="right">86.53</td>
    <td align="right">83.91</td>
    <td align="right">91.96</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">29.95</td>
    <td align="right">90.44</td>
    <td align="right">89.26</td>
    <td align="right">88.19</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.94</td>
    <td align="right">85.35</td>
    <td align="right">84.59</td>
    <td align="right">84.96</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.13</td>
    <td align="right">27.51</td>
    <td align="right">18.08</td>
    <td align="right">29.52</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.45</td>
    <td align="right">31.92</td>
    <td align="right">24.65</td>
    <td align="right">34.70</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.97</td>
    <td align="right">30.79</td>
    <td align="right">24.55</td>
    <td align="right">32.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.87</td>
    <td align="right">39.24</td>
    <td align="right">20.60</td>
    <td align="right">39.51</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.13</td>
    <td align="right">46.10</td>
    <td align="right">24.24</td>
    <td align="right">47.64</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">31.49</td>
    <td align="right">51.29</td>
    <td align="right">29.79</td>
    <td align="right">46.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.93</td>
    <td align="right">57.81</td>
    <td align="right">24.84</td>
    <td align="right">57.69</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.65</td>
    <td align="right">67.95</td>
    <td align="right">29.88</td>
    <td align="right">67.15</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.25</td>
    <td align="right">74.98</td>
    <td align="right">32.91</td>
    <td align="right">61.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.70</td>
    <td align="right">74.33</td>
    <td align="right">29.48</td>
    <td align="right">73.62</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.51</td>
    <td align="right">86.75</td>
    <td align="right">33.45</td>
    <td align="right">83.16</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">72.33</td>
    <td align="right">108.64</td>
    <td align="right">42.65</td>
    <td align="right">86.36</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.39</td>
    <td align="right">27.74</td>
    <td align="right">27.37</td>
    <td align="right">27.51</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.62</td>
    <td align="right">33.32</td>
    <td align="right">32.68</td>
    <td align="right">33.01</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.98</td>
    <td align="right">32.97</td>
    <td align="right">32.93</td>
    <td align="right">32.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.23</td>
    <td align="right">38.75</td>
    <td align="right">36.45</td>
    <td align="right">37.61</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.82</td>
    <td align="right">49.27</td>
    <td align="right">46.14</td>
    <td align="right">47.58</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.66</td>
    <td align="right">54.93</td>
    <td align="right">54.35</td>
    <td align="right">54.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.08</td>
    <td align="right">56.80</td>
    <td align="right">57.30</td>
    <td align="right">58.57</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.56</td>
    <td align="right">73.71</td>
    <td align="right">69.86</td>
    <td align="right">71.69</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">44.95</td>
    <td align="right">84.52</td>
    <td align="right">83.73</td>
    <td align="right">84.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.09</td>
    <td align="right">71.83</td>
    <td align="right">69.38</td>
    <td align="right">72.52</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.58</td>
    <td align="right">90.12</td>
    <td align="right">87.71</td>
    <td align="right">88.91</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">72.32</td>
    <td align="right">116.47</td>
    <td align="right">116.01</td>
    <td align="right">116.28</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.13</td>
    <td align="right">27.74</td>
    <td align="right">17.90</td>
    <td align="right">30.13</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.59</td>
    <td align="right">30.82</td>
    <td align="right">22.82</td>
    <td align="right">34.80</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.59</td>
    <td align="right">31.62</td>
    <td align="right">24.46</td>
    <td align="right">32.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">18.27</td>
    <td align="right">40.87</td>
    <td align="right">21.25</td>
    <td align="right">41.54</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.89</td>
    <td align="right">47.71</td>
    <td align="right">24.46</td>
    <td align="right">48.99</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">30.15</td>
    <td align="right">49.70</td>
    <td align="right">27.07</td>
    <td align="right">45.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.74</td>
    <td align="right">58.83</td>
    <td align="right">24.84</td>
    <td align="right">59.31</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.49</td>
    <td align="right">67.81</td>
    <td align="right">30.54</td>
    <td align="right">66.65</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.78</td>
    <td align="right">74.72</td>
    <td align="right">26.51</td>
    <td align="right">62.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.68</td>
    <td align="right">71.11</td>
    <td align="right">28.23</td>
    <td align="right">71.25</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.21</td>
    <td align="right">83.17</td>
    <td align="right">33.02</td>
    <td align="right">80.84</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">73.88</td>
    <td align="right">102.69</td>
    <td align="right">29.76</td>
    <td align="right">83.24</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.94</td>
    <td align="right">27.64</td>
    <td align="right">27.08</td>
    <td align="right">27.31</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.58</td>
    <td align="right">33.65</td>
    <td align="right">33.08</td>
    <td align="right">33.33</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.71</td>
    <td align="right">32.50</td>
    <td align="right">32.84</td>
    <td align="right">32.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">18.04</td>
    <td align="right">41.41</td>
    <td align="right">39.33</td>
    <td align="right">40.48</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">24.37</td>
    <td align="right">49.89</td>
    <td align="right">46.96</td>
    <td align="right">48.25</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.64</td>
    <td align="right">54.99</td>
    <td align="right">54.68</td>
    <td align="right">55.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.93</td>
    <td align="right">56.19</td>
    <td align="right">53.40</td>
    <td align="right">54.91</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.63</td>
    <td align="right">71.28</td>
    <td align="right">68.08</td>
    <td align="right">69.65</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.67</td>
    <td align="right">86.40</td>
    <td align="right">84.13</td>
    <td align="right">85.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.51</td>
    <td align="right">72.00</td>
    <td align="right">69.63</td>
    <td align="right">70.77</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">53.33</td>
    <td align="right">90.58</td>
    <td align="right">87.74</td>
    <td align="right">88.95</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">72.44</td>
    <td align="right">114.69</td>
    <td align="right">113.32</td>
    <td align="right">113.56</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.10</td>
    <td align="right">7.85</td>
    <td align="right">5.25</td>
    <td align="right">15.97</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.35</td>
    <td align="right">22.49</td>
    <td align="right">20.94</td>
    <td align="right">23.45</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.06</td>
    <td align="right">19.01</td>
    <td align="right">18.77</td>
    <td align="right">18.90</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.05</td>
    <td align="right">18.89</td>
    <td align="right">18.70</td>
    <td align="right">18.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.64</td>
    <td align="right">26.82</td>
    <td align="right">21.84</td>
    <td align="right">26.70</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.60</td>
    <td align="right">20.44</td>
    <td align="right">20.29</td>
    <td align="right">20.36</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.57</td>
    <td align="right">20.48</td>
    <td align="right">20.36</td>
    <td align="right">20.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.69</td>
    <td align="right">30.93</td>
    <td align="right">20.96</td>
    <td align="right">29.15</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">21.23</td>
    <td align="right">21.11</td>
    <td align="right">21.19</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.93</td>
    <td align="right">21.30</td>
    <td align="right">21.20</td>
    <td align="right">21.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.25</td>
    <td align="right">34.81</td>
    <td align="right">21.52</td>
    <td align="right">31.55</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.41</td>
    <td align="right">21.72</td>
    <td align="right">21.62</td>
    <td align="right">21.68</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.32</td>
    <td align="right">21.95</td>
    <td align="right">21.90</td>
    <td align="right">21.94</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.34</td>
    <td align="right">32.61</td>
    <td align="right">32.57</td>
    <td align="right">32.58</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.06</td>
    <td align="right">18.94</td>
    <td align="right">18.70</td>
    <td align="right">18.84</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.07</td>
    <td align="right">18.91</td>
    <td align="right">18.72</td>
    <td align="right">18.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.65</td>
    <td align="right">39.69</td>
    <td align="right">39.75</td>
    <td align="right">39.72</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.56</td>
    <td align="right">20.44</td>
    <td align="right">20.29</td>
    <td align="right">20.36</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.57</td>
    <td align="right">20.49</td>
    <td align="right">20.38</td>
    <td align="right">20.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.90</td>
    <td align="right">40.78</td>
    <td align="right">40.83</td>
    <td align="right">40.83</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">21.23</td>
    <td align="right">21.12</td>
    <td align="right">21.19</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.92</td>
    <td align="right">21.31</td>
    <td align="right">21.20</td>
    <td align="right">21.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.85</td>
    <td align="right">43.37</td>
    <td align="right">43.37</td>
    <td align="right">43.41</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.41</td>
    <td align="right">21.70</td>
    <td align="right">21.62</td>
    <td align="right">21.66</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.31</td>
    <td align="right">21.95</td>
    <td align="right">21.89</td>
    <td align="right">21.93</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.36</td>
    <td align="right">22.16</td>
    <td align="right">20.88</td>
    <td align="right">23.25</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.49</td>
    <td align="right">18.89</td>
    <td align="right">18.66</td>
    <td align="right">18.79</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.04</td>
    <td align="right">18.93</td>
    <td align="right">18.69</td>
    <td align="right">18.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.32</td>
    <td align="right">27.03</td>
    <td align="right">21.69</td>
    <td align="right">27.04</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.03</td>
    <td align="right">20.43</td>
    <td align="right">20.29</td>
    <td align="right">20.36</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.48</td>
    <td align="right">20.39</td>
    <td align="right">20.26</td>
    <td align="right">20.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.36</td>
    <td align="right">30.99</td>
    <td align="right">21.01</td>
    <td align="right">29.01</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.43</td>
    <td align="right">21.21</td>
    <td align="right">21.10</td>
    <td align="right">21.16</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.88</td>
    <td align="right">21.18</td>
    <td align="right">21.07</td>
    <td align="right">21.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.76</td>
    <td align="right">35.19</td>
    <td align="right">21.38</td>
    <td align="right">31.62</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">4.84</td>
    <td align="right">21.71</td>
    <td align="right">21.61</td>
    <td align="right">21.67</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.22</td>
    <td align="right">21.85</td>
    <td align="right">21.80</td>
    <td align="right">21.83</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.35</td>
    <td align="right">32.52</td>
    <td align="right">32.50</td>
    <td align="right">32.48</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.49</td>
    <td align="right">18.86</td>
    <td align="right">18.64</td>
    <td align="right">18.76</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.03</td>
    <td align="right">18.91</td>
    <td align="right">18.68</td>
    <td align="right">18.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.38</td>
    <td align="right">39.91</td>
    <td align="right">39.96</td>
    <td align="right">39.94</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.03</td>
    <td align="right">20.43</td>
    <td align="right">20.28</td>
    <td align="right">20.37</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.47</td>
    <td align="right">20.41</td>
    <td align="right">20.25</td>
    <td align="right">20.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.70</td>
    <td align="right">40.82</td>
    <td align="right">40.86</td>
    <td align="right">40.85</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.41</td>
    <td align="right">21.21</td>
    <td align="right">21.10</td>
    <td align="right">21.17</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.89</td>
    <td align="right">21.18</td>
    <td align="right">21.07</td>
    <td align="right">21.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.94</td>
    <td align="right">43.18</td>
    <td align="right">43.17</td>
    <td align="right">43.21</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">4.83</td>
    <td align="right">21.71</td>
    <td align="right">21.61</td>
    <td align="right">21.66</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.23</td>
    <td align="right">21.86</td>
    <td align="right">21.82</td>
    <td align="right">21.82</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.28</td>
    <td align="right">20.37</td>
    <td align="right">15.35</td>
    <td align="right">22.32</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.37</td>
    <td align="right">19.73</td>
    <td align="right">14.71</td>
    <td align="right">21.67</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.89</td>
    <td align="right">22.89</td>
    <td align="right">22.70</td>
    <td align="right">22.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.39</td>
    <td align="right">22.05</td>
    <td align="right">16.27</td>
    <td align="right">24.07</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.05</td>
    <td align="right">21.93</td>
    <td align="right">16.40</td>
    <td align="right">24.02</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.77</td>
    <td align="right">22.10</td>
    <td align="right">21.97</td>
    <td align="right">22.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.81</td>
    <td align="right">23.76</td>
    <td align="right">17.18</td>
    <td align="right">25.60</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.98</td>
    <td align="right">23.01</td>
    <td align="right">16.55</td>
    <td align="right">24.78</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.39</td>
    <td align="right">25.13</td>
    <td align="right">4.21</td>
    <td align="right">24.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.20</td>
    <td align="right">24.81</td>
    <td align="right">16.70</td>
    <td align="right">26.18</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.92</td>
    <td align="right">24.40</td>
    <td align="right">16.77</td>
    <td align="right">25.79</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.44</td>
    <td align="right">25.58</td>
    <td align="right">4.20</td>
    <td align="right">25.06</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.22</td>
    <td align="right">22.37</td>
    <td align="right">22.20</td>
    <td align="right">22.30</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.38</td>
    <td align="right">21.93</td>
    <td align="right">21.75</td>
    <td align="right">21.84</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.88</td>
    <td align="right">22.87</td>
    <td align="right">22.71</td>
    <td align="right">22.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.39</td>
    <td align="right">28.45</td>
    <td align="right">28.30</td>
    <td align="right">28.38</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.07</td>
    <td align="right">30.38</td>
    <td align="right">30.26</td>
    <td align="right">30.33</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.78</td>
    <td align="right">22.11</td>
    <td align="right">21.98</td>
    <td align="right">22.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.79</td>
    <td align="right">31.65</td>
    <td align="right">31.63</td>
    <td align="right">31.63</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.99</td>
    <td align="right">30.98</td>
    <td align="right">30.96</td>
    <td align="right">30.99</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.39</td>
    <td align="right">26.77</td>
    <td align="right">26.68</td>
    <td align="right">26.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.21</td>
    <td align="right">32.99</td>
    <td align="right">32.96</td>
    <td align="right">32.95</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.95</td>
    <td align="right">32.41</td>
    <td align="right">32.37</td>
    <td align="right">32.36</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.46</td>
    <td align="right">27.17</td>
    <td align="right">27.10</td>
    <td align="right">27.13</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.13</td>
    <td align="right">20.59</td>
    <td align="right">15.70</td>
    <td align="right">22.55</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.18</td>
    <td align="right">19.51</td>
    <td align="right">14.56</td>
    <td align="right">21.57</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.64</td>
    <td align="right">22.44</td>
    <td align="right">22.24</td>
    <td align="right">22.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.98</td>
    <td align="right">22.01</td>
    <td align="right">16.48</td>
    <td align="right">23.83</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">3.85</td>
    <td align="right">22.07</td>
    <td align="right">16.25</td>
    <td align="right">24.23</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.23</td>
    <td align="right">22.12</td>
    <td align="right">21.95</td>
    <td align="right">22.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.34</td>
    <td align="right">24.20</td>
    <td align="right">17.10</td>
    <td align="right">25.96</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.53</td>
    <td align="right">23.53</td>
    <td align="right">16.45</td>
    <td align="right">25.36</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.21</td>
    <td align="right">25.18</td>
    <td align="right">4.13</td>
    <td align="right">24.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">5.80</td>
    <td align="right">24.90</td>
    <td align="right">16.28</td>
    <td align="right">26.42</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.79</td>
    <td align="right">24.61</td>
    <td align="right">16.46</td>
    <td align="right">25.87</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.24</td>
    <td align="right">25.64</td>
    <td align="right">4.11</td>
    <td align="right">24.83</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.14</td>
    <td align="right">22.26</td>
    <td align="right">22.08</td>
    <td align="right">22.17</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.20</td>
    <td align="right">21.84</td>
    <td align="right">21.65</td>
    <td align="right">21.74</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.64</td>
    <td align="right">22.48</td>
    <td align="right">22.25</td>
    <td align="right">22.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.00</td>
    <td align="right">28.52</td>
    <td align="right">28.37</td>
    <td align="right">28.45</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">3.90</td>
    <td align="right">30.01</td>
    <td align="right">29.91</td>
    <td align="right">29.99</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.23</td>
    <td align="right">22.13</td>
    <td align="right">21.98</td>
    <td align="right">22.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.37</td>
    <td align="right">31.96</td>
    <td align="right">31.89</td>
    <td align="right">31.94</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.53</td>
    <td align="right">30.95</td>
    <td align="right">30.86</td>
    <td align="right">30.90</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.22</td>
    <td align="right">26.48</td>
    <td align="right">26.40</td>
    <td align="right">26.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">5.84</td>
    <td align="right">32.75</td>
    <td align="right">32.71</td>
    <td align="right">32.73</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.76</td>
    <td align="right">32.26</td>
    <td align="right">32.24</td>
    <td align="right">32.25</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.26</td>
    <td align="right">26.87</td>
    <td align="right">26.80</td>
    <td align="right">26.86</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.85</td>
    <td align="right">22.07</td>
    <td align="right">21.90</td>
    <td align="right">21.99</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.92</td>
    <td align="right">24.37</td>
    <td align="right">24.20</td>
    <td align="right">24.28</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.04</td>
    <td align="right">23.81</td>
    <td align="right">23.63</td>
    <td align="right">23.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.95</td>
    <td align="right">23.61</td>
    <td align="right">23.48</td>
    <td align="right">23.56</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.49</td>
    <td align="right">23.26</td>
    <td align="right">23.14</td>
    <td align="right">23.20</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.23</td>
    <td align="right">25.30</td>
    <td align="right">25.20</td>
    <td align="right">25.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.47</td>
    <td align="right">24.23</td>
    <td align="right">3.96</td>
    <td align="right">24.06</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.82</td>
    <td align="right">25.51</td>
    <td align="right">5.92</td>
    <td align="right">26.43</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">5.99</td>
    <td align="right">24.78</td>
    <td align="right">5.79</td>
    <td align="right">25.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.50</td>
    <td align="right">24.65</td>
    <td align="right">3.92</td>
    <td align="right">24.43</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.92</td>
    <td align="right">27.87</td>
    <td align="right">6.03</td>
    <td align="right">28.12</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.21</td>
    <td align="right">27.03</td>
    <td align="right">5.88</td>
    <td align="right">27.50</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.83</td>
    <td align="right">22.06</td>
    <td align="right">21.89</td>
    <td align="right">21.97</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.89</td>
    <td align="right">24.32</td>
    <td align="right">24.16</td>
    <td align="right">24.24</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.09</td>
    <td align="right">23.83</td>
    <td align="right">23.66</td>
    <td align="right">23.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.99</td>
    <td align="right">23.62</td>
    <td align="right">23.49</td>
    <td align="right">23.56</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.52</td>
    <td align="right">23.28</td>
    <td align="right">23.13</td>
    <td align="right">23.21</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.27</td>
    <td align="right">25.31</td>
    <td align="right">25.22</td>
    <td align="right">25.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.48</td>
    <td align="right">25.98</td>
    <td align="right">25.90</td>
    <td align="right">25.94</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.80</td>
    <td align="right">27.53</td>
    <td align="right">27.48</td>
    <td align="right">27.50</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.03</td>
    <td align="right">26.86</td>
    <td align="right">26.80</td>
    <td align="right">26.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.50</td>
    <td align="right">26.41</td>
    <td align="right">26.35</td>
    <td align="right">26.37</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.93</td>
    <td align="right">28.68</td>
    <td align="right">28.63</td>
    <td align="right">28.66</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.24</td>
    <td align="right">28.03</td>
    <td align="right">28.05</td>
    <td align="right">28.03</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.71</td>
    <td align="right">21.67</td>
    <td align="right">21.49</td>
    <td align="right">21.58</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.64</td>
    <td align="right">24.14</td>
    <td align="right">23.95</td>
    <td align="right">24.07</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.90</td>
    <td align="right">23.75</td>
    <td align="right">23.56</td>
    <td align="right">23.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.71</td>
    <td align="right">23.14</td>
    <td align="right">22.96</td>
    <td align="right">23.03</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.15</td>
    <td align="right">23.25</td>
    <td align="right">23.14</td>
    <td align="right">23.21</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.06</td>
    <td align="right">25.25</td>
    <td align="right">25.12</td>
    <td align="right">25.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.43</td>
    <td align="right">24.59</td>
    <td align="right">3.89</td>
    <td align="right">23.99</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.45</td>
    <td align="right">25.29</td>
    <td align="right">5.13</td>
    <td align="right">26.00</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">5.85</td>
    <td align="right">24.59</td>
    <td align="right">4.91</td>
    <td align="right">25.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.47</td>
    <td align="right">25.06</td>
    <td align="right">3.88</td>
    <td align="right">24.32</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.76</td>
    <td align="right">28.06</td>
    <td align="right">5.16</td>
    <td align="right">27.76</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.19</td>
    <td align="right">27.41</td>
    <td align="right">5.01</td>
    <td align="right">27.44</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.61</td>
    <td align="right">21.58</td>
    <td align="right">21.38</td>
    <td align="right">21.48</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.69</td>
    <td align="right">24.20</td>
    <td align="right">23.96</td>
    <td align="right">24.08</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.92</td>
    <td align="right">23.74</td>
    <td align="right">23.56</td>
    <td align="right">23.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.73</td>
    <td align="right">23.10</td>
    <td align="right">22.96</td>
    <td align="right">23.03</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.14</td>
    <td align="right">23.26</td>
    <td align="right">23.14</td>
    <td align="right">23.23</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.06</td>
    <td align="right">25.26</td>
    <td align="right">25.16</td>
    <td align="right">25.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.44</td>
    <td align="right">25.57</td>
    <td align="right">25.50</td>
    <td align="right">25.54</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.47</td>
    <td align="right">27.39</td>
    <td align="right">27.37</td>
    <td align="right">27.35</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">5.82</td>
    <td align="right">26.52</td>
    <td align="right">26.28</td>
    <td align="right">26.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.46</td>
    <td align="right">25.97</td>
    <td align="right">25.92</td>
    <td align="right">25.94</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.74</td>
    <td align="right">28.77</td>
    <td align="right">28.72</td>
    <td align="right">28.75</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.18</td>
    <td align="right">28.12</td>
    <td align="right">28.17</td>
    <td align="right">28.15</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.32</td>
    <td align="right">19.61</td>
    <td align="right">15.51</td>
    <td align="right">22.10</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.74</td>
    <td align="right">9.15</td>
    <td align="right">20.19</td>
    <td align="right">17.65</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.42</td>
    <td align="right">23.30</td>
    <td align="right">21.17</td>
    <td align="right">24.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.72</td>
    <td align="right">22.12</td>
    <td align="right">15.36</td>
    <td align="right">24.18</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.57</td>
    <td align="right">26.17</td>
    <td align="right">17.21</td>
    <td align="right">28.54</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.83</td>
    <td align="right">26.74</td>
    <td align="right">21.58</td>
    <td align="right">26.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.97</td>
    <td align="right">23.34</td>
    <td align="right">14.68</td>
    <td align="right">25.04</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">16.08</td>
    <td align="right">27.42</td>
    <td align="right">17.99</td>
    <td align="right">29.30</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.71</td>
    <td align="right">27.76</td>
    <td align="right">19.78</td>
    <td align="right">28.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.31</td>
    <td align="right">24.06</td>
    <td align="right">15.62</td>
    <td align="right">26.00</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.47</td>
    <td align="right">15.22</td>
    <td align="right">17.27</td>
    <td align="right">21.95</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.49</td>
    <td align="right">32.26</td>
    <td align="right">24.27</td>
    <td align="right">31.27</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.33</td>
    <td align="right">20.96</td>
    <td align="right">20.77</td>
    <td align="right">20.86</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.75</td>
    <td align="right">26.54</td>
    <td align="right">26.37</td>
    <td align="right">26.46</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.58</td>
    <td align="right">25.27</td>
    <td align="right">25.30</td>
    <td align="right">25.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.61</td>
    <td align="right">22.58</td>
    <td align="right">22.44</td>
    <td align="right">22.51</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.55</td>
    <td align="right">28.07</td>
    <td align="right">27.96</td>
    <td align="right">28.04</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.78</td>
    <td align="right">28.81</td>
    <td align="right">28.81</td>
    <td align="right">28.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.97</td>
    <td align="right">24.19</td>
    <td align="right">24.08</td>
    <td align="right">24.13</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">16.15</td>
    <td align="right">29.57</td>
    <td align="right">29.47</td>
    <td align="right">29.54</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.74</td>
    <td align="right">30.34</td>
    <td align="right">30.30</td>
    <td align="right">30.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.31</td>
    <td align="right">25.23</td>
    <td align="right">25.15</td>
    <td align="right">25.19</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.17</td>
    <td align="right">29.70</td>
    <td align="right">29.62</td>
    <td align="right">29.67</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.65</td>
    <td align="right">33.82</td>
    <td align="right">33.70</td>
    <td align="right">33.78</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">5.99</td>
    <td align="right">20.13</td>
    <td align="right">15.54</td>
    <td align="right">22.50</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.73</td>
    <td align="right">9.04</td>
    <td align="right">19.98</td>
    <td align="right">17.27</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.35</td>
    <td align="right">23.46</td>
    <td align="right">20.95</td>
    <td align="right">24.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.03</td>
    <td align="right">22.60</td>
    <td align="right">15.42</td>
    <td align="right">24.71</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.76</td>
    <td align="right">25.88</td>
    <td align="right">16.84</td>
    <td align="right">28.24</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.61</td>
    <td align="right">27.44</td>
    <td align="right">20.47</td>
    <td align="right">27.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.04</td>
    <td align="right">23.90</td>
    <td align="right">14.95</td>
    <td align="right">25.56</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">16.20</td>
    <td align="right">27.08</td>
    <td align="right">17.61</td>
    <td align="right">28.82</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.87</td>
    <td align="right">28.45</td>
    <td align="right">18.13</td>
    <td align="right">28.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.37</td>
    <td align="right">24.61</td>
    <td align="right">15.68</td>
    <td align="right">26.40</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.79</td>
    <td align="right">14.95</td>
    <td align="right">17.04</td>
    <td align="right">21.84</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.70</td>
    <td align="right">33.04</td>
    <td align="right">21.17</td>
    <td align="right">31.98</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">5.98</td>
    <td align="right">21.50</td>
    <td align="right">21.27</td>
    <td align="right">21.40</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.72</td>
    <td align="right">26.20</td>
    <td align="right">26.01</td>
    <td align="right">26.13</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.25</td>
    <td align="right">25.73</td>
    <td align="right">25.75</td>
    <td align="right">25.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.04</td>
    <td align="right">23.38</td>
    <td align="right">23.21</td>
    <td align="right">23.29</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">14.70</td>
    <td align="right">27.70</td>
    <td align="right">27.60</td>
    <td align="right">27.68</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.60</td>
    <td align="right">29.52</td>
    <td align="right">29.54</td>
    <td align="right">29.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.04</td>
    <td align="right">24.87</td>
    <td align="right">24.75</td>
    <td align="right">24.82</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.51</td>
    <td align="right">29.05</td>
    <td align="right">28.94</td>
    <td align="right">29.05</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.62</td>
    <td align="right">30.81</td>
    <td align="right">30.83</td>
    <td align="right">30.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.36</td>
    <td align="right">25.99</td>
    <td align="right">25.88</td>
    <td align="right">25.93</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.14</td>
    <td align="right">29.37</td>
    <td align="right">29.31</td>
    <td align="right">29.34</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">22.00</td>
    <td align="right">34.38</td>
    <td align="right">34.26</td>
    <td align="right">34.34</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">52.03</td>
    <td align="right">30.47</td>
    <td align="right">17.14</td>
    <td align="right">42.76</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.64</td>
    <td align="right">30.76</td>
    <td align="right">24.86</td>
    <td align="right">30.87</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.26</td>
    <td align="right">25.59</td>
    <td align="right">25.18</td>
    <td align="right">25.28</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.40</td>
    <td align="right">27.24</td>
    <td align="right">26.55</td>
    <td align="right">26.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">48.41</td>
    <td align="right">65.33</td>
    <td align="right">30.66</td>
    <td align="right">50.23</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.94</td>
    <td align="right">36.71</td>
    <td align="right">34.52</td>
    <td align="right">36.56</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.70</td>
    <td align="right">38.45</td>
    <td align="right">36.40</td>
    <td align="right">37.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.34</td>
    <td align="right">106.56</td>
    <td align="right">36.14</td>
    <td align="right">73.95</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.14</td>
    <td align="right">53.41</td>
    <td align="right">50.69</td>
    <td align="right">52.18</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.04</td>
    <td align="right">54.94</td>
    <td align="right">51.91</td>
    <td align="right">53.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">120.82</td>
    <td align="right">146.25</td>
    <td align="right">42.65</td>
    <td align="right">99.04</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.12</td>
    <td align="right">66.87</td>
    <td align="right">64.46</td>
    <td align="right">65.78</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.67</td>
    <td align="right">68.31</td>
    <td align="right">65.91</td>
    <td align="right">68.47</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">15.57</td>
    <td align="right">42.72</td>
    <td align="right">42.55</td>
    <td align="right">42.64</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.34</td>
    <td align="right">25.68</td>
    <td align="right">25.24</td>
    <td align="right">25.44</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.43</td>
    <td align="right">25.48</td>
    <td align="right">25.05</td>
    <td align="right">25.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">49.93</td>
    <td align="right">98.85</td>
    <td align="right">97.55</td>
    <td align="right">98.32</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.21</td>
    <td align="right">37.33</td>
    <td align="right">35.18</td>
    <td align="right">36.28</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">10.89</td>
    <td align="right">35.76</td>
    <td align="right">33.54</td>
    <td align="right">34.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">82.10</td>
    <td align="right">144.82</td>
    <td align="right">144.00</td>
    <td align="right">144.46</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.07</td>
    <td align="right">53.31</td>
    <td align="right">50.44</td>
    <td align="right">51.92</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.84</td>
    <td align="right">53.24</td>
    <td align="right">50.36</td>
    <td align="right">51.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">121.30</td>
    <td align="right">177.02</td>
    <td align="right">176.56</td>
    <td align="right">176.77</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.97</td>
    <td align="right">66.28</td>
    <td align="right">63.85</td>
    <td align="right">65.11</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.49</td>
    <td align="right">67.51</td>
    <td align="right">65.10</td>
    <td align="right">66.29</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">16.19</td>
    <td align="right">31.50</td>
    <td align="right">25.09</td>
    <td align="right">31.25</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.54</td>
    <td align="right">24.70</td>
    <td align="right">24.25</td>
    <td align="right">24.44</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.25</td>
    <td align="right">25.42</td>
    <td align="right">25.05</td>
    <td align="right">25.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">53.04</td>
    <td align="right">70.09</td>
    <td align="right">31.63</td>
    <td align="right">53.18</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.73</td>
    <td align="right">37.34</td>
    <td align="right">35.13</td>
    <td align="right">36.37</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">10.53</td>
    <td align="right">34.79</td>
    <td align="right">32.51</td>
    <td align="right">33.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.58</td>
    <td align="right">107.02</td>
    <td align="right">36.26</td>
    <td align="right">74.04</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.53</td>
    <td align="right">53.29</td>
    <td align="right">50.51</td>
    <td align="right">51.82</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.21</td>
    <td align="right">53.43</td>
    <td align="right">50.56</td>
    <td align="right">52.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">123.74</td>
    <td align="right">147.27</td>
    <td align="right">42.64</td>
    <td align="right">99.41</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.44</td>
    <td align="right">66.07</td>
    <td align="right">63.60</td>
    <td align="right">64.93</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.14</td>
    <td align="right">67.54</td>
    <td align="right">65.04</td>
    <td align="right">66.24</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">13.63</td>
    <td align="right">40.12</td>
    <td align="right">40.01</td>
    <td align="right">40.10</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.98</td>
    <td align="right">26.05</td>
    <td align="right">25.53</td>
    <td align="right">25.76</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.61</td>
    <td align="right">25.92</td>
    <td align="right">25.47</td>
    <td align="right">25.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">45.60</td>
    <td align="right">89.17</td>
    <td align="right">87.90</td>
    <td align="right">88.37</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.50</td>
    <td align="right">37.06</td>
    <td align="right">34.85</td>
    <td align="right">35.99</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.50</td>
    <td align="right">37.95</td>
    <td align="right">35.79</td>
    <td align="right">36.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">84.36</td>
    <td align="right">143.34</td>
    <td align="right">142.51</td>
    <td align="right">142.88</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.31</td>
    <td align="right">52.77</td>
    <td align="right">49.89</td>
    <td align="right">51.33</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.59</td>
    <td align="right">54.88</td>
    <td align="right">52.12</td>
    <td align="right">53.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">120.74</td>
    <td align="right">178.35</td>
    <td align="right">178.57</td>
    <td align="right">178.79</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.50</td>
    <td align="right">66.56</td>
    <td align="right">64.10</td>
    <td align="right">65.33</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.14</td>
    <td align="right">67.38</td>
    <td align="right">64.87</td>
    <td align="right">66.21</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.58</td>
    <td align="right">27.73</td>
    <td align="right">16.88</td>
    <td align="right">29.41</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.24</td>
    <td align="right">26.44</td>
    <td align="right">15.94</td>
    <td align="right">28.26</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.80</td>
    <td align="right">28.65</td>
    <td align="right">28.20</td>
    <td align="right">28.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.41</td>
    <td align="right">36.43</td>
    <td align="right">20.62</td>
    <td align="right">37.19</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">10.76</td>
    <td align="right">43.49</td>
    <td align="right">22.43</td>
    <td align="right">42.29</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.56</td>
    <td align="right">37.75</td>
    <td align="right">35.26</td>
    <td align="right">36.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.04</td>
    <td align="right">54.88</td>
    <td align="right">26.71</td>
    <td align="right">53.39</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.90</td>
    <td align="right">56.11</td>
    <td align="right">26.06</td>
    <td align="right">54.02</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.31</td>
    <td align="right">62.34</td>
    <td align="right">14.45</td>
    <td align="right">45.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">24.19</td>
    <td align="right">68.55</td>
    <td align="right">29.49</td>
    <td align="right">65.51</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">25.36</td>
    <td align="right">70.74</td>
    <td align="right">29.62</td>
    <td align="right">66.88</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.23</td>
    <td align="right">76.15</td>
    <td align="right">16.18</td>
    <td align="right">53.82</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.67</td>
    <td align="right">29.08</td>
    <td align="right">28.43</td>
    <td align="right">28.75</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.77</td>
    <td align="right">28.41</td>
    <td align="right">28.09</td>
    <td align="right">28.27</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.93</td>
    <td align="right">30.00</td>
    <td align="right">29.24</td>
    <td align="right">29.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.51</td>
    <td align="right">44.41</td>
    <td align="right">42.27</td>
    <td align="right">43.47</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.64</td>
    <td align="right">51.32</td>
    <td align="right">48.43</td>
    <td align="right">50.05</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">8.17</td>
    <td align="right">39.82</td>
    <td align="right">37.60</td>
    <td align="right">38.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.27</td>
    <td align="right">65.88</td>
    <td align="right">64.87</td>
    <td align="right">65.31</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.70</td>
    <td align="right">68.37</td>
    <td align="right">67.29</td>
    <td align="right">67.77</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.13</td>
    <td align="right">68.19</td>
    <td align="right">64.69</td>
    <td align="right">66.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">24.08</td>
    <td align="right">85.98</td>
    <td align="right">85.07</td>
    <td align="right">85.51</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">25.10</td>
    <td align="right">87.86</td>
    <td align="right">87.03</td>
    <td align="right">87.52</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.25</td>
    <td align="right">82.45</td>
    <td align="right">79.70</td>
    <td align="right">81.18</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.37</td>
    <td align="right">27.70</td>
    <td align="right">17.41</td>
    <td align="right">29.49</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.66</td>
    <td align="right">27.10</td>
    <td align="right">16.56</td>
    <td align="right">28.91</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.82</td>
    <td align="right">29.63</td>
    <td align="right">29.01</td>
    <td align="right">29.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.33</td>
    <td align="right">39.55</td>
    <td align="right">21.72</td>
    <td align="right">40.27</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.00</td>
    <td align="right">39.39</td>
    <td align="right">21.29</td>
    <td align="right">38.84</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.75</td>
    <td align="right">38.50</td>
    <td align="right">36.13</td>
    <td align="right">37.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">17.37</td>
    <td align="right">54.61</td>
    <td align="right">25.92</td>
    <td align="right">51.65</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">17.73</td>
    <td align="right">59.10</td>
    <td align="right">26.66</td>
    <td align="right">54.57</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.77</td>
    <td align="right">61.88</td>
    <td align="right">14.31</td>
    <td align="right">45.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.20</td>
    <td align="right">70.71</td>
    <td align="right">27.74</td>
    <td align="right">66.64</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.51</td>
    <td align="right">71.59</td>
    <td align="right">28.18</td>
    <td align="right">66.94</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.87</td>
    <td align="right">76.75</td>
    <td align="right">16.11</td>
    <td align="right">54.44</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">3.97</td>
    <td align="right">27.90</td>
    <td align="right">27.31</td>
    <td align="right">27.52</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.24</td>
    <td align="right">28.38</td>
    <td align="right">27.93</td>
    <td align="right">28.14</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.00</td>
    <td align="right">29.99</td>
    <td align="right">29.43</td>
    <td align="right">29.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">7.69</td>
    <td align="right">44.09</td>
    <td align="right">41.89</td>
    <td align="right">42.98</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">8.97</td>
    <td align="right">49.88</td>
    <td align="right">47.37</td>
    <td align="right">48.64</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.85</td>
    <td align="right">38.90</td>
    <td align="right">36.61</td>
    <td align="right">37.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">17.51</td>
    <td align="right">71.88</td>
    <td align="right">69.38</td>
    <td align="right">70.78</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">17.99</td>
    <td align="right">72.27</td>
    <td align="right">69.87</td>
    <td align="right">71.05</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.76</td>
    <td align="right">68.00</td>
    <td align="right">64.42</td>
    <td align="right">66.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.02</td>
    <td align="right">87.41</td>
    <td align="right">86.33</td>
    <td align="right">86.82</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.52</td>
    <td align="right">87.72</td>
    <td align="right">86.90</td>
    <td align="right">87.30</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.75</td>
    <td align="right">85.63</td>
    <td align="right">87.75</td>
    <td align="right">89.16</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.88</td>
    <td align="right">29.12</td>
    <td align="right">28.62</td>
    <td align="right">28.83</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.13</td>
    <td align="right">31.04</td>
    <td align="right">30.53</td>
    <td align="right">30.72</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.42</td>
    <td align="right">30.54</td>
    <td align="right">30.21</td>
    <td align="right">30.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.57</td>
    <td align="right">42.31</td>
    <td align="right">39.70</td>
    <td align="right">42.42</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.40</td>
    <td align="right">40.07</td>
    <td align="right">38.01</td>
    <td align="right">39.03</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.64</td>
    <td align="right">47.84</td>
    <td align="right">45.34</td>
    <td align="right">48.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.38</td>
    <td align="right">61.06</td>
    <td align="right">14.21</td>
    <td align="right">44.35</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">20.05</td>
    <td align="right">58.40</td>
    <td align="right">19.34</td>
    <td align="right">49.95</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.22</td>
    <td align="right">58.31</td>
    <td align="right">19.35</td>
    <td align="right">49.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.56</td>
    <td align="right">77.05</td>
    <td align="right">16.22</td>
    <td align="right">54.17</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.28</td>
    <td align="right">82.52</td>
    <td align="right">22.77</td>
    <td align="right">68.22</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.99</td>
    <td align="right">82.31</td>
    <td align="right">22.63</td>
    <td align="right">68.18</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.55</td>
    <td align="right">27.48</td>
    <td align="right">27.12</td>
    <td align="right">27.31</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.34</td>
    <td align="right">30.44</td>
    <td align="right">29.99</td>
    <td align="right">30.27</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.90</td>
    <td align="right">31.40</td>
    <td align="right">30.89</td>
    <td align="right">31.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.24</td>
    <td align="right">40.42</td>
    <td align="right">37.88</td>
    <td align="right">39.28</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.18</td>
    <td align="right">38.98</td>
    <td align="right">36.73</td>
    <td align="right">37.86</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.74</td>
    <td align="right">47.89</td>
    <td align="right">45.10</td>
    <td align="right">46.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.48</td>
    <td align="right">68.83</td>
    <td align="right">65.21</td>
    <td align="right">67.03</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.94</td>
    <td align="right">64.27</td>
    <td align="right">63.21</td>
    <td align="right">63.70</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.80</td>
    <td align="right">64.34</td>
    <td align="right">63.18</td>
    <td align="right">63.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.60</td>
    <td align="right">85.58</td>
    <td align="right">83.01</td>
    <td align="right">84.35</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.33</td>
    <td align="right">84.62</td>
    <td align="right">84.40</td>
    <td align="right">85.17</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.68</td>
    <td align="right">85.62</td>
    <td align="right">85.58</td>
    <td align="right">87.36</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.66</td>
    <td align="right">28.65</td>
    <td align="right">28.11</td>
    <td align="right">28.36</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.90</td>
    <td align="right">30.24</td>
    <td align="right">29.70</td>
    <td align="right">29.96</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.66</td>
    <td align="right">29.62</td>
    <td align="right">29.23</td>
    <td align="right">29.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.23</td>
    <td align="right">42.02</td>
    <td align="right">39.28</td>
    <td align="right">40.65</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.31</td>
    <td align="right">39.03</td>
    <td align="right">37.00</td>
    <td align="right">38.05</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.45</td>
    <td align="right">48.54</td>
    <td align="right">45.47</td>
    <td align="right">46.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.08</td>
    <td align="right">60.99</td>
    <td align="right">14.07</td>
    <td align="right">44.49</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.06</td>
    <td align="right">56.54</td>
    <td align="right">17.79</td>
    <td align="right">47.96</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.80</td>
    <td align="right">57.10</td>
    <td align="right">18.14</td>
    <td align="right">48.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.42</td>
    <td align="right">77.61</td>
    <td align="right">16.03</td>
    <td align="right">54.51</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.01</td>
    <td align="right">83.19</td>
    <td align="right">20.56</td>
    <td align="right">68.10</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">26.89</td>
    <td align="right">80.49</td>
    <td align="right">22.22</td>
    <td align="right">67.75</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.72</td>
    <td align="right">28.72</td>
    <td align="right">28.15</td>
    <td align="right">28.41</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.32</td>
    <td align="right">31.70</td>
    <td align="right">31.04</td>
    <td align="right">31.42</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.99</td>
    <td align="right">30.38</td>
    <td align="right">29.79</td>
    <td align="right">30.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.41</td>
    <td align="right">43.31</td>
    <td align="right">40.66</td>
    <td align="right">41.90</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.19</td>
    <td align="right">41.20</td>
    <td align="right">39.00</td>
    <td align="right">40.05</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.36</td>
    <td align="right">48.89</td>
    <td align="right">45.50</td>
    <td align="right">46.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.18</td>
    <td align="right">68.64</td>
    <td align="right">65.19</td>
    <td align="right">66.94</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.01</td>
    <td align="right">64.32</td>
    <td align="right">62.72</td>
    <td align="right">63.59</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.96</td>
    <td align="right">64.95</td>
    <td align="right">63.55</td>
    <td align="right">64.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.20</td>
    <td align="right">84.84</td>
    <td align="right">82.41</td>
    <td align="right">83.69</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">24.89</td>
    <td align="right">84.54</td>
    <td align="right">83.64</td>
    <td align="right">84.12</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">27.62</td>
    <td align="right">84.16</td>
    <td align="right">83.50</td>
    <td align="right">83.82</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.77</td>
    <td align="right">26.00</td>
    <td align="right">17.28</td>
    <td align="right">28.49</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.08</td>
    <td align="right">12.29</td>
    <td align="right">22.13</td>
    <td align="right">21.18</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">15.35</td>
    <td align="right">31.52</td>
    <td align="right">24.43</td>
    <td align="right">32.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">18.20</td>
    <td align="right">38.79</td>
    <td align="right">20.42</td>
    <td align="right">39.71</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.11</td>
    <td align="right">45.90</td>
    <td align="right">22.05</td>
    <td align="right">45.58</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">31.44</td>
    <td align="right">49.78</td>
    <td align="right">28.48</td>
    <td align="right">45.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">29.09</td>
    <td align="right">55.01</td>
    <td align="right">24.01</td>
    <td align="right">55.26</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.40</td>
    <td align="right">65.45</td>
    <td align="right">27.72</td>
    <td align="right">62.94</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.99</td>
    <td align="right">70.91</td>
    <td align="right">31.53</td>
    <td align="right">60.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.27</td>
    <td align="right">68.69</td>
    <td align="right">27.82</td>
    <td align="right">68.85</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.54</td>
    <td align="right">51.00</td>
    <td align="right">29.87</td>
    <td align="right">52.73</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">77.21</td>
    <td align="right">104.34</td>
    <td align="right">42.37</td>
    <td align="right">84.60</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.86</td>
    <td align="right">27.52</td>
    <td align="right">27.19</td>
    <td align="right">27.34</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.84</td>
    <td align="right">33.58</td>
    <td align="right">32.98</td>
    <td align="right">33.22</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.25</td>
    <td align="right">32.35</td>
    <td align="right">32.25</td>
    <td align="right">32.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.80</td>
    <td align="right">38.68</td>
    <td align="right">36.58</td>
    <td align="right">37.67</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.59</td>
    <td align="right">48.88</td>
    <td align="right">45.39</td>
    <td align="right">47.06</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.85</td>
    <td align="right">52.05</td>
    <td align="right">51.52</td>
    <td align="right">51.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.93</td>
    <td align="right">55.56</td>
    <td align="right">52.74</td>
    <td align="right">54.19</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.23</td>
    <td align="right">71.32</td>
    <td align="right">67.64</td>
    <td align="right">69.43</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.82</td>
    <td align="right">83.37</td>
    <td align="right">82.65</td>
    <td align="right">84.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.01</td>
    <td align="right">69.15</td>
    <td align="right">66.75</td>
    <td align="right">67.97</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.85</td>
    <td align="right">88.68</td>
    <td align="right">86.11</td>
    <td align="right">87.51</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">77.37</td>
    <td align="right">115.78</td>
    <td align="right">114.26</td>
    <td align="right">114.52</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">6.88</td>
    <td align="right">25.47</td>
    <td align="right">16.91</td>
    <td align="right">27.73</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.79</td>
    <td align="right">12.67</td>
    <td align="right">22.53</td>
    <td align="right">21.72</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.83</td>
    <td align="right">30.44</td>
    <td align="right">23.28</td>
    <td align="right">31.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.24</td>
    <td align="right">38.54</td>
    <td align="right">20.29</td>
    <td align="right">39.66</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.57</td>
    <td align="right">45.77</td>
    <td align="right">21.85</td>
    <td align="right">45.32</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">32.08</td>
    <td align="right">48.60</td>
    <td align="right">25.97</td>
    <td align="right">44.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.33</td>
    <td align="right">55.71</td>
    <td align="right">24.28</td>
    <td align="right">55.55</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.44</td>
    <td align="right">63.52</td>
    <td align="right">27.00</td>
    <td align="right">60.69</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">50.63</td>
    <td align="right">72.32</td>
    <td align="right">25.37</td>
    <td align="right">61.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.44</td>
    <td align="right">68.85</td>
    <td align="right">27.81</td>
    <td align="right">68.81</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.59</td>
    <td align="right">50.97</td>
    <td align="right">29.90</td>
    <td align="right">52.83</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">77.86</td>
    <td align="right">103.03</td>
    <td align="right">31.74</td>
    <td align="right">83.36</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.39</td>
    <td align="right">28.19</td>
    <td align="right">27.78</td>
    <td align="right">27.96</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.82</td>
    <td align="right">32.35</td>
    <td align="right">31.69</td>
    <td align="right">31.96</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.00</td>
    <td align="right">31.80</td>
    <td align="right">31.79</td>
    <td align="right">31.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.07</td>
    <td align="right">38.98</td>
    <td align="right">36.80</td>
    <td align="right">37.78</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">21.78</td>
    <td align="right">47.78</td>
    <td align="right">44.24</td>
    <td align="right">45.99</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">30.94</td>
    <td align="right">52.30</td>
    <td align="right">51.78</td>
    <td align="right">52.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.86</td>
    <td align="right">55.42</td>
    <td align="right">52.69</td>
    <td align="right">54.07</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.47</td>
    <td align="right">70.98</td>
    <td align="right">67.17</td>
    <td align="right">70.82</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">50.30</td>
    <td align="right">84.07</td>
    <td align="right">83.47</td>
    <td align="right">83.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.69</td>
    <td align="right">70.80</td>
    <td align="right">68.46</td>
    <td align="right">69.67</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.52</td>
    <td align="right">87.61</td>
    <td align="right">85.23</td>
    <td align="right">86.72</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.22</td>
    <td align="right">115.89</td>
    <td align="right">115.40</td>
    <td align="right">115.70</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.53</td>
    <td align="right">2.92</td>
    <td align="right">2.50</td>
    <td align="right">10.74</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.31</td>
    <td align="right">14.49</td>
    <td align="right">13.60</td>
    <td align="right">14.94</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.29</td>
    <td align="right">13.84</td>
    <td align="right">13.83</td>
    <td align="right">13.83</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.61</td>
    <td align="right">14.32</td>
    <td align="right">14.34</td>
    <td align="right">14.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.46</td>
    <td align="right">16.40</td>
    <td align="right">13.82</td>
    <td align="right">16.52</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">14.25</td>
    <td align="right">14.23</td>
    <td align="right">14.24</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.70</td>
    <td align="right">14.59</td>
    <td align="right">14.57</td>
    <td align="right">14.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.58</td>
    <td align="right">17.32</td>
    <td align="right">13.08</td>
    <td align="right">16.95</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">14.53</td>
    <td align="right">14.54</td>
    <td align="right">14.54</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.75</td>
    <td align="right">14.64</td>
    <td align="right">14.64</td>
    <td align="right">14.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.97</td>
    <td align="right">19.60</td>
    <td align="right">13.27</td>
    <td align="right">18.68</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.80</td>
    <td align="right">14.53</td>
    <td align="right">14.54</td>
    <td align="right">14.54</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.80</td>
    <td align="right">15.02</td>
    <td align="right">15.04</td>
    <td align="right">15.04</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.35</td>
    <td align="right">16.32</td>
    <td align="right">16.21</td>
    <td align="right">16.24</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.31</td>
    <td align="right">13.90</td>
    <td align="right">13.90</td>
    <td align="right">13.84</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.62</td>
    <td align="right">14.37</td>
    <td align="right">14.36</td>
    <td align="right">14.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.46</td>
    <td align="right">18.22</td>
    <td align="right">18.20</td>
    <td align="right">18.24</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">14.24</td>
    <td align="right">14.22</td>
    <td align="right">14.23</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.69</td>
    <td align="right">14.54</td>
    <td align="right">14.59</td>
    <td align="right">14.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.60</td>
    <td align="right">19.48</td>
    <td align="right">19.45</td>
    <td align="right">19.53</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">14.54</td>
    <td align="right">14.52</td>
    <td align="right">14.52</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.75</td>
    <td align="right">14.67</td>
    <td align="right">14.66</td>
    <td align="right">14.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.92</td>
    <td align="right">22.21</td>
    <td align="right">21.90</td>
    <td align="right">21.89</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.79</td>
    <td align="right">14.49</td>
    <td align="right">14.49</td>
    <td align="right">14.49</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.79</td>
    <td align="right">15.02</td>
    <td align="right">15.03</td>
    <td align="right">15.03</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">5.51</td>
    <td align="right">14.18</td>
    <td align="right">13.48</td>
    <td align="right">14.86</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.17</td>
    <td align="right">13.92</td>
    <td align="right">13.91</td>
    <td align="right">13.91</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.29</td>
    <td align="right">14.56</td>
    <td align="right">14.59</td>
    <td align="right">14.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">8.35</td>
    <td align="right">16.04</td>
    <td align="right">13.44</td>
    <td align="right">16.12</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.33</td>
    <td align="right">14.20</td>
    <td align="right">14.21</td>
    <td align="right">14.21</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.47</td>
    <td align="right">14.98</td>
    <td align="right">14.98</td>
    <td align="right">14.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">10.51</td>
    <td align="right">17.19</td>
    <td align="right">12.86</td>
    <td align="right">16.83</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.55</td>
    <td align="right">14.55</td>
    <td align="right">14.57</td>
    <td align="right">14.57</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.65</td>
    <td align="right">15.00</td>
    <td align="right">14.95</td>
    <td align="right">14.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">12.65</td>
    <td align="right">19.79</td>
    <td align="right">13.05</td>
    <td align="right">18.26</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.72</td>
    <td align="right">14.61</td>
    <td align="right">14.54</td>
    <td align="right">14.59</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.63</td>
    <td align="right">15.25</td>
    <td align="right">15.21</td>
    <td align="right">15.26</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">5.55</td>
    <td align="right">16.41</td>
    <td align="right">16.24</td>
    <td align="right">16.24</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.20</td>
    <td align="right">13.97</td>
    <td align="right">13.96</td>
    <td align="right">13.94</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.29</td>
    <td align="right">14.57</td>
    <td align="right">14.58</td>
    <td align="right">14.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">8.33</td>
    <td align="right">18.09</td>
    <td align="right">18.09</td>
    <td align="right">18.07</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.32</td>
    <td align="right">14.15</td>
    <td align="right">14.16</td>
    <td align="right">14.19</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.45</td>
    <td align="right">14.94</td>
    <td align="right">14.92</td>
    <td align="right">14.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">10.54</td>
    <td align="right">19.43</td>
    <td align="right">19.40</td>
    <td align="right">19.41</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.54</td>
    <td align="right">14.51</td>
    <td align="right">14.50</td>
    <td align="right">14.48</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.63</td>
    <td align="right">14.98</td>
    <td align="right">14.94</td>
    <td align="right">14.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">12.50</td>
    <td align="right">21.77</td>
    <td align="right">21.52</td>
    <td align="right">21.69</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.71</td>
    <td align="right">14.55</td>
    <td align="right">14.55</td>
    <td align="right">14.55</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.61</td>
    <td align="right">15.20</td>
    <td align="right">15.20</td>
    <td align="right">15.20</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.23</td>
    <td align="right">13.22</td>
    <td align="right">10.91</td>
    <td align="right">14.33</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.26</td>
    <td align="right">12.73</td>
    <td align="right">10.07</td>
    <td align="right">13.80</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.01</td>
    <td align="right">19.56</td>
    <td align="right">19.51</td>
    <td align="right">19.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.19</td>
    <td align="right">14.26</td>
    <td align="right">12.05</td>
    <td align="right">15.12</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.80</td>
    <td align="right">13.27</td>
    <td align="right">10.71</td>
    <td align="right">14.31</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.50</td>
    <td align="right">17.18</td>
    <td align="right">17.21</td>
    <td align="right">17.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.04</td>
    <td align="right">14.47</td>
    <td align="right">11.66</td>
    <td align="right">15.27</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.11</td>
    <td align="right">13.85</td>
    <td align="right">11.04</td>
    <td align="right">14.84</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.90</td>
    <td align="right">19.06</td>
    <td align="right">1.90</td>
    <td align="right">20.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.53</td>
    <td align="right">14.72</td>
    <td align="right">11.28</td>
    <td align="right">15.59</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.73</td>
    <td align="right">14.28</td>
    <td align="right">11.20</td>
    <td align="right">15.19</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.93</td>
    <td align="right">20.78</td>
    <td align="right">1.87</td>
    <td align="right">20.95</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.23</td>
    <td align="right">17.32</td>
    <td align="right">17.26</td>
    <td align="right">17.27</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.30</td>
    <td align="right">17.07</td>
    <td align="right">17.05</td>
    <td align="right">17.08</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.02</td>
    <td align="right">19.32</td>
    <td align="right">19.31</td>
    <td align="right">19.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.19</td>
    <td align="right">16.77</td>
    <td align="right">16.83</td>
    <td align="right">16.68</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.73</td>
    <td align="right">19.13</td>
    <td align="right">19.14</td>
    <td align="right">19.19</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.52</td>
    <td align="right">17.18</td>
    <td align="right">17.17</td>
    <td align="right">17.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.09</td>
    <td align="right">19.47</td>
    <td align="right">19.48</td>
    <td align="right">19.46</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">19.86</td>
    <td align="right">19.84</td>
    <td align="right">19.82</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.97</td>
    <td align="right">21.16</td>
    <td align="right">21.19</td>
    <td align="right">21.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.50</td>
    <td align="right">20.70</td>
    <td align="right">20.70</td>
    <td align="right">20.68</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.65</td>
    <td align="right">21.44</td>
    <td align="right">21.45</td>
    <td align="right">21.46</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.90</td>
    <td align="right">22.14</td>
    <td align="right">22.09</td>
    <td align="right">22.11</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.94</td>
    <td align="right">13.18</td>
    <td align="right">11.09</td>
    <td align="right">14.38</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.95</td>
    <td align="right">13.10</td>
    <td align="right">10.50</td>
    <td align="right">14.03</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.62</td>
    <td align="right">20.00</td>
    <td align="right">19.97</td>
    <td align="right">20.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.09</td>
    <td align="right">14.30</td>
    <td align="right">11.74</td>
    <td align="right">14.94</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.60</td>
    <td align="right">13.81</td>
    <td align="right">11.28</td>
    <td align="right">14.80</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.40</td>
    <td align="right">17.31</td>
    <td align="right">17.30</td>
    <td align="right">17.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.56</td>
    <td align="right">14.23</td>
    <td align="right">11.90</td>
    <td align="right">15.34</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.52</td>
    <td align="right">14.23</td>
    <td align="right">11.37</td>
    <td align="right">14.89</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.67</td>
    <td align="right">20.00</td>
    <td align="right">1.94</td>
    <td align="right">20.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.25</td>
    <td align="right">14.78</td>
    <td align="right">11.39</td>
    <td align="right">15.61</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.33</td>
    <td align="right">14.79</td>
    <td align="right">11.50</td>
    <td align="right">15.31</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.78</td>
    <td align="right">21.41</td>
    <td align="right">1.87</td>
    <td align="right">21.28</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.94</td>
    <td align="right">17.37</td>
    <td align="right">17.34</td>
    <td align="right">17.33</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.00</td>
    <td align="right">17.64</td>
    <td align="right">17.60</td>
    <td align="right">17.63</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.65</td>
    <td align="right">20.03</td>
    <td align="right">19.98</td>
    <td align="right">20.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.07</td>
    <td align="right">16.72</td>
    <td align="right">16.73</td>
    <td align="right">16.72</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.64</td>
    <td align="right">20.13</td>
    <td align="right">20.04</td>
    <td align="right">19.97</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.40</td>
    <td align="right">17.35</td>
    <td align="right">17.34</td>
    <td align="right">17.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.50</td>
    <td align="right">19.47</td>
    <td align="right">19.72</td>
    <td align="right">19.70</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.49</td>
    <td align="right">20.14</td>
    <td align="right">20.19</td>
    <td align="right">20.18</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.66</td>
    <td align="right">21.93</td>
    <td align="right">22.09</td>
    <td align="right">22.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.27</td>
    <td align="right">21.21</td>
    <td align="right">21.08</td>
    <td align="right">21.09</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.30</td>
    <td align="right">21.93</td>
    <td align="right">21.98</td>
    <td align="right">22.00</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.74</td>
    <td align="right">22.86</td>
    <td align="right">22.83</td>
    <td align="right">22.86</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">1.97</td>
    <td align="right">18.71</td>
    <td align="right">18.70</td>
    <td align="right">18.72</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.22</td>
    <td align="right">13.18</td>
    <td align="right">10.96</td>
    <td align="right">14.34</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.31</td>
    <td align="right">12.74</td>
    <td align="right">10.11</td>
    <td align="right">13.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.02</td>
    <td align="right">17.49</td>
    <td align="right">17.70</td>
    <td align="right">17.64</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.19</td>
    <td align="right">14.23</td>
    <td align="right">12.02</td>
    <td align="right">15.09</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.79</td>
    <td align="right">13.26</td>
    <td align="right">10.74</td>
    <td align="right">14.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.94</td>
    <td align="right">18.38</td>
    <td align="right">1.88</td>
    <td align="right">20.14</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.03</td>
    <td align="right">14.29</td>
    <td align="right">11.65</td>
    <td align="right">15.26</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.08</td>
    <td align="right">13.85</td>
    <td align="right">11.03</td>
    <td align="right">14.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.89</td>
    <td align="right">20.32</td>
    <td align="right">1.85</td>
    <td align="right">20.44</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.63</td>
    <td align="right">14.66</td>
    <td align="right">11.24</td>
    <td align="right">15.59</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.63</td>
    <td align="right">14.24</td>
    <td align="right">11.16</td>
    <td align="right">15.14</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">1.98</td>
    <td align="right">18.74</td>
    <td align="right">18.73</td>
    <td align="right">18.75</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.23</td>
    <td align="right">17.28</td>
    <td align="right">17.28</td>
    <td align="right">17.26</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.27</td>
    <td align="right">17.13</td>
    <td align="right">17.09</td>
    <td align="right">17.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.07</td>
    <td align="right">17.71</td>
    <td align="right">17.49</td>
    <td align="right">17.48</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">16.87</td>
    <td align="right">16.83</td>
    <td align="right">16.84</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.73</td>
    <td align="right">19.35</td>
    <td align="right">19.32</td>
    <td align="right">19.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.88</td>
    <td align="right">20.64</td>
    <td align="right">20.64</td>
    <td align="right">20.61</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.08</td>
    <td align="right">19.64</td>
    <td align="right">19.52</td>
    <td align="right">19.52</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.04</td>
    <td align="right">19.92</td>
    <td align="right">19.83</td>
    <td align="right">20.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.88</td>
    <td align="right">21.91</td>
    <td align="right">21.87</td>
    <td align="right">21.69</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.52</td>
    <td align="right">20.98</td>
    <td align="right">20.94</td>
    <td align="right">20.93</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.73</td>
    <td align="right">21.44</td>
    <td align="right">21.53</td>
    <td align="right">21.43</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">1.63</td>
    <td align="right">19.58</td>
    <td align="right">19.49</td>
    <td align="right">19.56</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.90</td>
    <td align="right">13.21</td>
    <td align="right">11.11</td>
    <td align="right">14.39</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.97</td>
    <td align="right">13.26</td>
    <td align="right">10.55</td>
    <td align="right">14.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">1.67</td>
    <td align="right">18.52</td>
    <td align="right">18.46</td>
    <td align="right">18.47</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.09</td>
    <td align="right">14.42</td>
    <td align="right">11.76</td>
    <td align="right">15.01</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.53</td>
    <td align="right">13.77</td>
    <td align="right">11.18</td>
    <td align="right">14.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.69</td>
    <td align="right">19.33</td>
    <td align="right">1.93</td>
    <td align="right">20.69</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.63</td>
    <td align="right">14.38</td>
    <td align="right">11.87</td>
    <td align="right">15.43</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.49</td>
    <td align="right">14.22</td>
    <td align="right">11.34</td>
    <td align="right">15.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.71</td>
    <td align="right">21.24</td>
    <td align="right">1.87</td>
    <td align="right">21.02</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.19</td>
    <td align="right">14.86</td>
    <td align="right">11.34</td>
    <td align="right">15.43</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.28</td>
    <td align="right">14.74</td>
    <td align="right">11.48</td>
    <td align="right">15.39</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">1.63</td>
    <td align="right">19.68</td>
    <td align="right">19.65</td>
    <td align="right">19.55</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.89</td>
    <td align="right">17.30</td>
    <td align="right">17.40</td>
    <td align="right">17.41</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.94</td>
    <td align="right">17.62</td>
    <td align="right">17.59</td>
    <td align="right">17.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">1.65</td>
    <td align="right">18.46</td>
    <td align="right">18.43</td>
    <td align="right">18.45</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.09</td>
    <td align="right">16.84</td>
    <td align="right">16.80</td>
    <td align="right">16.71</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.52</td>
    <td align="right">20.13</td>
    <td align="right">20.27</td>
    <td align="right">20.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.69</td>
    <td align="right">21.89</td>
    <td align="right">21.75</td>
    <td align="right">21.74</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.54</td>
    <td align="right">19.49</td>
    <td align="right">19.47</td>
    <td align="right">19.48</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.53</td>
    <td align="right">20.38</td>
    <td align="right">20.23</td>
    <td align="right">20.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.69</td>
    <td align="right">22.65</td>
    <td align="right">22.68</td>
    <td align="right">22.68</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.15</td>
    <td align="right">21.17</td>
    <td align="right">21.16</td>
    <td align="right">21.22</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.33</td>
    <td align="right">22.04</td>
    <td align="right">21.99</td>
    <td align="right">21.95</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.22</td>
    <td align="right">13.20</td>
    <td align="right">11.43</td>
    <td align="right">14.41</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.98</td>
    <td align="right">4.44</td>
    <td align="right">13.60</td>
    <td align="right">10.63</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.70</td>
    <td align="right">15.41</td>
    <td align="right">14.56</td>
    <td align="right">16.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.39</td>
    <td align="right">14.72</td>
    <td align="right">10.95</td>
    <td align="right">15.50</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.36</td>
    <td align="right">15.40</td>
    <td align="right">11.24</td>
    <td align="right">16.64</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.87</td>
    <td align="right">17.12</td>
    <td align="right">14.39</td>
    <td align="right">17.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.49</td>
    <td align="right">15.04</td>
    <td align="right">10.64</td>
    <td align="right">15.64</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.49</td>
    <td align="right">15.96</td>
    <td align="right">12.01</td>
    <td align="right">17.01</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.05</td>
    <td align="right">17.61</td>
    <td align="right">13.09</td>
    <td align="right">17.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.98</td>
    <td align="right">15.68</td>
    <td align="right">11.25</td>
    <td align="right">16.07</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.39</td>
    <td align="right">7.57</td>
    <td align="right">11.58</td>
    <td align="right">12.50</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.18</td>
    <td align="right">20.84</td>
    <td align="right">15.66</td>
    <td align="right">20.29</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.21</td>
    <td align="right">14.22</td>
    <td align="right">14.20</td>
    <td align="right">14.23</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.96</td>
    <td align="right">17.11</td>
    <td align="right">17.18</td>
    <td align="right">17.16</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.71</td>
    <td align="right">16.87</td>
    <td align="right">16.87</td>
    <td align="right">16.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.40</td>
    <td align="right">15.44</td>
    <td align="right">15.42</td>
    <td align="right">15.44</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.37</td>
    <td align="right">17.89</td>
    <td align="right">17.94</td>
    <td align="right">17.92</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.91</td>
    <td align="right">19.04</td>
    <td align="right">18.95</td>
    <td align="right">18.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.50</td>
    <td align="right">16.28</td>
    <td align="right">16.26</td>
    <td align="right">16.32</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.53</td>
    <td align="right">18.85</td>
    <td align="right">18.82</td>
    <td align="right">18.83</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.04</td>
    <td align="right">19.97</td>
    <td align="right">19.96</td>
    <td align="right">19.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.02</td>
    <td align="right">17.33</td>
    <td align="right">17.33</td>
    <td align="right">17.27</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.43</td>
    <td align="right">19.22</td>
    <td align="right">19.21</td>
    <td align="right">19.27</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.12</td>
    <td align="right">22.68</td>
    <td align="right">22.66</td>
    <td align="right">22.77</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.18</td>
    <td align="right">13.21</td>
    <td align="right">11.45</td>
    <td align="right">14.37</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.82</td>
    <td align="right">4.42</td>
    <td align="right">13.97</td>
    <td align="right">11.07</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">6.63</td>
    <td align="right">15.82</td>
    <td align="right">15.13</td>
    <td align="right">16.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.40</td>
    <td align="right">14.75</td>
    <td align="right">11.11</td>
    <td align="right">15.50</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.58</td>
    <td align="right">15.65</td>
    <td align="right">11.51</td>
    <td align="right">16.84</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">9.65</td>
    <td align="right">17.47</td>
    <td align="right">14.81</td>
    <td align="right">17.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.46</td>
    <td align="right">15.09</td>
    <td align="right">10.69</td>
    <td align="right">15.80</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.42</td>
    <td align="right">16.22</td>
    <td align="right">12.35</td>
    <td align="right">17.33</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">10.67</td>
    <td align="right">17.53</td>
    <td align="right">13.25</td>
    <td align="right">17.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.04</td>
    <td align="right">15.80</td>
    <td align="right">11.47</td>
    <td align="right">16.12</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.45</td>
    <td align="right">7.57</td>
    <td align="right">11.90</td>
    <td align="right">12.71</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">15.03</td>
    <td align="right">21.69</td>
    <td align="right">15.05</td>
    <td align="right">20.05</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.19</td>
    <td align="right">14.31</td>
    <td align="right">14.20</td>
    <td align="right">14.22</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.84</td>
    <td align="right">17.93</td>
    <td align="right">18.04</td>
    <td align="right">18.12</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">6.63</td>
    <td align="right">16.94</td>
    <td align="right">16.92</td>
    <td align="right">16.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.37</td>
    <td align="right">15.46</td>
    <td align="right">15.40</td>
    <td align="right">15.41</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.22</td>
    <td align="right">18.60</td>
    <td align="right">18.65</td>
    <td align="right">18.67</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">9.63</td>
    <td align="right">19.38</td>
    <td align="right">19.30</td>
    <td align="right">19.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.47</td>
    <td align="right">16.33</td>
    <td align="right">16.29</td>
    <td align="right">16.32</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.49</td>
    <td align="right">19.61</td>
    <td align="right">19.60</td>
    <td align="right">19.53</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">10.68</td>
    <td align="right">20.16</td>
    <td align="right">20.13</td>
    <td align="right">20.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.99</td>
    <td align="right">17.21</td>
    <td align="right">17.35</td>
    <td align="right">17.24</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.38</td>
    <td align="right">19.97</td>
    <td align="right">19.93</td>
    <td align="right">19.94</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">14.97</td>
    <td align="right">22.76</td>
    <td align="right">22.72</td>
    <td align="right">22.83</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.02</td>
    <td align="right">11.08</td>
    <td align="right">5.83</td>
    <td align="right">18.34</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.76</td>
    <td align="right">19.31</td>
    <td align="right">15.79</td>
    <td align="right">19.23</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.02</td>
    <td align="right">21.20</td>
    <td align="right">17.89</td>
    <td align="right">18.39</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.12</td>
    <td align="right">17.03</td>
    <td align="right">16.50</td>
    <td align="right">16.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">12.65</td>
    <td align="right">28.67</td>
    <td align="right">18.76</td>
    <td align="right">26.15</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.52</td>
    <td align="right">34.90</td>
    <td align="right">29.84</td>
    <td align="right">32.19</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.38</td>
    <td align="right">26.34</td>
    <td align="right">25.81</td>
    <td align="right">26.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">31.17</td>
    <td align="right">46.65</td>
    <td align="right">21.94</td>
    <td align="right">38.21</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">7.15</td>
    <td align="right">49.17</td>
    <td align="right">46.45</td>
    <td align="right">49.41</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.18</td>
    <td align="right">37.52</td>
    <td align="right">34.37</td>
    <td align="right">34.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">49.84</td>
    <td align="right">62.44</td>
    <td align="right">23.82</td>
    <td align="right">47.40</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.34</td>
    <td align="right">49.66</td>
    <td align="right">48.67</td>
    <td align="right">48.87</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.00</td>
    <td align="right">49.19</td>
    <td align="right">47.44</td>
    <td align="right">48.73</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.67</td>
    <td align="right">26.07</td>
    <td align="right">25.56</td>
    <td align="right">25.91</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.00</td>
    <td align="right">20.14</td>
    <td align="right">17.49</td>
    <td align="right">19.08</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.08</td>
    <td align="right">16.74</td>
    <td align="right">16.27</td>
    <td align="right">16.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">12.42</td>
    <td align="right">50.66</td>
    <td align="right">50.07</td>
    <td align="right">50.40</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.08</td>
    <td align="right">28.33</td>
    <td align="right">25.48</td>
    <td align="right">27.10</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">2.97</td>
    <td align="right">23.03</td>
    <td align="right">21.80</td>
    <td align="right">22.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">26.94</td>
    <td align="right">92.49</td>
    <td align="right">91.09</td>
    <td align="right">91.15</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">5.97</td>
    <td align="right">38.92</td>
    <td align="right">36.67</td>
    <td align="right">37.88</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">5.75</td>
    <td align="right">34.79</td>
    <td align="right">32.93</td>
    <td align="right">33.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">49.77</td>
    <td align="right">129.92</td>
    <td align="right">129.22</td>
    <td align="right">129.79</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.26</td>
    <td align="right">48.37</td>
    <td align="right">46.67</td>
    <td align="right">47.41</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">6.96</td>
    <td align="right">47.66</td>
    <td align="right">45.90</td>
    <td align="right">46.63</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">6.59</td>
    <td align="right">18.72</td>
    <td align="right">15.47</td>
    <td align="right">18.81</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.86</td>
    <td align="right">19.98</td>
    <td align="right">17.40</td>
    <td align="right">17.80</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.86</td>
    <td align="right">18.51</td>
    <td align="right">17.70</td>
    <td align="right">18.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">10.85</td>
    <td align="right">27.62</td>
    <td align="right">17.95</td>
    <td align="right">25.45</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">2.98</td>
    <td align="right">27.79</td>
    <td align="right">24.69</td>
    <td align="right">26.22</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">2.99</td>
    <td align="right">27.85</td>
    <td align="right">25.04</td>
    <td align="right">26.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">24.14</td>
    <td align="right">41.45</td>
    <td align="right">20.41</td>
    <td align="right">34.87</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">5.93</td>
    <td align="right">38.41</td>
    <td align="right">36.49</td>
    <td align="right">37.61</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">5.89</td>
    <td align="right">39.51</td>
    <td align="right">36.96</td>
    <td align="right">38.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">45.27</td>
    <td align="right">60.69</td>
    <td align="right">23.22</td>
    <td align="right">46.33</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.17</td>
    <td align="right">48.27</td>
    <td align="right">46.39</td>
    <td align="right">46.96</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">6.91</td>
    <td align="right">49.62</td>
    <td align="right">47.71</td>
    <td align="right">48.40</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">6.58</td>
    <td align="right">25.84</td>
    <td align="right">25.35</td>
    <td align="right">25.69</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.87</td>
    <td align="right">20.05</td>
    <td align="right">17.46</td>
    <td align="right">19.17</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.85</td>
    <td align="right">18.55</td>
    <td align="right">17.54</td>
    <td align="right">17.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">10.84</td>
    <td align="right">50.33</td>
    <td align="right">49.78</td>
    <td align="right">50.06</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">2.95</td>
    <td align="right">27.71</td>
    <td align="right">24.70</td>
    <td align="right">26.22</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.00</td>
    <td align="right">27.75</td>
    <td align="right">25.02</td>
    <td align="right">26.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">24.05</td>
    <td align="right">91.29</td>
    <td align="right">89.76</td>
    <td align="right">90.54</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">5.95</td>
    <td align="right">38.42</td>
    <td align="right">36.32</td>
    <td align="right">37.76</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">5.91</td>
    <td align="right">39.52</td>
    <td align="right">37.05</td>
    <td align="right">38.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">45.28</td>
    <td align="right">129.82</td>
    <td align="right">128.97</td>
    <td align="right">129.45</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.17</td>
    <td align="right">48.21</td>
    <td align="right">46.42</td>
    <td align="right">47.04</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">6.91</td>
    <td align="right">49.57</td>
    <td align="right">47.88</td>
    <td align="right">48.66</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.69</td>
    <td align="right">17.49</td>
    <td align="right">11.85</td>
    <td align="right">18.21</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.69</td>
    <td align="right">17.02</td>
    <td align="right">11.14</td>
    <td align="right">17.77</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.38</td>
    <td align="right">23.77</td>
    <td align="right">23.14</td>
    <td align="right">23.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.60</td>
    <td align="right">29.59</td>
    <td align="right">14.53</td>
    <td align="right">28.89</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.09</td>
    <td align="right">27.74</td>
    <td align="right">13.02</td>
    <td align="right">26.45</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.58</td>
    <td align="right">32.29</td>
    <td align="right">29.08</td>
    <td align="right">30.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.64</td>
    <td align="right">40.47</td>
    <td align="right">16.07</td>
    <td align="right">37.37</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.38</td>
    <td align="right">40.38</td>
    <td align="right">15.48</td>
    <td align="right">37.11</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.39</td>
    <td align="right">43.08</td>
    <td align="right">5.83</td>
    <td align="right">34.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.17</td>
    <td align="right">52.14</td>
    <td align="right">16.72</td>
    <td align="right">46.42</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.69</td>
    <td align="right">52.22</td>
    <td align="right">17.14</td>
    <td align="right">47.21</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.39</td>
    <td align="right">60.37</td>
    <td align="right">6.96</td>
    <td align="right">42.51</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.68</td>
    <td align="right">21.62</td>
    <td align="right">21.24</td>
    <td align="right">21.33</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.69</td>
    <td align="right">22.06</td>
    <td align="right">21.27</td>
    <td align="right">21.60</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.37</td>
    <td align="right">23.77</td>
    <td align="right">23.17</td>
    <td align="right">23.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.61</td>
    <td align="right">31.60</td>
    <td align="right">28.60</td>
    <td align="right">30.16</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.04</td>
    <td align="right">34.24</td>
    <td align="right">31.94</td>
    <td align="right">33.09</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.56</td>
    <td align="right">32.34</td>
    <td align="right">29.06</td>
    <td align="right">30.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.61</td>
    <td align="right">49.66</td>
    <td align="right">47.01</td>
    <td align="right">48.34</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.61</td>
    <td align="right">48.07</td>
    <td align="right">46.01</td>
    <td align="right">47.09</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.43</td>
    <td align="right">47.57</td>
    <td align="right">46.20</td>
    <td align="right">46.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.16</td>
    <td align="right">66.17</td>
    <td align="right">64.65</td>
    <td align="right">65.48</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.61</td>
    <td align="right">69.46</td>
    <td align="right">67.24</td>
    <td align="right">67.86</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.41</td>
    <td align="right">64.93</td>
    <td align="right">62.52</td>
    <td align="right">63.58</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.28</td>
    <td align="right">17.79</td>
    <td align="right">12.05</td>
    <td align="right">18.48</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.36</td>
    <td align="right">17.71</td>
    <td align="right">11.60</td>
    <td align="right">18.37</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">1.98</td>
    <td align="right">25.22</td>
    <td align="right">24.27</td>
    <td align="right">24.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.54</td>
    <td align="right">29.59</td>
    <td align="right">14.25</td>
    <td align="right">28.48</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.12</td>
    <td align="right">28.48</td>
    <td align="right">13.58</td>
    <td align="right">27.10</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.52</td>
    <td align="right">32.27</td>
    <td align="right">29.56</td>
    <td align="right">30.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.70</td>
    <td align="right">40.85</td>
    <td align="right">16.68</td>
    <td align="right">37.92</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.81</td>
    <td align="right">41.43</td>
    <td align="right">16.07</td>
    <td align="right">37.74</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.19</td>
    <td align="right">46.70</td>
    <td align="right">6.13</td>
    <td align="right">35.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.83</td>
    <td align="right">51.46</td>
    <td align="right">16.84</td>
    <td align="right">46.40</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.62</td>
    <td align="right">53.34</td>
    <td align="right">17.47</td>
    <td align="right">47.73</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.27</td>
    <td align="right">61.29</td>
    <td align="right">7.39</td>
    <td align="right">43.69</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.28</td>
    <td align="right">22.17</td>
    <td align="right">21.37</td>
    <td align="right">21.84</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.37</td>
    <td align="right">23.12</td>
    <td align="right">22.19</td>
    <td align="right">22.76</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">1.98</td>
    <td align="right">25.18</td>
    <td align="right">24.29</td>
    <td align="right">24.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.56</td>
    <td align="right">31.63</td>
    <td align="right">28.57</td>
    <td align="right">30.18</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.15</td>
    <td align="right">35.68</td>
    <td align="right">33.21</td>
    <td align="right">34.49</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.50</td>
    <td align="right">32.31</td>
    <td align="right">29.19</td>
    <td align="right">30.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.71</td>
    <td align="right">50.61</td>
    <td align="right">47.90</td>
    <td align="right">49.34</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.77</td>
    <td align="right">50.45</td>
    <td align="right">47.64</td>
    <td align="right">49.08</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.22</td>
    <td align="right">51.19</td>
    <td align="right">48.52</td>
    <td align="right">50.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.86</td>
    <td align="right">67.32</td>
    <td align="right">65.13</td>
    <td align="right">66.06</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.62</td>
    <td align="right">69.44</td>
    <td align="right">67.66</td>
    <td align="right">68.60</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.28</td>
    <td align="right">65.70</td>
    <td align="right">63.59</td>
    <td align="right">64.74</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.35</td>
    <td align="right">23.12</td>
    <td align="right">22.46</td>
    <td align="right">22.87</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.68</td>
    <td align="right">17.52</td>
    <td align="right">11.86</td>
    <td align="right">18.23</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.70</td>
    <td align="right">17.13</td>
    <td align="right">11.14</td>
    <td align="right">17.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.75</td>
    <td align="right">29.15</td>
    <td align="right">27.91</td>
    <td align="right">28.81</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.62</td>
    <td align="right">29.63</td>
    <td align="right">14.53</td>
    <td align="right">28.95</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.04</td>
    <td align="right">27.64</td>
    <td align="right">13.04</td>
    <td align="right">26.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.43</td>
    <td align="right">42.48</td>
    <td align="right">5.86</td>
    <td align="right">34.31</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.61</td>
    <td align="right">40.55</td>
    <td align="right">16.09</td>
    <td align="right">37.44</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.38</td>
    <td align="right">40.47</td>
    <td align="right">15.52</td>
    <td align="right">37.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.45</td>
    <td align="right">60.15</td>
    <td align="right">6.96</td>
    <td align="right">42.30</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.17</td>
    <td align="right">52.16</td>
    <td align="right">16.73</td>
    <td align="right">46.49</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.60</td>
    <td align="right">52.42</td>
    <td align="right">17.18</td>
    <td align="right">47.70</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.35</td>
    <td align="right">23.00</td>
    <td align="right">22.46</td>
    <td align="right">22.80</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.68</td>
    <td align="right">21.69</td>
    <td align="right">21.07</td>
    <td align="right">21.33</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.69</td>
    <td align="right">21.95</td>
    <td align="right">21.28</td>
    <td align="right">21.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.77</td>
    <td align="right">28.92</td>
    <td align="right">27.43</td>
    <td align="right">28.49</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.61</td>
    <td align="right">31.61</td>
    <td align="right">28.63</td>
    <td align="right">30.08</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.05</td>
    <td align="right">34.21</td>
    <td align="right">32.07</td>
    <td align="right">33.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.39</td>
    <td align="right">47.29</td>
    <td align="right">45.65</td>
    <td align="right">46.40</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.62</td>
    <td align="right">49.54</td>
    <td align="right">47.06</td>
    <td align="right">48.36</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.68</td>
    <td align="right">48.51</td>
    <td align="right">46.12</td>
    <td align="right">46.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.46</td>
    <td align="right">65.07</td>
    <td align="right">62.79</td>
    <td align="right">64.33</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.16</td>
    <td align="right">66.28</td>
    <td align="right">64.89</td>
    <td align="right">65.60</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.61</td>
    <td align="right">69.44</td>
    <td align="right">67.20</td>
    <td align="right">68.33</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.00</td>
    <td align="right">24.47</td>
    <td align="right">23.68</td>
    <td align="right">24.04</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.28</td>
    <td align="right">19.79</td>
    <td align="right">12.08</td>
    <td align="right">18.40</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.37</td>
    <td align="right">17.71</td>
    <td align="right">11.62</td>
    <td align="right">18.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.64</td>
    <td align="right">33.20</td>
    <td align="right">30.63</td>
    <td align="right">31.81</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.52</td>
    <td align="right">29.49</td>
    <td align="right">14.25</td>
    <td align="right">28.53</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.13</td>
    <td align="right">28.36</td>
    <td align="right">13.58</td>
    <td align="right">27.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.25</td>
    <td align="right">46.60</td>
    <td align="right">6.20</td>
    <td align="right">35.86</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.71</td>
    <td align="right">40.79</td>
    <td align="right">16.68</td>
    <td align="right">37.79</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.86</td>
    <td align="right">41.61</td>
    <td align="right">16.09</td>
    <td align="right">37.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.63</td>
    <td align="right">61.14</td>
    <td align="right">7.44</td>
    <td align="right">43.81</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.84</td>
    <td align="right">51.39</td>
    <td align="right">16.83</td>
    <td align="right">46.40</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.67</td>
    <td align="right">53.47</td>
    <td align="right">17.47</td>
    <td align="right">47.49</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.00</td>
    <td align="right">24.45</td>
    <td align="right">23.69</td>
    <td align="right">24.06</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.28</td>
    <td align="right">22.11</td>
    <td align="right">21.47</td>
    <td align="right">21.79</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.36</td>
    <td align="right">23.09</td>
    <td align="right">22.19</td>
    <td align="right">22.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.65</td>
    <td align="right">33.10</td>
    <td align="right">30.54</td>
    <td align="right">32.02</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.50</td>
    <td align="right">31.56</td>
    <td align="right">28.54</td>
    <td align="right">30.22</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.12</td>
    <td align="right">35.66</td>
    <td align="right">33.11</td>
    <td align="right">34.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.31</td>
    <td align="right">50.91</td>
    <td align="right">48.29</td>
    <td align="right">49.71</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.69</td>
    <td align="right">47.89</td>
    <td align="right">47.95</td>
    <td align="right">49.37</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.80</td>
    <td align="right">50.42</td>
    <td align="right">47.70</td>
    <td align="right">49.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.62</td>
    <td align="right">66.10</td>
    <td align="right">64.06</td>
    <td align="right">65.11</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.84</td>
    <td align="right">67.01</td>
    <td align="right">65.16</td>
    <td align="right">66.12</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.60</td>
    <td align="right">69.31</td>
    <td align="right">67.62</td>
    <td align="right">68.63</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.51</td>
    <td align="right">20.68</td>
    <td align="right">12.54</td>
    <td align="right">19.74</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.72</td>
    <td align="right">5.39</td>
    <td align="right">14.54</td>
    <td align="right">12.05</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">8.93</td>
    <td align="right">18.76</td>
    <td align="right">16.51</td>
    <td align="right">19.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">7.95</td>
    <td align="right">29.56</td>
    <td align="right">13.29</td>
    <td align="right">28.89</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.09</td>
    <td align="right">28.73</td>
    <td align="right">13.33</td>
    <td align="right">28.80</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.01</td>
    <td align="right">28.32</td>
    <td align="right">18.52</td>
    <td align="right">27.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.12</td>
    <td align="right">40.94</td>
    <td align="right">14.65</td>
    <td align="right">40.27</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">20.83</td>
    <td align="right">41.83</td>
    <td align="right">16.71</td>
    <td align="right">40.91</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">23.31</td>
    <td align="right">36.81</td>
    <td align="right">19.04</td>
    <td align="right">34.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.52</td>
    <td align="right">51.40</td>
    <td align="right">16.50</td>
    <td align="right">50.13</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.27</td>
    <td align="right">19.96</td>
    <td align="right">17.48</td>
    <td align="right">25.23</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.68</td>
    <td align="right">57.70</td>
    <td align="right">27.98</td>
    <td align="right">49.39</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.51</td>
    <td align="right">21.84</td>
    <td align="right">19.14</td>
    <td align="right">19.93</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.69</td>
    <td align="right">21.92</td>
    <td align="right">21.37</td>
    <td align="right">21.64</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">8.93</td>
    <td align="right">22.60</td>
    <td align="right">22.31</td>
    <td align="right">22.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">7.96</td>
    <td align="right">30.81</td>
    <td align="right">27.49</td>
    <td align="right">29.18</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.10</td>
    <td align="right">33.13</td>
    <td align="right">30.80</td>
    <td align="right">31.93</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.02</td>
    <td align="right">34.54</td>
    <td align="right">34.07</td>
    <td align="right">34.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.08</td>
    <td align="right">42.06</td>
    <td align="right">39.89</td>
    <td align="right">41.10</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">20.82</td>
    <td align="right">47.47</td>
    <td align="right">46.16</td>
    <td align="right">47.61</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">23.37</td>
    <td align="right">55.42</td>
    <td align="right">54.45</td>
    <td align="right">54.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.48</td>
    <td align="right">52.38</td>
    <td align="right">50.52</td>
    <td align="right">51.15</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.22</td>
    <td align="right">63.06</td>
    <td align="right">60.08</td>
    <td align="right">61.11</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.65</td>
    <td align="right">85.08</td>
    <td align="right">84.34</td>
    <td align="right">84.60</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.58</td>
    <td align="right">20.69</td>
    <td align="right">12.62</td>
    <td align="right">19.53</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.59</td>
    <td align="right">5.36</td>
    <td align="right">14.83</td>
    <td align="right">12.41</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">7.89</td>
    <td align="right">19.02</td>
    <td align="right">16.90</td>
    <td align="right">19.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.27</td>
    <td align="right">29.54</td>
    <td align="right">13.23</td>
    <td align="right">28.68</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">13.82</td>
    <td align="right">29.27</td>
    <td align="right">13.43</td>
    <td align="right">28.83</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">12.71</td>
    <td align="right">28.10</td>
    <td align="right">18.02</td>
    <td align="right">26.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.67</td>
    <td align="right">40.87</td>
    <td align="right">14.69</td>
    <td align="right">40.46</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">21.08</td>
    <td align="right">42.52</td>
    <td align="right">16.75</td>
    <td align="right">41.36</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">21.95</td>
    <td align="right">36.83</td>
    <td align="right">16.94</td>
    <td align="right">34.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.72</td>
    <td align="right">51.35</td>
    <td align="right">16.54</td>
    <td align="right">50.02</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.97</td>
    <td align="right">20.41</td>
    <td align="right">17.39</td>
    <td align="right">25.58</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.42</td>
    <td align="right">59.35</td>
    <td align="right">19.64</td>
    <td align="right">49.19</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.60</td>
    <td align="right">21.69</td>
    <td align="right">19.05</td>
    <td align="right">20.72</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.59</td>
    <td align="right">22.87</td>
    <td align="right">22.43</td>
    <td align="right">22.60</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">7.89</td>
    <td align="right">22.38</td>
    <td align="right">22.15</td>
    <td align="right">22.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.30</td>
    <td align="right">30.49</td>
    <td align="right">27.40</td>
    <td align="right">29.07</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.25</td>
    <td align="right">34.27</td>
    <td align="right">31.76</td>
    <td align="right">33.19</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">12.69</td>
    <td align="right">34.73</td>
    <td align="right">34.23</td>
    <td align="right">34.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.60</td>
    <td align="right">42.13</td>
    <td align="right">39.89</td>
    <td align="right">41.50</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">21.07</td>
    <td align="right">50.17</td>
    <td align="right">47.42</td>
    <td align="right">47.52</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">22.00</td>
    <td align="right">56.14</td>
    <td align="right">54.99</td>
    <td align="right">55.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.70</td>
    <td align="right">52.51</td>
    <td align="right">50.43</td>
    <td align="right">51.53</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.94</td>
    <td align="right">63.20</td>
    <td align="right">61.28</td>
    <td align="right">62.23</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.44</td>
    <td align="right">88.26</td>
    <td align="right">87.74</td>
    <td align="right">87.95</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">24.97</td>
    <td align="right">19.44</td>
    <td align="right">4.84</td>
    <td align="right">17.79</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.41</td>
    <td align="right">12.74</td>
    <td align="right">16.79</td>
    <td align="right">15.87</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.85</td>
    <td align="right">4.73</td>
    <td align="right">5.00</td>
    <td align="right">10.71</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.39</td>
    <td align="right">5.39</td>
    <td align="right">5.60</td>
    <td align="right">11.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.25</td>
    <td align="right">17.15</td>
    <td align="right">17.66</td>
    <td align="right">18.59</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.45</td>
    <td align="right">5.33</td>
    <td align="right">5.27</td>
    <td align="right">11.31</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.10</td>
    <td align="right">5.85</td>
    <td align="right">5.63</td>
    <td align="right">11.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.25</td>
    <td align="right">20.44</td>
    <td align="right">16.49</td>
    <td align="right">20.57</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.09</td>
    <td align="right">5.70</td>
    <td align="right">5.58</td>
    <td align="right">11.80</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.73</td>
    <td align="right">6.50</td>
    <td align="right">6.34</td>
    <td align="right">12.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.07</td>
    <td align="right">26.02</td>
    <td align="right">17.13</td>
    <td align="right">23.77</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.77</td>
    <td align="right">5.99</td>
    <td align="right">5.85</td>
    <td align="right">12.42</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.36</td>
    <td align="right">7.20</td>
    <td align="right">7.01</td>
    <td align="right">12.73</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.35</td>
    <td align="right">22.88</td>
    <td align="right">22.89</td>
    <td align="right">22.89</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.84</td>
    <td align="right">4.72</td>
    <td align="right">4.97</td>
    <td align="right">10.69</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.39</td>
    <td align="right">5.38</td>
    <td align="right">5.58</td>
    <td align="right">11.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.23</td>
    <td align="right">27.94</td>
    <td align="right">27.89</td>
    <td align="right">27.68</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.44</td>
    <td align="right">5.31</td>
    <td align="right">5.24</td>
    <td align="right">11.31</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.07</td>
    <td align="right">5.82</td>
    <td align="right">5.74</td>
    <td align="right">11.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.25</td>
    <td align="right">33.48</td>
    <td align="right">32.60</td>
    <td align="right">32.75</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.09</td>
    <td align="right">5.68</td>
    <td align="right">5.58</td>
    <td align="right">11.87</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.73</td>
    <td align="right">6.56</td>
    <td align="right">6.42</td>
    <td align="right">12.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.08</td>
    <td align="right">39.30</td>
    <td align="right">39.14</td>
    <td align="right">39.15</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.74</td>
    <td align="right">5.98</td>
    <td align="right">5.80</td>
    <td align="right">12.33</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.37</td>
    <td align="right">7.09</td>
    <td align="right">6.93</td>
    <td align="right">12.60</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.26</td>
    <td align="right">12.61</td>
    <td align="right">16.75</td>
    <td align="right">15.81</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.89</td>
    <td align="right">4.72</td>
    <td align="right">5.01</td>
    <td align="right">10.71</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.44</td>
    <td align="right">5.39</td>
    <td align="right">5.61</td>
    <td align="right">10.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.09</td>
    <td align="right">16.91</td>
    <td align="right">17.09</td>
    <td align="right">18.30</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.52</td>
    <td align="right">5.35</td>
    <td align="right">5.26</td>
    <td align="right">11.41</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.07</td>
    <td align="right">5.85</td>
    <td align="right">5.79</td>
    <td align="right">11.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.18</td>
    <td align="right">20.83</td>
    <td align="right">16.79</td>
    <td align="right">20.93</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.14</td>
    <td align="right">5.67</td>
    <td align="right">5.56</td>
    <td align="right">11.79</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.66</td>
    <td align="right">6.52</td>
    <td align="right">6.38</td>
    <td align="right">12.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.68</td>
    <td align="right">25.99</td>
    <td align="right">17.01</td>
    <td align="right">23.68</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.83</td>
    <td align="right">6.00</td>
    <td align="right">5.88</td>
    <td align="right">12.38</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.30</td>
    <td align="right">7.19</td>
    <td align="right">7.03</td>
    <td align="right">12.83</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.22</td>
    <td align="right">23.18</td>
    <td align="right">23.19</td>
    <td align="right">23.17</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.89</td>
    <td align="right">4.73</td>
    <td align="right">5.01</td>
    <td align="right">10.70</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.43</td>
    <td align="right">5.39</td>
    <td align="right">5.61</td>
    <td align="right">10.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.10</td>
    <td align="right">28.30</td>
    <td align="right">28.21</td>
    <td align="right">28.12</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.53</td>
    <td align="right">5.36</td>
    <td align="right">5.30</td>
    <td align="right">11.35</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.08</td>
    <td align="right">5.84</td>
    <td align="right">5.80</td>
    <td align="right">11.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.24</td>
    <td align="right">34.14</td>
    <td align="right">33.68</td>
    <td align="right">33.74</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.16</td>
    <td align="right">5.71</td>
    <td align="right">5.59</td>
    <td align="right">11.84</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.70</td>
    <td align="right">6.56</td>
    <td align="right">6.50</td>
    <td align="right">12.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.84</td>
    <td align="right">40.58</td>
    <td align="right">40.43</td>
    <td align="right">40.34</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.82</td>
    <td align="right">5.98</td>
    <td align="right">5.86</td>
    <td align="right">12.36</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.31</td>
    <td align="right">7.19</td>
    <td align="right">7.04</td>
    <td align="right">12.85</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.45</td>
    <td align="right">8.21</td>
    <td align="right">13.20</td>
    <td align="right">13.06</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">8.41</td>
    <td align="right">8.81</td>
    <td align="right">13.79</td>
    <td align="right">14.02</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.86</td>
    <td align="right">3.33</td>
    <td align="right">3.65</td>
    <td align="right">10.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.26</td>
    <td align="right">11.55</td>
    <td align="right">13.57</td>
    <td align="right">14.73</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.70</td>
    <td align="right">12.77</td>
    <td align="right">14.59</td>
    <td align="right">16.28</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">4.59</td>
    <td align="right">3.54</td>
    <td align="right">11.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.55</td>
    <td align="right">14.37</td>
    <td align="right">15.82</td>
    <td align="right">18.07</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.38</td>
    <td align="right">15.33</td>
    <td align="right">16.84</td>
    <td align="right">18.76</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.31</td>
    <td align="right">6.03</td>
    <td align="right">4.41</td>
    <td align="right">13.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.69</td>
    <td align="right">16.35</td>
    <td align="right">15.23</td>
    <td align="right">19.30</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.15</td>
    <td align="right">21.85</td>
    <td align="right">17.29</td>
    <td align="right">22.97</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.36</td>
    <td align="right">6.06</td>
    <td align="right">4.40</td>
    <td align="right">14.11</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.46</td>
    <td align="right">6.26</td>
    <td align="right">6.17</td>
    <td align="right">12.07</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.53</td>
    <td align="right">6.53</td>
    <td align="right">6.61</td>
    <td align="right">13.35</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.87</td>
    <td align="right">3.33</td>
    <td align="right">3.65</td>
    <td align="right">10.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.26</td>
    <td align="right">8.81</td>
    <td align="right">8.24</td>
    <td align="right">14.31</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.72</td>
    <td align="right">9.11</td>
    <td align="right">8.92</td>
    <td align="right">15.83</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.77</td>
    <td align="right">3.39</td>
    <td align="right">3.32</td>
    <td align="right">11.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.61</td>
    <td align="right">11.06</td>
    <td align="right">10.68</td>
    <td align="right">16.85</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.38</td>
    <td align="right">12.29</td>
    <td align="right">12.01</td>
    <td align="right">18.31</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.31</td>
    <td align="right">4.68</td>
    <td align="right">4.47</td>
    <td align="right">12.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.63</td>
    <td align="right">12.07</td>
    <td align="right">11.62</td>
    <td align="right">17.90</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.21</td>
    <td align="right">13.91</td>
    <td align="right">13.58</td>
    <td align="right">20.07</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.36</td>
    <td align="right">4.72</td>
    <td align="right">4.50</td>
    <td align="right">12.89</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.42</td>
    <td align="right">8.29</td>
    <td align="right">13.18</td>
    <td align="right">12.90</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">8.51</td>
    <td align="right">8.91</td>
    <td align="right">13.61</td>
    <td align="right">13.96</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.85</td>
    <td align="right">3.29</td>
    <td align="right">3.63</td>
    <td align="right">11.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.16</td>
    <td align="right">11.56</td>
    <td align="right">13.74</td>
    <td align="right">15.20</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.52</td>
    <td align="right">12.88</td>
    <td align="right">14.63</td>
    <td align="right">16.38</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">4.57</td>
    <td align="right">3.53</td>
    <td align="right">11.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.51</td>
    <td align="right">14.59</td>
    <td align="right">15.81</td>
    <td align="right">18.15</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.34</td>
    <td align="right">15.26</td>
    <td align="right">16.76</td>
    <td align="right">18.70</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.35</td>
    <td align="right">5.96</td>
    <td align="right">4.40</td>
    <td align="right">13.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.66</td>
    <td align="right">16.37</td>
    <td align="right">15.34</td>
    <td align="right">19.34</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.23</td>
    <td align="right">21.86</td>
    <td align="right">17.35</td>
    <td align="right">23.21</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.37</td>
    <td align="right">5.99</td>
    <td align="right">4.39</td>
    <td align="right">14.05</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.40</td>
    <td align="right">6.14</td>
    <td align="right">6.16</td>
    <td align="right">11.98</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.60</td>
    <td align="right">6.50</td>
    <td align="right">6.58</td>
    <td align="right">13.30</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.87</td>
    <td align="right">3.28</td>
    <td align="right">3.63</td>
    <td align="right">10.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.22</td>
    <td align="right">8.66</td>
    <td align="right">8.11</td>
    <td align="right">14.09</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.52</td>
    <td align="right">9.03</td>
    <td align="right">8.86</td>
    <td align="right">15.40</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">3.40</td>
    <td align="right">3.26</td>
    <td align="right">10.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.58</td>
    <td align="right">11.05</td>
    <td align="right">10.59</td>
    <td align="right">16.62</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.37</td>
    <td align="right">12.23</td>
    <td align="right">11.96</td>
    <td align="right">18.32</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.36</td>
    <td align="right">4.54</td>
    <td align="right">4.40</td>
    <td align="right">12.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.73</td>
    <td align="right">12.16</td>
    <td align="right">11.80</td>
    <td align="right">18.04</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.30</td>
    <td align="right">13.92</td>
    <td align="right">13.58</td>
    <td align="right">19.96</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.39</td>
    <td align="right">4.57</td>
    <td align="right">4.41</td>
    <td align="right">12.87</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.82</td>
    <td align="right">3.15</td>
    <td align="right">3.39</td>
    <td align="right">10.66</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.74</td>
    <td align="right">4.31</td>
    <td align="right">4.49</td>
    <td align="right">12.21</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.80</td>
    <td align="right">4.12</td>
    <td align="right">4.33</td>
    <td align="right">12.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.26</td>
    <td align="right">4.94</td>
    <td align="right">3.89</td>
    <td align="right">12.12</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.20</td>
    <td align="right">5.45</td>
    <td align="right">4.52</td>
    <td align="right">12.60</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.72</td>
    <td align="right">6.34</td>
    <td align="right">5.22</td>
    <td align="right">13.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.41</td>
    <td align="right">5.83</td>
    <td align="right">4.28</td>
    <td align="right">13.53</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.94</td>
    <td align="right">8.08</td>
    <td align="right">6.37</td>
    <td align="right">15.89</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.72</td>
    <td align="right">7.77</td>
    <td align="right">6.12</td>
    <td align="right">15.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.45</td>
    <td align="right">5.83</td>
    <td align="right">4.25</td>
    <td align="right">13.56</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.89</td>
    <td align="right">9.00</td>
    <td align="right">6.40</td>
    <td align="right">16.44</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.11</td>
    <td align="right">8.65</td>
    <td align="right">6.20</td>
    <td align="right">16.06</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.87</td>
    <td align="right">3.15</td>
    <td align="right">3.39</td>
    <td align="right">10.66</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.74</td>
    <td align="right">4.32</td>
    <td align="right">4.49</td>
    <td align="right">12.21</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.80</td>
    <td align="right">4.12</td>
    <td align="right">4.31</td>
    <td align="right">11.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.25</td>
    <td align="right">3.39</td>
    <td align="right">3.28</td>
    <td align="right">11.11</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.19</td>
    <td align="right">6.34</td>
    <td align="right">6.10</td>
    <td align="right">13.49</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.72</td>
    <td align="right">7.11</td>
    <td align="right">6.88</td>
    <td align="right">15.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.41</td>
    <td align="right">4.42</td>
    <td align="right">4.21</td>
    <td align="right">12.42</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.96</td>
    <td align="right">8.88</td>
    <td align="right">8.59</td>
    <td align="right">16.57</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.74</td>
    <td align="right">8.58</td>
    <td align="right">8.22</td>
    <td align="right">15.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.44</td>
    <td align="right">4.41</td>
    <td align="right">4.20</td>
    <td align="right">12.48</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.88</td>
    <td align="right">9.47</td>
    <td align="right">9.23</td>
    <td align="right">17.16</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.08</td>
    <td align="right">9.24</td>
    <td align="right">9.11</td>
    <td align="right">16.86</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.72</td>
    <td align="right">3.10</td>
    <td align="right">3.37</td>
    <td align="right">10.66</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.67</td>
    <td align="right">4.20</td>
    <td align="right">4.41</td>
    <td align="right">12.09</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.78</td>
    <td align="right">4.05</td>
    <td align="right">4.23</td>
    <td align="right">12.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.17</td>
    <td align="right">4.90</td>
    <td align="right">3.79</td>
    <td align="right">12.08</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.24</td>
    <td align="right">5.43</td>
    <td align="right">4.54</td>
    <td align="right">12.56</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.72</td>
    <td align="right">6.13</td>
    <td align="right">5.11</td>
    <td align="right">13.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.39</td>
    <td align="right">5.68</td>
    <td align="right">4.11</td>
    <td align="right">13.43</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.92</td>
    <td align="right">7.99</td>
    <td align="right">6.22</td>
    <td align="right">15.96</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.68</td>
    <td align="right">7.61</td>
    <td align="right">5.91</td>
    <td align="right">15.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.44</td>
    <td align="right">5.72</td>
    <td align="right">4.08</td>
    <td align="right">13.46</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.56</td>
    <td align="right">8.88</td>
    <td align="right">6.20</td>
    <td align="right">16.43</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.01</td>
    <td align="right">8.59</td>
    <td align="right">6.02</td>
    <td align="right">15.99</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.72</td>
    <td align="right">3.08</td>
    <td align="right">3.36</td>
    <td align="right">10.58</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.66</td>
    <td align="right">4.18</td>
    <td align="right">4.38</td>
    <td align="right">12.05</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.77</td>
    <td align="right">4.05</td>
    <td align="right">4.23</td>
    <td align="right">11.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.19</td>
    <td align="right">3.38</td>
    <td align="right">3.28</td>
    <td align="right">11.18</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.21</td>
    <td align="right">6.36</td>
    <td align="right">6.09</td>
    <td align="right">13.53</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.69</td>
    <td align="right">7.03</td>
    <td align="right">6.78</td>
    <td align="right">14.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.37</td>
    <td align="right">4.25</td>
    <td align="right">4.13</td>
    <td align="right">12.29</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.90</td>
    <td align="right">8.88</td>
    <td align="right">8.45</td>
    <td align="right">16.42</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.64</td>
    <td align="right">8.45</td>
    <td align="right">8.15</td>
    <td align="right">16.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.42</td>
    <td align="right">4.28</td>
    <td align="right">4.16</td>
    <td align="right">12.42</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.49</td>
    <td align="right">9.45</td>
    <td align="right">9.32</td>
    <td align="right">17.25</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.02</td>
    <td align="right">9.17</td>
    <td align="right">9.06</td>
    <td align="right">16.83</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.12</td>
    <td align="right">7.95</td>
    <td align="right">12.73</td>
    <td align="right">12.57</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.66</td>
    <td align="right">11.22</td>
    <td align="right">15.85</td>
    <td align="right">15.47</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.05</td>
    <td align="right">13.53</td>
    <td align="right">17.96</td>
    <td align="right">16.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.43</td>
    <td align="right">11.55</td>
    <td align="right">13.92</td>
    <td align="right">15.82</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.73</td>
    <td align="right">12.76</td>
    <td align="right">14.92</td>
    <td align="right">17.18</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.71</td>
    <td align="right">17.38</td>
    <td align="right">18.53</td>
    <td align="right">19.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.42</td>
    <td align="right">13.14</td>
    <td align="right">13.41</td>
    <td align="right">17.09</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.26</td>
    <td align="right">14.90</td>
    <td align="right">15.55</td>
    <td align="right">18.42</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.44</td>
    <td align="right">20.18</td>
    <td align="right">19.08</td>
    <td align="right">21.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.73</td>
    <td align="right">15.60</td>
    <td align="right">14.36</td>
    <td align="right">18.81</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.56</td>
    <td align="right">17.37</td>
    <td align="right">14.17</td>
    <td align="right">20.17</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.66</td>
    <td align="right">25.78</td>
    <td align="right">20.83</td>
    <td align="right">24.02</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.14</td>
    <td align="right">7.48</td>
    <td align="right">7.57</td>
    <td align="right">13.29</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.34</td>
    <td align="right">9.30</td>
    <td align="right">9.28</td>
    <td align="right">15.72</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.12</td>
    <td align="right">10.31</td>
    <td align="right">10.50</td>
    <td align="right">16.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.42</td>
    <td align="right">9.88</td>
    <td align="right">9.57</td>
    <td align="right">15.11</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.75</td>
    <td align="right">11.23</td>
    <td align="right">10.74</td>
    <td align="right">17.18</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.81</td>
    <td align="right">14.54</td>
    <td align="right">14.55</td>
    <td align="right">20.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.43</td>
    <td align="right">12.22</td>
    <td align="right">12.10</td>
    <td align="right">17.28</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.31</td>
    <td align="right">14.51</td>
    <td align="right">14.13</td>
    <td align="right">19.45</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.46</td>
    <td align="right">16.50</td>
    <td align="right">16.40</td>
    <td align="right">22.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.82</td>
    <td align="right">14.59</td>
    <td align="right">14.37</td>
    <td align="right">19.10</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.44</td>
    <td align="right">15.82</td>
    <td align="right">15.80</td>
    <td align="right">20.70</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.64</td>
    <td align="right">24.82</td>
    <td align="right">24.63</td>
    <td align="right">27.66</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.39</td>
    <td align="right">8.16</td>
    <td align="right">13.11</td>
    <td align="right">12.74</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.72</td>
    <td align="right">11.34</td>
    <td align="right">16.00</td>
    <td align="right">15.45</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.24</td>
    <td align="right">13.74</td>
    <td align="right">18.36</td>
    <td align="right">16.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.72</td>
    <td align="right">11.97</td>
    <td align="right">14.11</td>
    <td align="right">16.22</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.77</td>
    <td align="right">12.78</td>
    <td align="right">14.85</td>
    <td align="right">17.33</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.87</td>
    <td align="right">17.60</td>
    <td align="right">19.06</td>
    <td align="right">19.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.91</td>
    <td align="right">13.68</td>
    <td align="right">13.58</td>
    <td align="right">17.16</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.28</td>
    <td align="right">14.94</td>
    <td align="right">15.62</td>
    <td align="right">18.56</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.25</td>
    <td align="right">20.18</td>
    <td align="right">16.68</td>
    <td align="right">21.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">15.19</td>
    <td align="right">16.24</td>
    <td align="right">14.44</td>
    <td align="right">19.26</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.42</td>
    <td align="right">17.48</td>
    <td align="right">14.04</td>
    <td align="right">20.33</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.68</td>
    <td align="right">25.94</td>
    <td align="right">17.45</td>
    <td align="right">24.43</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.36</td>
    <td align="right">7.66</td>
    <td align="right">7.75</td>
    <td align="right">13.51</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.36</td>
    <td align="right">9.17</td>
    <td align="right">9.24</td>
    <td align="right">15.55</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.17</td>
    <td align="right">10.57</td>
    <td align="right">10.74</td>
    <td align="right">17.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.74</td>
    <td align="right">9.92</td>
    <td align="right">9.78</td>
    <td align="right">15.96</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.78</td>
    <td align="right">11.31</td>
    <td align="right">10.99</td>
    <td align="right">17.40</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.87</td>
    <td align="right">15.06</td>
    <td align="right">14.95</td>
    <td align="right">21.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.93</td>
    <td align="right">13.01</td>
    <td align="right">12.68</td>
    <td align="right">18.30</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.20</td>
    <td align="right">14.35</td>
    <td align="right">14.19</td>
    <td align="right">19.61</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.26</td>
    <td align="right">16.40</td>
    <td align="right">16.33</td>
    <td align="right">22.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">15.09</td>
    <td align="right">14.93</td>
    <td align="right">14.67</td>
    <td align="right">19.61</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.35</td>
    <td align="right">15.95</td>
    <td align="right">15.81</td>
    <td align="right">20.93</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.72</td>
    <td align="right">24.18</td>
    <td align="right">23.96</td>
    <td align="right">28.75</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">46.27</td>
    <td align="right">72.85</td>
    <td align="right">17.33</td>
    <td align="right">53.99</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">11.12</td>
    <td align="right">13.19</td>
    <td align="right">18.62</td>
    <td align="right">17.81</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.24</td>
    <td align="right">4.98</td>
    <td align="right">5.37</td>
    <td align="right">11.95</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.75</td>
    <td align="right">5.70</td>
    <td align="right">5.99</td>
    <td align="right">12.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">16.91</td>
    <td align="right">18.28</td>
    <td align="right">19.36</td>
    <td align="right">20.65</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.09</td>
    <td align="right">9.46</td>
    <td align="right">6.99</td>
    <td align="right">13.99</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.75</td>
    <td align="right">10.08</td>
    <td align="right">7.41</td>
    <td align="right">14.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.72</td>
    <td align="right">80.60</td>
    <td align="right">29.18</td>
    <td align="right">56.23</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.44</td>
    <td align="right">16.87</td>
    <td align="right">15.84</td>
    <td align="right">22.50</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.50</td>
    <td align="right">20.14</td>
    <td align="right">18.98</td>
    <td align="right">25.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.18</td>
    <td align="right">119.00</td>
    <td align="right">35.77</td>
    <td align="right">79.41</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.72</td>
    <td align="right">20.33</td>
    <td align="right">19.61</td>
    <td align="right">27.44</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.91</td>
    <td align="right">24.83</td>
    <td align="right">24.11</td>
    <td align="right">31.47</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">11.08</td>
    <td align="right">24.20</td>
    <td align="right">24.20</td>
    <td align="right">24.17</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.24</td>
    <td align="right">4.97</td>
    <td align="right">5.31</td>
    <td align="right">11.97</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.76</td>
    <td align="right">5.71</td>
    <td align="right">5.99</td>
    <td align="right">12.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">16.72</td>
    <td align="right">31.17</td>
    <td align="right">30.05</td>
    <td align="right">31.27</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.83</td>
    <td align="right">9.40</td>
    <td align="right">6.82</td>
    <td align="right">13.73</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">7.32</td>
    <td align="right">9.81</td>
    <td align="right">7.36</td>
    <td align="right">14.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.56</td>
    <td align="right">112.54</td>
    <td align="right">111.37</td>
    <td align="right">112.00</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.46</td>
    <td align="right">16.96</td>
    <td align="right">15.84</td>
    <td align="right">22.48</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.57</td>
    <td align="right">20.10</td>
    <td align="right">18.90</td>
    <td align="right">25.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.06</td>
    <td align="right">172.20</td>
    <td align="right">172.01</td>
    <td align="right">172.21</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.68</td>
    <td align="right">20.31</td>
    <td align="right">19.58</td>
    <td align="right">27.37</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.88</td>
    <td align="right">24.87</td>
    <td align="right">24.09</td>
    <td align="right">31.40</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">10.90</td>
    <td align="right">12.98</td>
    <td align="right">18.50</td>
    <td align="right">17.74</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">6.29</td>
    <td align="right">4.99</td>
    <td align="right">5.31</td>
    <td align="right">11.96</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.81</td>
    <td align="right">11.57</td>
    <td align="right">11.60</td>
    <td align="right">17.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">16.81</td>
    <td align="right">18.78</td>
    <td align="right">19.15</td>
    <td align="right">21.56</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.07</td>
    <td align="right">9.23</td>
    <td align="right">6.82</td>
    <td align="right">13.77</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.62</td>
    <td align="right">9.97</td>
    <td align="right">7.17</td>
    <td align="right">13.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.47</td>
    <td align="right">81.65</td>
    <td align="right">29.52</td>
    <td align="right">56.26</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.51</td>
    <td align="right">18.61</td>
    <td align="right">17.17</td>
    <td align="right">23.96</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.37</td>
    <td align="right">20.08</td>
    <td align="right">18.93</td>
    <td align="right">25.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">102.99</td>
    <td align="right">120.61</td>
    <td align="right">36.34</td>
    <td align="right">80.78</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.64</td>
    <td align="right">23.13</td>
    <td align="right">22.37</td>
    <td align="right">29.95</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.57</td>
    <td align="right">24.91</td>
    <td align="right">24.12</td>
    <td align="right">31.56</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">10.91</td>
    <td align="right">24.45</td>
    <td align="right">24.48</td>
    <td align="right">24.45</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.29</td>
    <td align="right">4.98</td>
    <td align="right">5.39</td>
    <td align="right">12.00</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.83</td>
    <td align="right">5.72</td>
    <td align="right">6.04</td>
    <td align="right">12.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">16.45</td>
    <td align="right">30.51</td>
    <td align="right">29.82</td>
    <td align="right">33.04</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">7.54</td>
    <td align="right">9.09</td>
    <td align="right">6.76</td>
    <td align="right">13.73</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">8.05</td>
    <td align="right">9.86</td>
    <td align="right">7.23</td>
    <td align="right">14.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.25</td>
    <td align="right">115.87</td>
    <td align="right">114.64</td>
    <td align="right">115.23</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.53</td>
    <td align="right">18.50</td>
    <td align="right">17.16</td>
    <td align="right">23.89</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.29</td>
    <td align="right">20.14</td>
    <td align="right">18.92</td>
    <td align="right">25.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.12</td>
    <td align="right">180.73</td>
    <td align="right">179.92</td>
    <td align="right">180.64</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.68</td>
    <td align="right">23.02</td>
    <td align="right">22.30</td>
    <td align="right">30.02</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.60</td>
    <td align="right">24.84</td>
    <td align="right">24.07</td>
    <td align="right">31.68</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.13</td>
    <td align="right">8.77</td>
    <td align="right">13.69</td>
    <td align="right">14.42</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.68</td>
    <td align="right">9.39</td>
    <td align="right">14.55</td>
    <td align="right">15.62</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.18</td>
    <td align="right">3.54</td>
    <td align="right">3.93</td>
    <td align="right">12.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.00</td>
    <td align="right">15.88</td>
    <td align="right">15.29</td>
    <td align="right">17.67</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.35</td>
    <td align="right">18.51</td>
    <td align="right">15.74</td>
    <td align="right">19.19</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.57</td>
    <td align="right">8.36</td>
    <td align="right">5.02</td>
    <td align="right">13.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.29</td>
    <td align="right">32.97</td>
    <td align="right">24.51</td>
    <td align="right">33.67</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.69</td>
    <td align="right">33.95</td>
    <td align="right">28.30</td>
    <td align="right">36.16</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.06</td>
    <td align="right">19.39</td>
    <td align="right">14.06</td>
    <td align="right">23.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.26</td>
    <td align="right">49.08</td>
    <td align="right">27.39</td>
    <td align="right">47.67</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.05</td>
    <td align="right">60.66</td>
    <td align="right">33.67</td>
    <td align="right">57.36</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.41</td>
    <td align="right">22.29</td>
    <td align="right">16.04</td>
    <td align="right">27.67</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.57</td>
    <td align="right">6.61</td>
    <td align="right">6.58</td>
    <td align="right">13.29</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.73</td>
    <td align="right">6.86</td>
    <td align="right">7.15</td>
    <td align="right">14.59</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.16</td>
    <td align="right">3.53</td>
    <td align="right">3.92</td>
    <td align="right">12.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">9.92</td>
    <td align="right">12.51</td>
    <td align="right">9.95</td>
    <td align="right">17.02</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.27</td>
    <td align="right">14.15</td>
    <td align="right">10.84</td>
    <td align="right">18.41</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">8.01</td>
    <td align="right">7.36</td>
    <td align="right">5.01</td>
    <td align="right">13.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.30</td>
    <td align="right">29.20</td>
    <td align="right">26.82</td>
    <td align="right">35.15</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.75</td>
    <td align="right">30.87</td>
    <td align="right">29.80</td>
    <td align="right">37.68</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.01</td>
    <td align="right">16.26</td>
    <td align="right">15.49</td>
    <td align="right">24.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.26</td>
    <td align="right">38.08</td>
    <td align="right">37.14</td>
    <td align="right">46.64</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.99</td>
    <td align="right">39.98</td>
    <td align="right">39.38</td>
    <td align="right">49.17</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.48</td>
    <td align="right">18.49</td>
    <td align="right">17.95</td>
    <td align="right">28.86</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.07</td>
    <td align="right">8.84</td>
    <td align="right">13.73</td>
    <td align="right">14.36</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.69</td>
    <td align="right">9.51</td>
    <td align="right">14.45</td>
    <td align="right">15.58</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">5.45</td>
    <td align="right">3.52</td>
    <td align="right">3.91</td>
    <td align="right">12.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">9.84</td>
    <td align="right">15.99</td>
    <td align="right">15.52</td>
    <td align="right">18.49</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.08</td>
    <td align="right">19.24</td>
    <td align="right">15.89</td>
    <td align="right">19.59</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.00</td>
    <td align="right">8.49</td>
    <td align="right">5.13</td>
    <td align="right">13.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.58</td>
    <td align="right">33.29</td>
    <td align="right">24.68</td>
    <td align="right">34.33</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">30.16</td>
    <td align="right">33.75</td>
    <td align="right">28.03</td>
    <td align="right">36.01</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.12</td>
    <td align="right">19.36</td>
    <td align="right">14.36</td>
    <td align="right">23.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.26</td>
    <td align="right">49.73</td>
    <td align="right">27.84</td>
    <td align="right">48.54</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.15</td>
    <td align="right">60.77</td>
    <td align="right">33.77</td>
    <td align="right">57.60</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">18.11</td>
    <td align="right">22.33</td>
    <td align="right">16.47</td>
    <td align="right">27.65</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.11</td>
    <td align="right">6.59</td>
    <td align="right">6.60</td>
    <td align="right">13.28</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.76</td>
    <td align="right">6.85</td>
    <td align="right">7.02</td>
    <td align="right">14.55</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.19</td>
    <td align="right">8.77</td>
    <td align="right">8.65</td>
    <td align="right">15.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">9.81</td>
    <td align="right">12.76</td>
    <td align="right">9.91</td>
    <td align="right">17.12</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.07</td>
    <td align="right">14.30</td>
    <td align="right">11.24</td>
    <td align="right">18.14</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">5.25</td>
    <td align="right">13.70</td>
    <td align="right">13.11</td>
    <td align="right">22.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.55</td>
    <td align="right">30.45</td>
    <td align="right">28.84</td>
    <td align="right">36.93</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">30.18</td>
    <td align="right">30.98</td>
    <td align="right">29.82</td>
    <td align="right">37.59</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.20</td>
    <td align="right">16.19</td>
    <td align="right">15.30</td>
    <td align="right">24.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.28</td>
    <td align="right">38.00</td>
    <td align="right">37.17</td>
    <td align="right">46.57</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.26</td>
    <td align="right">40.08</td>
    <td align="right">39.54</td>
    <td align="right">49.21</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">18.07</td>
    <td align="right">18.37</td>
    <td align="right">17.67</td>
    <td align="right">28.73</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">5.08</td>
    <td align="right">3.30</td>
    <td align="right">3.65</td>
    <td align="right">11.96</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.12</td>
    <td align="right">4.53</td>
    <td align="right">4.86</td>
    <td align="right">13.63</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.21</td>
    <td align="right">4.33</td>
    <td align="right">4.62</td>
    <td align="right">13.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">4.87</td>
    <td align="right">9.27</td>
    <td align="right">5.53</td>
    <td align="right">14.36</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">7.43</td>
    <td align="right">9.36</td>
    <td align="right">5.97</td>
    <td align="right">14.69</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">8.61</td>
    <td align="right">10.77</td>
    <td align="right">6.76</td>
    <td align="right">15.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.03</td>
    <td align="right">19.40</td>
    <td align="right">14.02</td>
    <td align="right">23.32</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.21</td>
    <td align="right">23.44</td>
    <td align="right">19.10</td>
    <td align="right">28.48</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.95</td>
    <td align="right">23.17</td>
    <td align="right">18.87</td>
    <td align="right">27.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.87</td>
    <td align="right">22.38</td>
    <td align="right">16.06</td>
    <td align="right">27.49</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.91</td>
    <td align="right">29.14</td>
    <td align="right">22.85</td>
    <td align="right">34.68</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.87</td>
    <td align="right">29.00</td>
    <td align="right">22.90</td>
    <td align="right">34.41</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">6.09</td>
    <td align="right">3.33</td>
    <td align="right">3.64</td>
    <td align="right">11.97</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.12</td>
    <td align="right">4.50</td>
    <td align="right">4.84</td>
    <td align="right">13.65</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.21</td>
    <td align="right">4.33</td>
    <td align="right">4.64</td>
    <td align="right">13.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">4.89</td>
    <td align="right">7.54</td>
    <td align="right">5.14</td>
    <td align="right">13.15</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">5.71</td>
    <td align="right">10.14</td>
    <td align="right">7.50</td>
    <td align="right">15.76</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.20</td>
    <td align="right">11.90</td>
    <td align="right">8.69</td>
    <td align="right">17.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.12</td>
    <td align="right">16.11</td>
    <td align="right">15.20</td>
    <td align="right">24.10</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.18</td>
    <td align="right">24.10</td>
    <td align="right">23.36</td>
    <td align="right">32.35</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.97</td>
    <td align="right">23.96</td>
    <td align="right">23.35</td>
    <td align="right">32.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.87</td>
    <td align="right">18.42</td>
    <td align="right">17.66</td>
    <td align="right">28.56</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.80</td>
    <td align="right">29.65</td>
    <td align="right">29.25</td>
    <td align="right">40.20</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.91</td>
    <td align="right">29.74</td>
    <td align="right">29.30</td>
    <td align="right">40.06</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.03</td>
    <td align="right">3.25</td>
    <td align="right">3.64</td>
    <td align="right">11.97</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.06</td>
    <td align="right">4.59</td>
    <td align="right">4.75</td>
    <td align="right">13.42</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.19</td>
    <td align="right">4.28</td>
    <td align="right">4.64</td>
    <td align="right">13.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">4.80</td>
    <td align="right">9.49</td>
    <td align="right">5.61</td>
    <td align="right">14.35</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">7.92</td>
    <td align="right">9.29</td>
    <td align="right">5.98</td>
    <td align="right">14.76</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">8.07</td>
    <td align="right">10.62</td>
    <td align="right">6.81</td>
    <td align="right">15.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.07</td>
    <td align="right">19.23</td>
    <td align="right">13.86</td>
    <td align="right">23.04</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.15</td>
    <td align="right">23.34</td>
    <td align="right">18.96</td>
    <td align="right">28.48</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.91</td>
    <td align="right">23.13</td>
    <td align="right">18.86</td>
    <td align="right">27.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">18.02</td>
    <td align="right">22.22</td>
    <td align="right">15.89</td>
    <td align="right">27.07</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">29.58</td>
    <td align="right">29.15</td>
    <td align="right">22.64</td>
    <td align="right">34.63</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.21</td>
    <td align="right">28.98</td>
    <td align="right">22.72</td>
    <td align="right">34.42</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.04</td>
    <td align="right">3.28</td>
    <td align="right">3.66</td>
    <td align="right">12.05</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.61</td>
    <td align="right">4.39</td>
    <td align="right">4.70</td>
    <td align="right">13.48</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.25</td>
    <td align="right">4.30</td>
    <td align="right">4.56</td>
    <td align="right">13.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.60</td>
    <td align="right">7.76</td>
    <td align="right">5.15</td>
    <td align="right">13.12</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">5.91</td>
    <td align="right">10.31</td>
    <td align="right">7.81</td>
    <td align="right">16.46</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.15</td>
    <td align="right">12.10</td>
    <td align="right">8.67</td>
    <td align="right">16.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.07</td>
    <td align="right">16.03</td>
    <td align="right">15.25</td>
    <td align="right">24.03</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.14</td>
    <td align="right">24.22</td>
    <td align="right">23.47</td>
    <td align="right">32.55</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.80</td>
    <td align="right">23.77</td>
    <td align="right">23.14</td>
    <td align="right">31.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.93</td>
    <td align="right">18.14</td>
    <td align="right">17.52</td>
    <td align="right">28.41</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">29.49</td>
    <td align="right">29.60</td>
    <td align="right">29.30</td>
    <td align="right">40.24</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.21</td>
    <td align="right">29.59</td>
    <td align="right">29.31</td>
    <td align="right">40.23</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.75</td>
    <td align="right">8.56</td>
    <td align="right">13.61</td>
    <td align="right">13.86</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.71</td>
    <td align="right">12.09</td>
    <td align="right">16.80</td>
    <td align="right">17.00</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.50</td>
    <td align="right">14.87</td>
    <td align="right">19.31</td>
    <td align="right">18.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.10</td>
    <td align="right">15.69</td>
    <td align="right">15.65</td>
    <td align="right">18.83</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.10</td>
    <td align="right">18.37</td>
    <td align="right">16.24</td>
    <td align="right">20.32</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">15.25</td>
    <td align="right">19.29</td>
    <td align="right">19.72</td>
    <td align="right">22.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.46</td>
    <td align="right">28.73</td>
    <td align="right">22.35</td>
    <td align="right">32.13</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.65</td>
    <td align="right">35.85</td>
    <td align="right">25.96</td>
    <td align="right">37.07</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.37</td>
    <td align="right">47.39</td>
    <td align="right">29.26</td>
    <td align="right">41.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.61</td>
    <td align="right">46.02</td>
    <td align="right">26.72</td>
    <td align="right">47.89</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.92</td>
    <td align="right">59.20</td>
    <td align="right">25.88</td>
    <td align="right">56.87</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">69.39</td>
    <td align="right">68.82</td>
    <td align="right">39.00</td>
    <td align="right">58.02</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.72</td>
    <td align="right">7.99</td>
    <td align="right">8.17</td>
    <td align="right">14.59</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">11.02</td>
    <td align="right">9.72</td>
    <td align="right">9.84</td>
    <td align="right">17.45</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.51</td>
    <td align="right">10.80</td>
    <td align="right">11.04</td>
    <td align="right">18.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.05</td>
    <td align="right">13.79</td>
    <td align="right">11.32</td>
    <td align="right">18.26</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.09</td>
    <td align="right">16.68</td>
    <td align="right">13.46</td>
    <td align="right">20.58</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">15.25</td>
    <td align="right">16.04</td>
    <td align="right">15.75</td>
    <td align="right">22.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.53</td>
    <td align="right">27.18</td>
    <td align="right">25.55</td>
    <td align="right">32.32</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.45</td>
    <td align="right">35.43</td>
    <td align="right">33.74</td>
    <td align="right">40.64</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.40</td>
    <td align="right">41.62</td>
    <td align="right">41.31</td>
    <td align="right">49.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.66</td>
    <td align="right">36.37</td>
    <td align="right">35.06</td>
    <td align="right">42.60</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">43.05</td>
    <td align="right">43.33</td>
    <td align="right">42.29</td>
    <td align="right">50.57</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">69.38</td>
    <td align="right">67.09</td>
    <td align="right">66.58</td>
    <td align="right">73.59</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.03</td>
    <td align="right">8.80</td>
    <td align="right">13.96</td>
    <td align="right">13.98</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.69</td>
    <td align="right">12.20</td>
    <td align="right">16.84</td>
    <td align="right">16.96</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.32</td>
    <td align="right">14.91</td>
    <td align="right">19.44</td>
    <td align="right">19.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.30</td>
    <td align="right">16.24</td>
    <td align="right">15.78</td>
    <td align="right">19.66</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">13.78</td>
    <td align="right">18.26</td>
    <td align="right">15.79</td>
    <td align="right">19.83</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">15.33</td>
    <td align="right">19.63</td>
    <td align="right">20.01</td>
    <td align="right">22.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.89</td>
    <td align="right">29.14</td>
    <td align="right">22.51</td>
    <td align="right">32.33</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.64</td>
    <td align="right">35.90</td>
    <td align="right">25.95</td>
    <td align="right">36.84</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">40.68</td>
    <td align="right">48.19</td>
    <td align="right">21.53</td>
    <td align="right">41.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">36.01</td>
    <td align="right">46.26</td>
    <td align="right">27.01</td>
    <td align="right">48.34</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">43.02</td>
    <td align="right">59.47</td>
    <td align="right">26.19</td>
    <td align="right">57.18</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">71.99</td>
    <td align="right">70.44</td>
    <td align="right">25.80</td>
    <td align="right">57.93</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.04</td>
    <td align="right">8.24</td>
    <td align="right">8.39</td>
    <td align="right">15.06</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.99</td>
    <td align="right">9.57</td>
    <td align="right">9.84</td>
    <td align="right">17.26</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.32</td>
    <td align="right">11.22</td>
    <td align="right">11.47</td>
    <td align="right">18.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.41</td>
    <td align="right">13.75</td>
    <td align="right">11.34</td>
    <td align="right">18.89</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.00</td>
    <td align="right">16.89</td>
    <td align="right">13.39</td>
    <td align="right">20.71</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">15.35</td>
    <td align="right">16.58</td>
    <td align="right">16.31</td>
    <td align="right">23.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.91</td>
    <td align="right">28.49</td>
    <td align="right">26.60</td>
    <td align="right">33.80</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.52</td>
    <td align="right">35.48</td>
    <td align="right">33.73</td>
    <td align="right">40.39</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">40.89</td>
    <td align="right">42.78</td>
    <td align="right">42.29</td>
    <td align="right">51.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.95</td>
    <td align="right">36.74</td>
    <td align="right">35.61</td>
    <td align="right">43.39</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">43.06</td>
    <td align="right">43.31</td>
    <td align="right">42.35</td>
    <td align="right">50.84</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">72.04</td>
    <td align="right">71.22</td>
    <td align="right">70.56</td>
    <td align="right">77.37</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">74.48</td>
    <td align="right">32.89</td>
    <td align="right">15.07</td>
    <td align="right">31.07</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.91</td>
    <td align="right">53.83</td>
    <td align="right">37.15</td>
    <td align="right">45.83</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.33</td>
    <td align="right">26.84</td>
    <td align="right">26.72</td>
    <td align="right">26.80</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.59</td>
    <td align="right">27.57</td>
    <td align="right">27.31</td>
    <td align="right">27.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.87</td>
    <td align="right">68.22</td>
    <td align="right">39.01</td>
    <td align="right">54.90</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.39</td>
    <td align="right">29.41</td>
    <td align="right">29.27</td>
    <td align="right">29.34</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.09</td>
    <td align="right">29.70</td>
    <td align="right">29.54</td>
    <td align="right">29.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.90</td>
    <td align="right">84.15</td>
    <td align="right">38.16</td>
    <td align="right">62.14</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.41</td>
    <td align="right">30.46</td>
    <td align="right">31.04</td>
    <td align="right">31.73</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">16.96</td>
    <td align="right">31.65</td>
    <td align="right">31.51</td>
    <td align="right">31.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.88</td>
    <td align="right">96.31</td>
    <td align="right">37.86</td>
    <td align="right">69.36</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.66</td>
    <td align="right">33.36</td>
    <td align="right">33.25</td>
    <td align="right">33.31</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.17</td>
    <td align="right">33.13</td>
    <td align="right">33.05</td>
    <td align="right">33.11</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">31.02</td>
    <td align="right">52.93</td>
    <td align="right">53.00</td>
    <td align="right">53.00</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.33</td>
    <td align="right">26.93</td>
    <td align="right">26.67</td>
    <td align="right">26.74</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.57</td>
    <td align="right">27.49</td>
    <td align="right">27.31</td>
    <td align="right">27.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.41</td>
    <td align="right">71.54</td>
    <td align="right">71.61</td>
    <td align="right">71.59</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.30</td>
    <td align="right">29.41</td>
    <td align="right">29.43</td>
    <td align="right">30.00</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.07</td>
    <td align="right">29.89</td>
    <td align="right">29.71</td>
    <td align="right">29.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.61</td>
    <td align="right">82.63</td>
    <td align="right">82.70</td>
    <td align="right">82.68</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.40</td>
    <td align="right">30.47</td>
    <td align="right">30.48</td>
    <td align="right">31.45</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.12</td>
    <td align="right">31.65</td>
    <td align="right">31.50</td>
    <td align="right">31.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.84</td>
    <td align="right">131.57</td>
    <td align="right">131.69</td>
    <td align="right">131.00</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.66</td>
    <td align="right">33.41</td>
    <td align="right">33.30</td>
    <td align="right">33.37</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.24</td>
    <td align="right">33.14</td>
    <td align="right">34.38</td>
    <td align="right">34.43</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.88</td>
    <td align="right">57.02</td>
    <td align="right">37.82</td>
    <td align="right">47.63</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.38</td>
    <td align="right">32.35</td>
    <td align="right">32.06</td>
    <td align="right">32.21</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.66</td>
    <td align="right">33.95</td>
    <td align="right">33.71</td>
    <td align="right">33.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">45.89</td>
    <td align="right">69.45</td>
    <td align="right">40.16</td>
    <td align="right">55.37</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.45</td>
    <td align="right">35.42</td>
    <td align="right">35.22</td>
    <td align="right">35.32</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.11</td>
    <td align="right">34.43</td>
    <td align="right">34.28</td>
    <td align="right">34.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.63</td>
    <td align="right">85.21</td>
    <td align="right">39.09</td>
    <td align="right">63.28</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.53</td>
    <td align="right">35.21</td>
    <td align="right">35.12</td>
    <td align="right">35.19</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.09</td>
    <td align="right">35.94</td>
    <td align="right">35.80</td>
    <td align="right">35.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">71.83</td>
    <td align="right">103.40</td>
    <td align="right">40.12</td>
    <td align="right">72.59</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.79</td>
    <td align="right">36.44</td>
    <td align="right">36.30</td>
    <td align="right">36.37</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.73</td>
    <td align="right">37.52</td>
    <td align="right">37.42</td>
    <td align="right">37.47</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.97</td>
    <td align="right">57.09</td>
    <td align="right">57.14</td>
    <td align="right">57.10</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.34</td>
    <td align="right">32.42</td>
    <td align="right">32.11</td>
    <td align="right">32.24</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.63</td>
    <td align="right">33.84</td>
    <td align="right">33.68</td>
    <td align="right">33.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.37</td>
    <td align="right">80.83</td>
    <td align="right">80.88</td>
    <td align="right">80.86</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.49</td>
    <td align="right">35.38</td>
    <td align="right">35.21</td>
    <td align="right">35.30</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.07</td>
    <td align="right">34.42</td>
    <td align="right">34.35</td>
    <td align="right">34.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.43</td>
    <td align="right">99.53</td>
    <td align="right">99.50</td>
    <td align="right">99.49</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.55</td>
    <td align="right">35.22</td>
    <td align="right">35.11</td>
    <td align="right">35.17</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.08</td>
    <td align="right">35.94</td>
    <td align="right">35.81</td>
    <td align="right">35.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.21</td>
    <td align="right">131.35</td>
    <td align="right">132.41</td>
    <td align="right">132.46</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.78</td>
    <td align="right">38.04</td>
    <td align="right">37.93</td>
    <td align="right">37.99</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.49</td>
    <td align="right">37.54</td>
    <td align="right">37.43</td>
    <td align="right">37.52</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.92</td>
    <td align="right">30.78</td>
    <td align="right">29.14</td>
    <td align="right">32.71</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.27</td>
    <td align="right">32.10</td>
    <td align="right">31.01</td>
    <td align="right">33.79</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.84</td>
    <td align="right">26.25</td>
    <td align="right">32.49</td>
    <td align="right">30.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.68</td>
    <td align="right">34.85</td>
    <td align="right">30.90</td>
    <td align="right">35.74</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.06</td>
    <td align="right">37.51</td>
    <td align="right">35.93</td>
    <td align="right">38.57</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.98</td>
    <td align="right">27.82</td>
    <td align="right">34.17</td>
    <td align="right">30.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.48</td>
    <td align="right">47.70</td>
    <td align="right">32.75</td>
    <td align="right">42.83</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.87</td>
    <td align="right">52.53</td>
    <td align="right">41.59</td>
    <td align="right">47.65</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.23</td>
    <td align="right">30.21</td>
    <td align="right">36.02</td>
    <td align="right">32.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.93</td>
    <td align="right">51.38</td>
    <td align="right">32.07</td>
    <td align="right">44.96</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.56</td>
    <td align="right">60.33</td>
    <td align="right">44.33</td>
    <td align="right">52.68</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.15</td>
    <td align="right">32.54</td>
    <td align="right">37.07</td>
    <td align="right">34.13</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.90</td>
    <td align="right">30.78</td>
    <td align="right">30.62</td>
    <td align="right">30.82</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.26</td>
    <td align="right">32.87</td>
    <td align="right">32.67</td>
    <td align="right">33.18</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.90</td>
    <td align="right">27.53</td>
    <td align="right">27.33</td>
    <td align="right">27.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.47</td>
    <td align="right">33.75</td>
    <td align="right">33.64</td>
    <td align="right">33.68</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.07</td>
    <td align="right">37.75</td>
    <td align="right">37.65</td>
    <td align="right">37.71</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.11</td>
    <td align="right">28.80</td>
    <td align="right">28.63</td>
    <td align="right">28.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.19</td>
    <td align="right">40.20</td>
    <td align="right">40.15</td>
    <td align="right">40.20</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.41</td>
    <td align="right">52.14</td>
    <td align="right">52.13</td>
    <td align="right">52.13</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.17</td>
    <td align="right">32.39</td>
    <td align="right">32.27</td>
    <td align="right">32.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.95</td>
    <td align="right">44.68</td>
    <td align="right">44.59</td>
    <td align="right">44.63</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.60</td>
    <td align="right">61.37</td>
    <td align="right">61.38</td>
    <td align="right">61.36</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.81</td>
    <td align="right">33.79</td>
    <td align="right">33.72</td>
    <td align="right">33.76</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">20.13</td>
    <td align="right">30.74</td>
    <td align="right">29.10</td>
    <td align="right">32.46</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.23</td>
    <td align="right">32.14</td>
    <td align="right">31.01</td>
    <td align="right">33.79</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.99</td>
    <td align="right">26.15</td>
    <td align="right">32.80</td>
    <td align="right">29.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.89</td>
    <td align="right">34.84</td>
    <td align="right">30.53</td>
    <td align="right">35.40</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.01</td>
    <td align="right">37.52</td>
    <td align="right">35.81</td>
    <td align="right">38.21</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.24</td>
    <td align="right">27.78</td>
    <td align="right">34.18</td>
    <td align="right">30.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.88</td>
    <td align="right">48.63</td>
    <td align="right">33.50</td>
    <td align="right">44.05</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.36</td>
    <td align="right">52.67</td>
    <td align="right">41.69</td>
    <td align="right">47.78</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.49</td>
    <td align="right">30.22</td>
    <td align="right">36.20</td>
    <td align="right">33.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.54</td>
    <td align="right">49.84</td>
    <td align="right">31.07</td>
    <td align="right">43.76</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.49</td>
    <td align="right">60.24</td>
    <td align="right">43.72</td>
    <td align="right">52.03</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.86</td>
    <td align="right">32.53</td>
    <td align="right">36.96</td>
    <td align="right">34.08</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.92</td>
    <td align="right">30.72</td>
    <td align="right">30.54</td>
    <td align="right">30.62</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.22</td>
    <td align="right">32.83</td>
    <td align="right">32.63</td>
    <td align="right">32.71</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.94</td>
    <td align="right">27.61</td>
    <td align="right">27.35</td>
    <td align="right">27.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.80</td>
    <td align="right">33.79</td>
    <td align="right">33.65</td>
    <td align="right">33.73</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">36.99</td>
    <td align="right">37.73</td>
    <td align="right">37.64</td>
    <td align="right">37.69</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.15</td>
    <td align="right">28.81</td>
    <td align="right">28.67</td>
    <td align="right">28.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.76</td>
    <td align="right">40.19</td>
    <td align="right">40.15</td>
    <td align="right">40.18</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.88</td>
    <td align="right">52.05</td>
    <td align="right">52.00</td>
    <td align="right">52.00</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.25</td>
    <td align="right">32.38</td>
    <td align="right">32.27</td>
    <td align="right">32.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.53</td>
    <td align="right">44.58</td>
    <td align="right">44.56</td>
    <td align="right">44.61</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.46</td>
    <td align="right">61.02</td>
    <td align="right">61.08</td>
    <td align="right">61.33</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.04</td>
    <td align="right">33.77</td>
    <td align="right">33.70</td>
    <td align="right">33.73</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.42</td>
    <td align="right">27.35</td>
    <td align="right">32.82</td>
    <td align="right">29.97</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.98</td>
    <td align="right">30.71</td>
    <td align="right">29.10</td>
    <td align="right">32.64</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.26</td>
    <td align="right">32.14</td>
    <td align="right">31.04</td>
    <td align="right">33.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.04</td>
    <td align="right">29.97</td>
    <td align="right">35.23</td>
    <td align="right">34.13</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.70</td>
    <td align="right">34.88</td>
    <td align="right">30.45</td>
    <td align="right">35.79</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.06</td>
    <td align="right">37.52</td>
    <td align="right">35.95</td>
    <td align="right">38.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.56</td>
    <td align="right">31.96</td>
    <td align="right">36.19</td>
    <td align="right">33.79</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.42</td>
    <td align="right">46.28</td>
    <td align="right">31.89</td>
    <td align="right">41.68</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.79</td>
    <td align="right">52.58</td>
    <td align="right">41.63</td>
    <td align="right">47.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.83</td>
    <td align="right">34.94</td>
    <td align="right">36.63</td>
    <td align="right">35.89</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.49</td>
    <td align="right">49.99</td>
    <td align="right">31.25</td>
    <td align="right">44.00</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.35</td>
    <td align="right">60.19</td>
    <td align="right">43.69</td>
    <td align="right">52.38</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.50</td>
    <td align="right">26.92</td>
    <td align="right">26.70</td>
    <td align="right">26.83</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.89</td>
    <td align="right">30.72</td>
    <td align="right">30.53</td>
    <td align="right">30.64</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.22</td>
    <td align="right">32.83</td>
    <td align="right">32.64</td>
    <td align="right">32.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.02</td>
    <td align="right">31.10</td>
    <td align="right">30.95</td>
    <td align="right">31.06</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.52</td>
    <td align="right">33.76</td>
    <td align="right">33.61</td>
    <td align="right">33.67</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.11</td>
    <td align="right">37.73</td>
    <td align="right">37.64</td>
    <td align="right">37.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.44</td>
    <td align="right">33.94</td>
    <td align="right">33.83</td>
    <td align="right">33.89</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.22</td>
    <td align="right">40.28</td>
    <td align="right">40.24</td>
    <td align="right">40.37</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.47</td>
    <td align="right">52.21</td>
    <td align="right">52.20</td>
    <td align="right">52.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.86</td>
    <td align="right">37.50</td>
    <td align="right">37.43</td>
    <td align="right">37.48</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.37</td>
    <td align="right">44.48</td>
    <td align="right">44.55</td>
    <td align="right">44.67</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.30</td>
    <td align="right">61.04</td>
    <td align="right">61.04</td>
    <td align="right">61.02</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.61</td>
    <td align="right">27.38</td>
    <td align="right">32.18</td>
    <td align="right">29.82</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.94</td>
    <td align="right">30.80</td>
    <td align="right">29.05</td>
    <td align="right">32.61</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.23</td>
    <td align="right">32.08</td>
    <td align="right">30.99</td>
    <td align="right">33.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.05</td>
    <td align="right">29.93</td>
    <td align="right">36.39</td>
    <td align="right">34.15</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.76</td>
    <td align="right">34.82</td>
    <td align="right">30.56</td>
    <td align="right">35.47</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.03</td>
    <td align="right">37.49</td>
    <td align="right">35.82</td>
    <td align="right">38.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.57</td>
    <td align="right">31.94</td>
    <td align="right">36.20</td>
    <td align="right">35.73</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.85</td>
    <td align="right">47.82</td>
    <td align="right">33.24</td>
    <td align="right">43.39</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.44</td>
    <td align="right">52.61</td>
    <td align="right">41.67</td>
    <td align="right">47.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.74</td>
    <td align="right">34.99</td>
    <td align="right">36.55</td>
    <td align="right">35.81</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.56</td>
    <td align="right">49.83</td>
    <td align="right">31.09</td>
    <td align="right">43.76</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.55</td>
    <td align="right">60.24</td>
    <td align="right">43.88</td>
    <td align="right">52.30</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.53</td>
    <td align="right">26.87</td>
    <td align="right">26.65</td>
    <td align="right">26.76</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.89</td>
    <td align="right">30.73</td>
    <td align="right">30.55</td>
    <td align="right">30.63</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.22</td>
    <td align="right">32.83</td>
    <td align="right">32.63</td>
    <td align="right">33.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.05</td>
    <td align="right">31.10</td>
    <td align="right">30.95</td>
    <td align="right">31.01</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.83</td>
    <td align="right">33.78</td>
    <td align="right">33.64</td>
    <td align="right">33.72</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.02</td>
    <td align="right">37.73</td>
    <td align="right">37.64</td>
    <td align="right">37.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.57</td>
    <td align="right">33.92</td>
    <td align="right">33.82</td>
    <td align="right">33.88</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.75</td>
    <td align="right">40.24</td>
    <td align="right">40.34</td>
    <td align="right">40.38</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.80</td>
    <td align="right">52.08</td>
    <td align="right">52.04</td>
    <td align="right">52.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.85</td>
    <td align="right">37.49</td>
    <td align="right">37.42</td>
    <td align="right">37.46</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.60</td>
    <td align="right">44.65</td>
    <td align="right">44.60</td>
    <td align="right">44.65</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.49</td>
    <td align="right">61.39</td>
    <td align="right">61.42</td>
    <td align="right">61.39</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.32</td>
    <td align="right">31.42</td>
    <td align="right">30.04</td>
    <td align="right">32.84</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.74</td>
    <td align="right">35.18</td>
    <td align="right">37.58</td>
    <td align="right">36.51</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.39</td>
    <td align="right">43.82</td>
    <td align="right">38.16</td>
    <td align="right">42.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.39</td>
    <td align="right">43.08</td>
    <td align="right">30.25</td>
    <td align="right">39.77</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.34</td>
    <td align="right">46.45</td>
    <td align="right">36.66</td>
    <td align="right">43.49</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.01</td>
    <td align="right">51.10</td>
    <td align="right">36.85</td>
    <td align="right">45.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.10</td>
    <td align="right">48.49</td>
    <td align="right">29.86</td>
    <td align="right">44.29</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.52</td>
    <td align="right">53.16</td>
    <td align="right">37.70</td>
    <td align="right">46.89</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.36</td>
    <td align="right">55.41</td>
    <td align="right">33.92</td>
    <td align="right">46.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.30</td>
    <td align="right">53.24</td>
    <td align="right">31.09</td>
    <td align="right">47.15</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.35</td>
    <td align="right">56.42</td>
    <td align="right">37.59</td>
    <td align="right">48.80</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">60.94</td>
    <td align="right">71.11</td>
    <td align="right">38.01</td>
    <td align="right">58.36</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.35</td>
    <td align="right">30.58</td>
    <td align="right">30.33</td>
    <td align="right">30.44</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.74</td>
    <td align="right">36.50</td>
    <td align="right">36.36</td>
    <td align="right">36.43</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">30.12</td>
    <td align="right">39.38</td>
    <td align="right">39.41</td>
    <td align="right">39.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.41</td>
    <td align="right">37.14</td>
    <td align="right">37.07</td>
    <td align="right">37.11</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.31</td>
    <td align="right">43.73</td>
    <td align="right">43.63</td>
    <td align="right">43.70</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.46</td>
    <td align="right">49.84</td>
    <td align="right">49.58</td>
    <td align="right">50.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.04</td>
    <td align="right">44.85</td>
    <td align="right">44.77</td>
    <td align="right">44.82</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.51</td>
    <td align="right">52.99</td>
    <td align="right">53.46</td>
    <td align="right">53.57</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.43</td>
    <td align="right">52.53</td>
    <td align="right">52.02</td>
    <td align="right">51.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.27</td>
    <td align="right">50.11</td>
    <td align="right">50.04</td>
    <td align="right">50.08</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.41</td>
    <td align="right">56.23</td>
    <td align="right">56.18</td>
    <td align="right">56.29</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">60.50</td>
    <td align="right">72.00</td>
    <td align="right">71.89</td>
    <td align="right">71.95</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.53</td>
    <td align="right">31.48</td>
    <td align="right">30.00</td>
    <td align="right">32.94</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.17</td>
    <td align="right">35.23</td>
    <td align="right">38.18</td>
    <td align="right">37.63</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.35</td>
    <td align="right">43.08</td>
    <td align="right">35.48</td>
    <td align="right">39.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.40</td>
    <td align="right">43.15</td>
    <td align="right">30.22</td>
    <td align="right">39.89</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.32</td>
    <td align="right">46.47</td>
    <td align="right">36.68</td>
    <td align="right">43.52</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">41.02</td>
    <td align="right">50.61</td>
    <td align="right">37.09</td>
    <td align="right">45.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.10</td>
    <td align="right">48.38</td>
    <td align="right">30.01</td>
    <td align="right">44.93</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.51</td>
    <td align="right">53.01</td>
    <td align="right">38.25</td>
    <td align="right">47.04</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">43.83</td>
    <td align="right">54.99</td>
    <td align="right">33.94</td>
    <td align="right">46.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.29</td>
    <td align="right">52.95</td>
    <td align="right">31.33</td>
    <td align="right">45.64</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.33</td>
    <td align="right">56.38</td>
    <td align="right">37.58</td>
    <td align="right">48.75</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">61.04</td>
    <td align="right">70.74</td>
    <td align="right">36.47</td>
    <td align="right">56.36</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.40</td>
    <td align="right">30.51</td>
    <td align="right">30.26</td>
    <td align="right">30.39</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.13</td>
    <td align="right">36.52</td>
    <td align="right">36.40</td>
    <td align="right">36.45</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.40</td>
    <td align="right">39.48</td>
    <td align="right">39.52</td>
    <td align="right">39.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.38</td>
    <td align="right">37.15</td>
    <td align="right">37.05</td>
    <td align="right">37.10</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.23</td>
    <td align="right">43.69</td>
    <td align="right">43.59</td>
    <td align="right">43.68</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.01</td>
    <td align="right">50.46</td>
    <td align="right">50.76</td>
    <td align="right">50.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.12</td>
    <td align="right">44.96</td>
    <td align="right">44.89</td>
    <td align="right">44.94</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.46</td>
    <td align="right">52.77</td>
    <td align="right">52.80</td>
    <td align="right">53.54</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">43.83</td>
    <td align="right">54.73</td>
    <td align="right">51.75</td>
    <td align="right">51.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.27</td>
    <td align="right">49.99</td>
    <td align="right">49.82</td>
    <td align="right">49.93</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.40</td>
    <td align="right">56.22</td>
    <td align="right">56.16</td>
    <td align="right">56.21</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">61.56</td>
    <td align="right">71.24</td>
    <td align="right">71.16</td>
    <td align="right">71.47</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">108.20</td>
    <td align="right">126.92</td>
    <td align="right">29.49</td>
    <td align="right">92.63</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">40.50</td>
    <td align="right">69.74</td>
    <td align="right">44.19</td>
    <td align="right">58.11</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.05</td>
    <td align="right">33.58</td>
    <td align="right">33.15</td>
    <td align="right">33.34</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">15.53</td>
    <td align="right">32.50</td>
    <td align="right">33.41</td>
    <td align="right">33.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">104.18</td>
    <td align="right">125.35</td>
    <td align="right">54.37</td>
    <td align="right">90.66</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.80</td>
    <td align="right">46.19</td>
    <td align="right">44.16</td>
    <td align="right">45.12</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.12</td>
    <td align="right">45.57</td>
    <td align="right">43.25</td>
    <td align="right">44.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">191.58</td>
    <td align="right">252.57</td>
    <td align="right">72.88</td>
    <td align="right">164.16</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.92</td>
    <td align="right">61.81</td>
    <td align="right">58.91</td>
    <td align="right">60.34</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.83</td>
    <td align="right">65.92</td>
    <td align="right">63.13</td>
    <td align="right">64.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">298.47</td>
    <td align="right">360.64</td>
    <td align="right">90.74</td>
    <td align="right">229.15</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.27</td>
    <td align="right">76.78</td>
    <td align="right">74.31</td>
    <td align="right">75.58</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">48.55</td>
    <td align="right">80.82</td>
    <td align="right">78.80</td>
    <td align="right">80.06</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">33.25</td>
    <td align="right">54.91</td>
    <td align="right">54.89</td>
    <td align="right">54.89</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.65</td>
    <td align="right">32.59</td>
    <td align="right">32.03</td>
    <td align="right">32.27</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.36</td>
    <td align="right">34.56</td>
    <td align="right">34.47</td>
    <td align="right">35.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">100.73</td>
    <td align="right">127.24</td>
    <td align="right">126.02</td>
    <td align="right">126.47</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.16</td>
    <td align="right">45.72</td>
    <td align="right">44.24</td>
    <td align="right">45.56</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">27.32</td>
    <td align="right">46.38</td>
    <td align="right">44.29</td>
    <td align="right">45.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">190.82</td>
    <td align="right">190.71</td>
    <td align="right">190.10</td>
    <td align="right">190.50</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.25</td>
    <td align="right">60.63</td>
    <td align="right">58.10</td>
    <td align="right">60.30</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.98</td>
    <td align="right">64.31</td>
    <td align="right">61.99</td>
    <td align="right">63.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">298.54</td>
    <td align="right">444.62</td>
    <td align="right">443.08</td>
    <td align="right">444.16</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">46.98</td>
    <td align="right">76.72</td>
    <td align="right">74.29</td>
    <td align="right">75.60</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.80</td>
    <td align="right">80.26</td>
    <td align="right">78.56</td>
    <td align="right">79.86</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">41.78</td>
    <td align="right">73.66</td>
    <td align="right">45.33</td>
    <td align="right">60.13</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.68</td>
    <td align="right">37.11</td>
    <td align="right">36.77</td>
    <td align="right">36.87</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">15.52</td>
    <td align="right">38.39</td>
    <td align="right">38.15</td>
    <td align="right">38.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">93.73</td>
    <td align="right">113.94</td>
    <td align="right">52.17</td>
    <td align="right">83.78</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.51</td>
    <td align="right">53.68</td>
    <td align="right">51.31</td>
    <td align="right">52.38</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">25.26</td>
    <td align="right">50.72</td>
    <td align="right">48.41</td>
    <td align="right">49.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">191.73</td>
    <td align="right">248.85</td>
    <td align="right">74.47</td>
    <td align="right">163.17</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.12</td>
    <td align="right">66.60</td>
    <td align="right">64.01</td>
    <td align="right">65.35</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.73</td>
    <td align="right">68.51</td>
    <td align="right">65.98</td>
    <td align="right">67.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.89</td>
    <td align="right">365.90</td>
    <td align="right">89.63</td>
    <td align="right">229.24</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.43</td>
    <td align="right">80.01</td>
    <td align="right">77.64</td>
    <td align="right">78.91</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.73</td>
    <td align="right">84.25</td>
    <td align="right">81.90</td>
    <td align="right">83.13</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">41.92</td>
    <td align="right">68.52</td>
    <td align="right">68.28</td>
    <td align="right">68.43</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.50</td>
    <td align="right">39.71</td>
    <td align="right">39.27</td>
    <td align="right">39.49</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.52</td>
    <td align="right">41.23</td>
    <td align="right">40.62</td>
    <td align="right">40.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">99.56</td>
    <td align="right">133.62</td>
    <td align="right">132.47</td>
    <td align="right">133.12</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.57</td>
    <td align="right">52.27</td>
    <td align="right">50.27</td>
    <td align="right">51.31</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.82</td>
    <td align="right">51.90</td>
    <td align="right">49.84</td>
    <td align="right">50.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">191.45</td>
    <td align="right">220.66</td>
    <td align="right">219.56</td>
    <td align="right">220.24</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.64</td>
    <td align="right">67.32</td>
    <td align="right">64.41</td>
    <td align="right">65.98</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.59</td>
    <td align="right">68.75</td>
    <td align="right">65.95</td>
    <td align="right">67.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">299.23</td>
    <td align="right">444.07</td>
    <td align="right">442.67</td>
    <td align="right">443.17</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.07</td>
    <td align="right">79.88</td>
    <td align="right">77.38</td>
    <td align="right">78.72</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.85</td>
    <td align="right">84.08</td>
    <td align="right">81.89</td>
    <td align="right">82.92</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.12</td>
    <td align="right">38.37</td>
    <td align="right">32.21</td>
    <td align="right">39.81</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.78</td>
    <td align="right">39.83</td>
    <td align="right">35.52</td>
    <td align="right">43.04</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.60</td>
    <td align="right">33.35</td>
    <td align="right">39.25</td>
    <td align="right">36.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">38.75</td>
    <td align="right">50.77</td>
    <td align="right">38.93</td>
    <td align="right">49.87</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.83</td>
    <td align="right">58.50</td>
    <td align="right">47.59</td>
    <td align="right">57.95</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.58</td>
    <td align="right">45.02</td>
    <td align="right">49.60</td>
    <td align="right">46.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.47</td>
    <td align="right">82.15</td>
    <td align="right">50.82</td>
    <td align="right">73.71</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.85</td>
    <td align="right">87.45</td>
    <td align="right">68.62</td>
    <td align="right">81.26</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.49</td>
    <td align="right">66.52</td>
    <td align="right">65.51</td>
    <td align="right">64.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.20</td>
    <td align="right">103.80</td>
    <td align="right">59.21</td>
    <td align="right">92.13</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">133.05</td>
    <td align="right">112.92</td>
    <td align="right">90.29</td>
    <td align="right">102.12</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.40</td>
    <td align="right">83.55</td>
    <td align="right">77.00</td>
    <td align="right">78.32</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.68</td>
    <td align="right">37.35</td>
    <td align="right">37.10</td>
    <td align="right">37.31</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">31.05</td>
    <td align="right">40.32</td>
    <td align="right">39.73</td>
    <td align="right">39.96</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.18</td>
    <td align="right">33.94</td>
    <td align="right">33.49</td>
    <td align="right">33.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.93</td>
    <td align="right">47.65</td>
    <td align="right">45.51</td>
    <td align="right">46.43</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">55.27</td>
    <td align="right">59.91</td>
    <td align="right">57.11</td>
    <td align="right">58.39</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">24.50</td>
    <td align="right">45.15</td>
    <td align="right">42.88</td>
    <td align="right">44.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.79</td>
    <td align="right">78.55</td>
    <td align="right">76.31</td>
    <td align="right">77.65</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.22</td>
    <td align="right">87.75</td>
    <td align="right">86.57</td>
    <td align="right">87.19</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.12</td>
    <td align="right">69.32</td>
    <td align="right">65.83</td>
    <td align="right">67.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.90</td>
    <td align="right">97.71</td>
    <td align="right">96.38</td>
    <td align="right">97.01</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.41</td>
    <td align="right">112.78</td>
    <td align="right">112.44</td>
    <td align="right">112.86</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.02</td>
    <td align="right">87.02</td>
    <td align="right">84.45</td>
    <td align="right">85.77</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.40</td>
    <td align="right">38.56</td>
    <td align="right">34.64</td>
    <td align="right">41.65</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.92</td>
    <td align="right">37.40</td>
    <td align="right">35.01</td>
    <td align="right">41.58</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">14.14</td>
    <td align="right">30.87</td>
    <td align="right">37.57</td>
    <td align="right">35.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">42.25</td>
    <td align="right">52.63</td>
    <td align="right">41.03</td>
    <td align="right">52.22</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.68</td>
    <td align="right">59.50</td>
    <td align="right">48.20</td>
    <td align="right">57.86</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">24.37</td>
    <td align="right">43.62</td>
    <td align="right">48.01</td>
    <td align="right">45.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.10</td>
    <td align="right">83.85</td>
    <td align="right">50.80</td>
    <td align="right">75.31</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.71</td>
    <td align="right">88.09</td>
    <td align="right">69.18</td>
    <td align="right">81.30</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.56</td>
    <td align="right">66.49</td>
    <td align="right">65.66</td>
    <td align="right">65.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.36</td>
    <td align="right">102.82</td>
    <td align="right">57.78</td>
    <td align="right">90.60</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.34</td>
    <td align="right">114.01</td>
    <td align="right">91.92</td>
    <td align="right">104.36</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.54</td>
    <td align="right">83.59</td>
    <td align="right">76.99</td>
    <td align="right">78.23</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.23</td>
    <td align="right">36.95</td>
    <td align="right">36.33</td>
    <td align="right">36.66</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.98</td>
    <td align="right">39.23</td>
    <td align="right">38.72</td>
    <td align="right">39.05</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.53</td>
    <td align="right">34.18</td>
    <td align="right">33.70</td>
    <td align="right">33.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.48</td>
    <td align="right">49.37</td>
    <td align="right">47.36</td>
    <td align="right">48.26</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.57</td>
    <td align="right">58.44</td>
    <td align="right">55.34</td>
    <td align="right">57.11</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.57</td>
    <td align="right">44.46</td>
    <td align="right">42.34</td>
    <td align="right">43.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.00</td>
    <td align="right">78.27</td>
    <td align="right">76.42</td>
    <td align="right">77.62</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.89</td>
    <td align="right">88.95</td>
    <td align="right">87.77</td>
    <td align="right">88.36</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.76</td>
    <td align="right">71.19</td>
    <td align="right">67.86</td>
    <td align="right">69.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.39</td>
    <td align="right">99.19</td>
    <td align="right">97.99</td>
    <td align="right">98.56</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.13</td>
    <td align="right">114.56</td>
    <td align="right">114.02</td>
    <td align="right">114.46</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.03</td>
    <td align="right">88.57</td>
    <td align="right">86.21</td>
    <td align="right">87.53</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">17.28</td>
    <td align="right">34.10</td>
    <td align="right">39.32</td>
    <td align="right">36.72</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.40</td>
    <td align="right">37.35</td>
    <td align="right">31.63</td>
    <td align="right">39.12</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.82</td>
    <td align="right">38.57</td>
    <td align="right">33.77</td>
    <td align="right">40.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.74</td>
    <td align="right">49.03</td>
    <td align="right">51.92</td>
    <td align="right">49.97</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.04</td>
    <td align="right">47.70</td>
    <td align="right">37.33</td>
    <td align="right">47.01</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">56.87</td>
    <td align="right">61.43</td>
    <td align="right">49.67</td>
    <td align="right">60.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.96</td>
    <td align="right">69.53</td>
    <td align="right">67.54</td>
    <td align="right">69.38</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.78</td>
    <td align="right">83.62</td>
    <td align="right">52.24</td>
    <td align="right">74.96</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.49</td>
    <td align="right">87.83</td>
    <td align="right">69.17</td>
    <td align="right">81.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.89</td>
    <td align="right">89.04</td>
    <td align="right">82.93</td>
    <td align="right">85.23</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.26</td>
    <td align="right">104.93</td>
    <td align="right">59.88</td>
    <td align="right">95.32</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">133.62</td>
    <td align="right">113.07</td>
    <td align="right">90.22</td>
    <td align="right">103.44</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">16.88</td>
    <td align="right">33.77</td>
    <td align="right">33.30</td>
    <td align="right">33.46</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.94</td>
    <td align="right">37.75</td>
    <td align="right">37.37</td>
    <td align="right">37.57</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.40</td>
    <td align="right">38.31</td>
    <td align="right">37.78</td>
    <td align="right">38.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.24</td>
    <td align="right">49.24</td>
    <td align="right">47.02</td>
    <td align="right">48.17</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.51</td>
    <td align="right">50.69</td>
    <td align="right">48.49</td>
    <td align="right">49.68</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.40</td>
    <td align="right">59.03</td>
    <td align="right">56.07</td>
    <td align="right">57.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.44</td>
    <td align="right">72.13</td>
    <td align="right">69.08</td>
    <td align="right">70.81</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.32</td>
    <td align="right">77.25</td>
    <td align="right">75.36</td>
    <td align="right">76.48</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.50</td>
    <td align="right">86.62</td>
    <td align="right">85.19</td>
    <td align="right">85.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.56</td>
    <td align="right">91.53</td>
    <td align="right">90.06</td>
    <td align="right">90.90</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.73</td>
    <td align="right">99.60</td>
    <td align="right">97.25</td>
    <td align="right">97.29</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.20</td>
    <td align="right">114.07</td>
    <td align="right">113.28</td>
    <td align="right">113.56</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">16.51</td>
    <td align="right">33.25</td>
    <td align="right">37.81</td>
    <td align="right">35.58</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">22.76</td>
    <td align="right">36.67</td>
    <td align="right">33.29</td>
    <td align="right">38.38</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">31.10</td>
    <td align="right">40.25</td>
    <td align="right">35.92</td>
    <td align="right">41.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">29.59</td>
    <td align="right">47.58</td>
    <td align="right">51.12</td>
    <td align="right">50.23</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.68</td>
    <td align="right">50.80</td>
    <td align="right">39.34</td>
    <td align="right">50.21</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">57.19</td>
    <td align="right">57.52</td>
    <td align="right">48.41</td>
    <td align="right">55.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.34</td>
    <td align="right">69.66</td>
    <td align="right">69.55</td>
    <td align="right">68.55</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.69</td>
    <td align="right">84.79</td>
    <td align="right">51.74</td>
    <td align="right">73.46</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.18</td>
    <td align="right">88.58</td>
    <td align="right">69.48</td>
    <td align="right">81.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">83.10</td>
    <td align="right">89.54</td>
    <td align="right">83.29</td>
    <td align="right">85.64</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.48</td>
    <td align="right">102.06</td>
    <td align="right">57.22</td>
    <td align="right">90.46</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.07</td>
    <td align="right">115.94</td>
    <td align="right">91.50</td>
    <td align="right">103.34</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">15.33</td>
    <td align="right">31.37</td>
    <td align="right">30.89</td>
    <td align="right">31.08</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">22.08</td>
    <td align="right">35.39</td>
    <td align="right">35.08</td>
    <td align="right">35.21</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.64</td>
    <td align="right">40.02</td>
    <td align="right">39.76</td>
    <td align="right">40.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">29.99</td>
    <td align="right">49.21</td>
    <td align="right">46.88</td>
    <td align="right">48.01</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.40</td>
    <td align="right">49.80</td>
    <td align="right">47.83</td>
    <td align="right">48.76</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.75</td>
    <td align="right">58.55</td>
    <td align="right">55.36</td>
    <td align="right">56.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.54</td>
    <td align="right">70.99</td>
    <td align="right">67.71</td>
    <td align="right">69.43</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.57</td>
    <td align="right">78.14</td>
    <td align="right">76.00</td>
    <td align="right">76.95</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.85</td>
    <td align="right">86.49</td>
    <td align="right">85.15</td>
    <td align="right">85.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.41</td>
    <td align="right">91.51</td>
    <td align="right">90.00</td>
    <td align="right">90.93</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.37</td>
    <td align="right">97.34</td>
    <td align="right">95.98</td>
    <td align="right">96.68</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.06</td>
    <td align="right">114.10</td>
    <td align="right">113.37</td>
    <td align="right">114.28</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.73</td>
    <td align="right">38.42</td>
    <td align="right">33.29</td>
    <td align="right">39.48</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.72</td>
    <td align="right">42.22</td>
    <td align="right">42.07</td>
    <td align="right">43.40</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">36.95</td>
    <td align="right">51.64</td>
    <td align="right">42.13</td>
    <td align="right">48.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.84</td>
    <td align="right">59.29</td>
    <td align="right">39.59</td>
    <td align="right">56.01</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">59.41</td>
    <td align="right">68.42</td>
    <td align="right">49.23</td>
    <td align="right">63.97</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">66.41</td>
    <td align="right">77.54</td>
    <td align="right">48.11</td>
    <td align="right">66.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.61</td>
    <td align="right">80.43</td>
    <td align="right">49.04</td>
    <td align="right">74.66</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">85.92</td>
    <td align="right">94.17</td>
    <td align="right">61.96</td>
    <td align="right">84.24</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">90.63</td>
    <td align="right">101.45</td>
    <td align="right">45.81</td>
    <td align="right">82.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.99</td>
    <td align="right">96.02</td>
    <td align="right">59.08</td>
    <td align="right">89.15</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">103.53</td>
    <td align="right">109.92</td>
    <td align="right">69.31</td>
    <td align="right">97.41</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.56</td>
    <td align="right">156.20</td>
    <td align="right">53.63</td>
    <td align="right">119.88</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.45</td>
    <td align="right">37.04</td>
    <td align="right">36.65</td>
    <td align="right">36.89</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">37.98</td>
    <td align="right">43.81</td>
    <td align="right">43.10</td>
    <td align="right">43.45</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">38.25</td>
    <td align="right">47.77</td>
    <td align="right">47.42</td>
    <td align="right">47.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.43</td>
    <td align="right">49.39</td>
    <td align="right">47.17</td>
    <td align="right">48.20</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">59.77</td>
    <td align="right">65.47</td>
    <td align="right">62.48</td>
    <td align="right">63.88</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">63.62</td>
    <td align="right">71.74</td>
    <td align="right">71.23</td>
    <td align="right">71.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.97</td>
    <td align="right">76.78</td>
    <td align="right">74.00</td>
    <td align="right">75.44</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.74</td>
    <td align="right">94.84</td>
    <td align="right">92.64</td>
    <td align="right">93.90</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">90.36</td>
    <td align="right">101.69</td>
    <td align="right">101.16</td>
    <td align="right">101.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">85.36</td>
    <td align="right">93.82</td>
    <td align="right">91.89</td>
    <td align="right">98.94</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.52</td>
    <td align="right">111.17</td>
    <td align="right">108.82</td>
    <td align="right">110.04</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.03</td>
    <td align="right">154.21</td>
    <td align="right">154.00</td>
    <td align="right">154.00</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.87</td>
    <td align="right">38.33</td>
    <td align="right">33.22</td>
    <td align="right">39.61</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">37.11</td>
    <td align="right">42.81</td>
    <td align="right">43.31</td>
    <td align="right">44.45</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">34.48</td>
    <td align="right">48.35</td>
    <td align="right">40.68</td>
    <td align="right">46.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.87</td>
    <td align="right">60.28</td>
    <td align="right">40.57</td>
    <td align="right">57.18</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">61.01</td>
    <td align="right">69.58</td>
    <td align="right">49.97</td>
    <td align="right">64.16</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">63.44</td>
    <td align="right">74.85</td>
    <td align="right">47.26</td>
    <td align="right">63.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.29</td>
    <td align="right">83.74</td>
    <td align="right">51.47</td>
    <td align="right">77.83</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">86.64</td>
    <td align="right">93.39</td>
    <td align="right">62.08</td>
    <td align="right">83.31</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">90.74</td>
    <td align="right">102.86</td>
    <td align="right">46.61</td>
    <td align="right">83.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.56</td>
    <td align="right">95.79</td>
    <td align="right">59.22</td>
    <td align="right">88.68</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">103.66</td>
    <td align="right">110.15</td>
    <td align="right">69.89</td>
    <td align="right">99.15</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.35</td>
    <td align="right">156.22</td>
    <td align="right">55.90</td>
    <td align="right">119.36</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">20.81</td>
    <td align="right">35.60</td>
    <td align="right">35.27</td>
    <td align="right">35.51</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">37.30</td>
    <td align="right">43.25</td>
    <td align="right">42.65</td>
    <td align="right">42.87</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">35.79</td>
    <td align="right">45.17</td>
    <td align="right">45.22</td>
    <td align="right">45.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.68</td>
    <td align="right">48.85</td>
    <td align="right">46.59</td>
    <td align="right">48.97</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">61.71</td>
    <td align="right">66.25</td>
    <td align="right">63.66</td>
    <td align="right">64.96</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">65.54</td>
    <td align="right">74.92</td>
    <td align="right">74.60</td>
    <td align="right">74.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">66.35</td>
    <td align="right">76.50</td>
    <td align="right">73.78</td>
    <td align="right">75.01</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.00</td>
    <td align="right">93.35</td>
    <td align="right">90.32</td>
    <td align="right">91.97</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">90.16</td>
    <td align="right">101.22</td>
    <td align="right">100.79</td>
    <td align="right">101.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">84.11</td>
    <td align="right">93.50</td>
    <td align="right">91.26</td>
    <td align="right">92.27</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.90</td>
    <td align="right">113.09</td>
    <td align="right">110.53</td>
    <td align="right">111.82</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.11</td>
    <td align="right">151.98</td>
    <td align="right">150.50</td>
    <td align="right">150.45</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">78.99</td>
    <td align="right">17.12</td>
    <td align="right">9.55</td>
    <td align="right">20.79</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.55</td>
    <td align="right">44.08</td>
    <td align="right">31.46</td>
    <td align="right">39.47</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.46</td>
    <td align="right">23.65</td>
    <td align="right">23.41</td>
    <td align="right">23.53</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.85</td>
    <td align="right">28.12</td>
    <td align="right">27.91</td>
    <td align="right">28.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.72</td>
    <td align="right">60.12</td>
    <td align="right">33.11</td>
    <td align="right">48.08</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.18</td>
    <td align="right">29.71</td>
    <td align="right">29.54</td>
    <td align="right">29.61</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.22</td>
    <td align="right">30.99</td>
    <td align="right">30.85</td>
    <td align="right">30.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.44</td>
    <td align="right">61.65</td>
    <td align="right">33.22</td>
    <td align="right">48.99</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.60</td>
    <td align="right">32.32</td>
    <td align="right">32.19</td>
    <td align="right">31.71</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.04</td>
    <td align="right">33.34</td>
    <td align="right">33.26</td>
    <td align="right">33.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">61.43</td>
    <td align="right">77.21</td>
    <td align="right">33.81</td>
    <td align="right">56.87</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.18</td>
    <td align="right">34.25</td>
    <td align="right">33.83</td>
    <td align="right">33.96</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.04</td>
    <td align="right">36.37</td>
    <td align="right">36.27</td>
    <td align="right">36.36</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.69</td>
    <td align="right">41.69</td>
    <td align="right">41.69</td>
    <td align="right">41.68</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.46</td>
    <td align="right">24.14</td>
    <td align="right">23.37</td>
    <td align="right">23.51</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.87</td>
    <td align="right">28.14</td>
    <td align="right">27.90</td>
    <td align="right">28.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.91</td>
    <td align="right">61.31</td>
    <td align="right">61.38</td>
    <td align="right">61.51</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.02</td>
    <td align="right">29.66</td>
    <td align="right">29.57</td>
    <td align="right">29.61</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.21</td>
    <td align="right">30.95</td>
    <td align="right">30.83</td>
    <td align="right">30.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.26</td>
    <td align="right">69.74</td>
    <td align="right">70.32</td>
    <td align="right">70.58</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.61</td>
    <td align="right">31.94</td>
    <td align="right">32.15</td>
    <td align="right">31.75</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.10</td>
    <td align="right">33.36</td>
    <td align="right">33.55</td>
    <td align="right">33.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">63.27</td>
    <td align="right">86.78</td>
    <td align="right">86.76</td>
    <td align="right">86.89</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.22</td>
    <td align="right">34.24</td>
    <td align="right">34.01</td>
    <td align="right">33.88</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.06</td>
    <td align="right">36.36</td>
    <td align="right">36.26</td>
    <td align="right">36.31</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.55</td>
    <td align="right">45.10</td>
    <td align="right">31.37</td>
    <td align="right">39.18</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.46</td>
    <td align="right">23.62</td>
    <td align="right">23.38</td>
    <td align="right">23.49</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.84</td>
    <td align="right">28.10</td>
    <td align="right">27.90</td>
    <td align="right">27.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.66</td>
    <td align="right">60.28</td>
    <td align="right">33.28</td>
    <td align="right">48.32</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.16</td>
    <td align="right">29.69</td>
    <td align="right">29.56</td>
    <td align="right">29.64</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.24</td>
    <td align="right">30.94</td>
    <td align="right">30.82</td>
    <td align="right">30.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.45</td>
    <td align="right">61.73</td>
    <td align="right">32.97</td>
    <td align="right">48.95</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.56</td>
    <td align="right">32.33</td>
    <td align="right">31.64</td>
    <td align="right">31.71</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.04</td>
    <td align="right">33.68</td>
    <td align="right">33.55</td>
    <td align="right">33.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">66.97</td>
    <td align="right">77.15</td>
    <td align="right">33.67</td>
    <td align="right">57.37</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.20</td>
    <td align="right">34.24</td>
    <td align="right">33.85</td>
    <td align="right">33.89</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.06</td>
    <td align="right">36.03</td>
    <td align="right">35.94</td>
    <td align="right">36.35</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.44</td>
    <td align="right">41.60</td>
    <td align="right">41.60</td>
    <td align="right">41.58</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.45</td>
    <td align="right">23.60</td>
    <td align="right">23.35</td>
    <td align="right">23.47</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.81</td>
    <td align="right">28.16</td>
    <td align="right">27.93</td>
    <td align="right">28.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.80</td>
    <td align="right">61.45</td>
    <td align="right">61.52</td>
    <td align="right">61.49</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.15</td>
    <td align="right">29.69</td>
    <td align="right">29.52</td>
    <td align="right">29.60</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.20</td>
    <td align="right">30.97</td>
    <td align="right">30.82</td>
    <td align="right">30.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.40</td>
    <td align="right">70.01</td>
    <td align="right">70.44</td>
    <td align="right">70.43</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.72</td>
    <td align="right">32.31</td>
    <td align="right">31.65</td>
    <td align="right">31.72</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.10</td>
    <td align="right">33.34</td>
    <td align="right">33.50</td>
    <td align="right">33.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">64.36</td>
    <td align="right">82.64</td>
    <td align="right">83.59</td>
    <td align="right">84.22</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.18</td>
    <td align="right">33.94</td>
    <td align="right">34.00</td>
    <td align="right">34.07</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.03</td>
    <td align="right">36.37</td>
    <td align="right">35.93</td>
    <td align="right">35.97</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.07</td>
    <td align="right">25.72</td>
    <td align="right">25.26</td>
    <td align="right">27.96</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.02</td>
    <td align="right">25.67</td>
    <td align="right">25.46</td>
    <td align="right">27.73</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.98</td>
    <td align="right">22.27</td>
    <td align="right">20.08</td>
    <td align="right">25.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.66</td>
    <td align="right">29.70</td>
    <td align="right">26.83</td>
    <td align="right">31.07</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.57</td>
    <td align="right">30.50</td>
    <td align="right">26.92</td>
    <td align="right">31.18</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.94</td>
    <td align="right">24.74</td>
    <td align="right">22.29</td>
    <td align="right">27.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.12</td>
    <td align="right">40.71</td>
    <td align="right">27.81</td>
    <td align="right">36.73</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.59</td>
    <td align="right">41.90</td>
    <td align="right">28.04</td>
    <td align="right">37.20</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.81</td>
    <td align="right">27.22</td>
    <td align="right">23.68</td>
    <td align="right">29.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.53</td>
    <td align="right">44.20</td>
    <td align="right">27.28</td>
    <td align="right">38.86</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.38</td>
    <td align="right">48.73</td>
    <td align="right">28.15</td>
    <td align="right">40.92</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.09</td>
    <td align="right">28.37</td>
    <td align="right">23.00</td>
    <td align="right">30.52</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.05</td>
    <td align="right">28.19</td>
    <td align="right">28.02</td>
    <td align="right">28.12</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.03</td>
    <td align="right">28.51</td>
    <td align="right">28.29</td>
    <td align="right">28.39</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.97</td>
    <td align="right">23.92</td>
    <td align="right">23.68</td>
    <td align="right">23.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">33.59</td>
    <td align="right">33.44</td>
    <td align="right">33.52</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.59</td>
    <td align="right">31.62</td>
    <td align="right">31.61</td>
    <td align="right">31.57</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.93</td>
    <td align="right">26.11</td>
    <td align="right">25.94</td>
    <td align="right">26.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.15</td>
    <td align="right">39.49</td>
    <td align="right">39.44</td>
    <td align="right">39.48</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.58</td>
    <td align="right">39.19</td>
    <td align="right">39.11</td>
    <td align="right">39.14</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.81</td>
    <td align="right">28.92</td>
    <td align="right">28.82</td>
    <td align="right">28.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.55</td>
    <td align="right">42.18</td>
    <td align="right">42.15</td>
    <td align="right">42.15</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.45</td>
    <td align="right">46.18</td>
    <td align="right">46.15</td>
    <td align="right">46.17</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.11</td>
    <td align="right">30.28</td>
    <td align="right">30.22</td>
    <td align="right">30.26</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.02</td>
    <td align="right">26.14</td>
    <td align="right">26.62</td>
    <td align="right">28.21</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.17</td>
    <td align="right">25.47</td>
    <td align="right">25.29</td>
    <td align="right">27.65</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.55</td>
    <td align="right">22.21</td>
    <td align="right">20.69</td>
    <td align="right">25.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.70</td>
    <td align="right">30.27</td>
    <td align="right">27.88</td>
    <td align="right">31.03</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.18</td>
    <td align="right">30.71</td>
    <td align="right">27.11</td>
    <td align="right">31.10</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.93</td>
    <td align="right">24.79</td>
    <td align="right">22.53</td>
    <td align="right">28.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.98</td>
    <td align="right">42.52</td>
    <td align="right">28.88</td>
    <td align="right">37.72</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.49</td>
    <td align="right">41.85</td>
    <td align="right">28.08</td>
    <td align="right">37.16</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.89</td>
    <td align="right">27.97</td>
    <td align="right">24.23</td>
    <td align="right">30.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.47</td>
    <td align="right">45.91</td>
    <td align="right">27.63</td>
    <td align="right">39.91</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.26</td>
    <td align="right">48.59</td>
    <td align="right">28.13</td>
    <td align="right">40.70</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.05</td>
    <td align="right">29.04</td>
    <td align="right">23.88</td>
    <td align="right">31.17</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.02</td>
    <td align="right">27.93</td>
    <td align="right">27.74</td>
    <td align="right">27.84</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.17</td>
    <td align="right">28.48</td>
    <td align="right">28.29</td>
    <td align="right">28.38</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.57</td>
    <td align="right">23.98</td>
    <td align="right">23.71</td>
    <td align="right">23.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">33.60</td>
    <td align="right">33.45</td>
    <td align="right">33.53</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.16</td>
    <td align="right">31.58</td>
    <td align="right">31.44</td>
    <td align="right">31.54</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.91</td>
    <td align="right">26.08</td>
    <td align="right">25.93</td>
    <td align="right">26.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.98</td>
    <td align="right">39.65</td>
    <td align="right">39.58</td>
    <td align="right">39.62</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.46</td>
    <td align="right">39.01</td>
    <td align="right">38.92</td>
    <td align="right">38.95</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.88</td>
    <td align="right">29.17</td>
    <td align="right">29.06</td>
    <td align="right">29.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.63</td>
    <td align="right">42.48</td>
    <td align="right">42.44</td>
    <td align="right">42.45</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.39</td>
    <td align="right">46.78</td>
    <td align="right">47.08</td>
    <td align="right">47.10</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.04</td>
    <td align="right">30.22</td>
    <td align="right">30.16</td>
    <td align="right">30.20</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.36</td>
    <td align="right">21.69</td>
    <td align="right">19.85</td>
    <td align="right">24.82</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.01</td>
    <td align="right">25.72</td>
    <td align="right">25.27</td>
    <td align="right">27.91</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.07</td>
    <td align="right">25.63</td>
    <td align="right">25.46</td>
    <td align="right">27.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.85</td>
    <td align="right">25.12</td>
    <td align="right">22.57</td>
    <td align="right">27.46</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">29.70</td>
    <td align="right">26.84</td>
    <td align="right">31.09</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.59</td>
    <td align="right">30.51</td>
    <td align="right">26.94</td>
    <td align="right">31.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.30</td>
    <td align="right">26.92</td>
    <td align="right">24.71</td>
    <td align="right">30.46</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.11</td>
    <td align="right">40.67</td>
    <td align="right">27.80</td>
    <td align="right">36.73</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.56</td>
    <td align="right">41.93</td>
    <td align="right">28.06</td>
    <td align="right">37.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.83</td>
    <td align="right">27.95</td>
    <td align="right">23.04</td>
    <td align="right">29.86</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.56</td>
    <td align="right">44.20</td>
    <td align="right">27.25</td>
    <td align="right">38.76</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.42</td>
    <td align="right">48.76</td>
    <td align="right">28.18</td>
    <td align="right">41.02</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.34</td>
    <td align="right">22.85</td>
    <td align="right">22.65</td>
    <td align="right">22.76</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">28.18</td>
    <td align="right">27.99</td>
    <td align="right">28.12</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.11</td>
    <td align="right">28.49</td>
    <td align="right">28.30</td>
    <td align="right">28.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.81</td>
    <td align="right">26.34</td>
    <td align="right">26.20</td>
    <td align="right">26.28</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.70</td>
    <td align="right">33.61</td>
    <td align="right">33.45</td>
    <td align="right">33.53</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.60</td>
    <td align="right">31.62</td>
    <td align="right">31.72</td>
    <td align="right">31.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.29</td>
    <td align="right">28.38</td>
    <td align="right">28.29</td>
    <td align="right">28.33</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.12</td>
    <td align="right">39.46</td>
    <td align="right">39.42</td>
    <td align="right">39.45</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.54</td>
    <td align="right">39.15</td>
    <td align="right">39.10</td>
    <td align="right">39.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.82</td>
    <td align="right">29.15</td>
    <td align="right">29.08</td>
    <td align="right">29.13</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.43</td>
    <td align="right">42.21</td>
    <td align="right">42.18</td>
    <td align="right">42.20</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.48</td>
    <td align="right">46.19</td>
    <td align="right">46.37</td>
    <td align="right">46.68</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.09</td>
    <td align="right">21.24</td>
    <td align="right">19.83</td>
    <td align="right">24.63</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">26.17</td>
    <td align="right">26.62</td>
    <td align="right">28.26</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.15</td>
    <td align="right">25.49</td>
    <td align="right">25.38</td>
    <td align="right">27.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.87</td>
    <td align="right">24.83</td>
    <td align="right">22.49</td>
    <td align="right">27.98</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">30.27</td>
    <td align="right">27.87</td>
    <td align="right">31.02</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.17</td>
    <td align="right">30.57</td>
    <td align="right">27.11</td>
    <td align="right">31.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.30</td>
    <td align="right">26.96</td>
    <td align="right">23.71</td>
    <td align="right">29.47</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.94</td>
    <td align="right">42.51</td>
    <td align="right">28.89</td>
    <td align="right">37.69</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.48</td>
    <td align="right">41.49</td>
    <td align="right">28.07</td>
    <td align="right">36.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.84</td>
    <td align="right">28.56</td>
    <td align="right">22.46</td>
    <td align="right">30.09</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.65</td>
    <td align="right">46.19</td>
    <td align="right">27.72</td>
    <td align="right">40.07</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.28</td>
    <td align="right">48.70</td>
    <td align="right">28.12</td>
    <td align="right">40.79</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.11</td>
    <td align="right">22.82</td>
    <td align="right">22.64</td>
    <td align="right">22.75</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">27.96</td>
    <td align="right">27.76</td>
    <td align="right">27.86</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.15</td>
    <td align="right">28.54</td>
    <td align="right">28.32</td>
    <td align="right">28.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.89</td>
    <td align="right">26.35</td>
    <td align="right">26.22</td>
    <td align="right">26.30</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.70</td>
    <td align="right">33.61</td>
    <td align="right">33.44</td>
    <td align="right">33.54</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.18</td>
    <td align="right">31.59</td>
    <td align="right">31.42</td>
    <td align="right">31.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.20</td>
    <td align="right">28.36</td>
    <td align="right">28.27</td>
    <td align="right">28.32</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.99</td>
    <td align="right">39.66</td>
    <td align="right">39.59</td>
    <td align="right">39.63</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.52</td>
    <td align="right">39.12</td>
    <td align="right">39.04</td>
    <td align="right">39.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.82</td>
    <td align="right">29.14</td>
    <td align="right">29.07</td>
    <td align="right">29.12</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.52</td>
    <td align="right">42.42</td>
    <td align="right">42.40</td>
    <td align="right">42.41</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.35</td>
    <td align="right">46.15</td>
    <td align="right">46.13</td>
    <td align="right">46.32</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.22</td>
    <td align="right">26.34</td>
    <td align="right">26.02</td>
    <td align="right">28.40</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.92</td>
    <td align="right">43.64</td>
    <td align="right">42.81</td>
    <td align="right">43.23</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.78</td>
    <td align="right">34.46</td>
    <td align="right">30.47</td>
    <td align="right">32.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.03</td>
    <td align="right">33.07</td>
    <td align="right">26.08</td>
    <td align="right">32.88</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">53.43</td>
    <td align="right">50.19</td>
    <td align="right">40.89</td>
    <td align="right">45.99</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.71</td>
    <td align="right">43.53</td>
    <td align="right">31.70</td>
    <td align="right">38.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.15</td>
    <td align="right">39.88</td>
    <td align="right">25.87</td>
    <td align="right">36.59</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">59.59</td>
    <td align="right">55.81</td>
    <td align="right">41.34</td>
    <td align="right">48.97</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.45</td>
    <td align="right">49.98</td>
    <td align="right">33.52</td>
    <td align="right">44.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.74</td>
    <td align="right">47.61</td>
    <td align="right">31.01</td>
    <td align="right">42.54</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.72</td>
    <td align="right">60.26</td>
    <td align="right">45.82</td>
    <td align="right">53.55</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.01</td>
    <td align="right">61.43</td>
    <td align="right">34.77</td>
    <td align="right">49.78</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.22</td>
    <td align="right">27.88</td>
    <td align="right">27.64</td>
    <td align="right">27.78</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.64</td>
    <td align="right">41.68</td>
    <td align="right">41.71</td>
    <td align="right">42.05</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.91</td>
    <td align="right">34.05</td>
    <td align="right">34.09</td>
    <td align="right">34.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.04</td>
    <td align="right">32.73</td>
    <td align="right">32.68</td>
    <td align="right">32.71</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">53.74</td>
    <td align="right">48.54</td>
    <td align="right">48.53</td>
    <td align="right">48.54</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.72</td>
    <td align="right">41.61</td>
    <td align="right">41.67</td>
    <td align="right">41.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.12</td>
    <td align="right">37.47</td>
    <td align="right">37.40</td>
    <td align="right">37.45</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.66</td>
    <td align="right">53.21</td>
    <td align="right">53.20</td>
    <td align="right">53.24</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.49</td>
    <td align="right">46.12</td>
    <td align="right">46.05</td>
    <td align="right">46.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.75</td>
    <td align="right">42.18</td>
    <td align="right">42.12</td>
    <td align="right">42.16</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.47</td>
    <td align="right">56.28</td>
    <td align="right">56.20</td>
    <td align="right">56.26</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.24</td>
    <td align="right">56.59</td>
    <td align="right">56.51</td>
    <td align="right">56.60</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.23</td>
    <td align="right">26.40</td>
    <td align="right">26.13</td>
    <td align="right">29.20</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">48.01</td>
    <td align="right">44.05</td>
    <td align="right">43.57</td>
    <td align="right">43.35</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">27.08</td>
    <td align="right">34.61</td>
    <td align="right">30.91</td>
    <td align="right">33.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.04</td>
    <td align="right">33.07</td>
    <td align="right">26.11</td>
    <td align="right">32.87</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">53.51</td>
    <td align="right">50.27</td>
    <td align="right">40.85</td>
    <td align="right">46.10</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.55</td>
    <td align="right">43.34</td>
    <td align="right">31.98</td>
    <td align="right">38.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.12</td>
    <td align="right">39.91</td>
    <td align="right">26.06</td>
    <td align="right">36.60</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">59.85</td>
    <td align="right">55.77</td>
    <td align="right">41.66</td>
    <td align="right">49.72</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.57</td>
    <td align="right">50.02</td>
    <td align="right">34.01</td>
    <td align="right">44.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.74</td>
    <td align="right">47.60</td>
    <td align="right">31.01</td>
    <td align="right">42.20</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.31</td>
    <td align="right">59.31</td>
    <td align="right">45.07</td>
    <td align="right">52.91</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.16</td>
    <td align="right">61.53</td>
    <td align="right">35.35</td>
    <td align="right">50.41</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.23</td>
    <td align="right">27.88</td>
    <td align="right">27.64</td>
    <td align="right">27.76</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">48.25</td>
    <td align="right">41.45</td>
    <td align="right">41.87</td>
    <td align="right">41.90</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.76</td>
    <td align="right">33.94</td>
    <td align="right">33.99</td>
    <td align="right">33.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.00</td>
    <td align="right">32.64</td>
    <td align="right">32.59</td>
    <td align="right">32.62</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">53.58</td>
    <td align="right">48.62</td>
    <td align="right">48.59</td>
    <td align="right">48.61</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.66</td>
    <td align="right">41.97</td>
    <td align="right">41.98</td>
    <td align="right">42.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.15</td>
    <td align="right">37.43</td>
    <td align="right">37.36</td>
    <td align="right">37.39</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.56</td>
    <td align="right">53.02</td>
    <td align="right">53.00</td>
    <td align="right">53.11</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.47</td>
    <td align="right">46.11</td>
    <td align="right">46.22</td>
    <td align="right">46.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.76</td>
    <td align="right">42.05</td>
    <td align="right">42.18</td>
    <td align="right">42.23</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">63.27</td>
    <td align="right">56.85</td>
    <td align="right">56.81</td>
    <td align="right">56.87</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.41</td>
    <td align="right">56.77</td>
    <td align="right">56.65</td>
    <td align="right">56.88</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">124.42</td>
    <td align="right">75.57</td>
    <td align="right">24.68</td>
    <td align="right">60.47</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">26.53</td>
    <td align="right">58.02</td>
    <td align="right">36.52</td>
    <td align="right">49.17</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.07</td>
    <td align="right">30.84</td>
    <td align="right">30.30</td>
    <td align="right">30.52</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.37</td>
    <td align="right">34.31</td>
    <td align="right">34.09</td>
    <td align="right">34.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">76.52</td>
    <td align="right">116.34</td>
    <td align="right">47.37</td>
    <td align="right">84.22</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.85</td>
    <td align="right">47.13</td>
    <td align="right">44.95</td>
    <td align="right">46.04</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">29.05</td>
    <td align="right">47.90</td>
    <td align="right">45.70</td>
    <td align="right">46.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">144.58</td>
    <td align="right">198.18</td>
    <td align="right">63.08</td>
    <td align="right">132.72</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">41.65</td>
    <td align="right">64.25</td>
    <td align="right">62.59</td>
    <td align="right">63.58</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">52.05</td>
    <td align="right">65.04</td>
    <td align="right">61.94</td>
    <td align="right">63.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">249.44</td>
    <td align="right">304.08</td>
    <td align="right">77.22</td>
    <td align="right">193.24</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.39</td>
    <td align="right">78.69</td>
    <td align="right">75.99</td>
    <td align="right">77.16</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.90</td>
    <td align="right">81.27</td>
    <td align="right">78.78</td>
    <td align="right">79.86</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">29.52</td>
    <td align="right">51.55</td>
    <td align="right">51.66</td>
    <td align="right">51.85</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.46</td>
    <td align="right">31.23</td>
    <td align="right">30.74</td>
    <td align="right">30.94</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.60</td>
    <td align="right">33.16</td>
    <td align="right">32.75</td>
    <td align="right">32.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">81.64</td>
    <td align="right">126.93</td>
    <td align="right">125.60</td>
    <td align="right">126.13</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.47</td>
    <td align="right">44.76</td>
    <td align="right">42.03</td>
    <td align="right">43.42</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">29.73</td>
    <td align="right">47.88</td>
    <td align="right">45.60</td>
    <td align="right">46.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">144.23</td>
    <td align="right">210.94</td>
    <td align="right">209.74</td>
    <td align="right">210.83</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.19</td>
    <td align="right">62.71</td>
    <td align="right">59.88</td>
    <td align="right">61.37</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.26</td>
    <td align="right">66.12</td>
    <td align="right">63.05</td>
    <td align="right">64.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">249.23</td>
    <td align="right">350.93</td>
    <td align="right">351.79</td>
    <td align="right">350.78</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.15</td>
    <td align="right">78.76</td>
    <td align="right">76.54</td>
    <td align="right">77.55</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.82</td>
    <td align="right">80.63</td>
    <td align="right">78.33</td>
    <td align="right">79.79</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">29.99</td>
    <td align="right">61.31</td>
    <td align="right">37.51</td>
    <td align="right">51.21</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.98</td>
    <td align="right">30.72</td>
    <td align="right">30.15</td>
    <td align="right">30.38</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.90</td>
    <td align="right">35.14</td>
    <td align="right">34.61</td>
    <td align="right">34.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">72.38</td>
    <td align="right">112.72</td>
    <td align="right">46.65</td>
    <td align="right">82.22</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.10</td>
    <td align="right">46.28</td>
    <td align="right">43.95</td>
    <td align="right">45.04</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">29.04</td>
    <td align="right">48.56</td>
    <td align="right">46.44</td>
    <td align="right">47.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">142.72</td>
    <td align="right">199.53</td>
    <td align="right">62.89</td>
    <td align="right">132.34</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">39.62</td>
    <td align="right">64.01</td>
    <td align="right">62.82</td>
    <td align="right">65.54</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.81</td>
    <td align="right">66.60</td>
    <td align="right">63.58</td>
    <td align="right">65.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">263.73</td>
    <td align="right">304.93</td>
    <td align="right">77.58</td>
    <td align="right">195.43</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.29</td>
    <td align="right">79.27</td>
    <td align="right">76.90</td>
    <td align="right">78.01</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.65</td>
    <td align="right">82.55</td>
    <td align="right">80.53</td>
    <td align="right">81.77</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">26.69</td>
    <td align="right">49.13</td>
    <td align="right">48.95</td>
    <td align="right">49.10</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.26</td>
    <td align="right">30.96</td>
    <td align="right">30.50</td>
    <td align="right">30.74</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">19.41</td>
    <td align="right">35.73</td>
    <td align="right">35.21</td>
    <td align="right">35.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">79.39</td>
    <td align="right">123.03</td>
    <td align="right">121.93</td>
    <td align="right">122.61</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">27.11</td>
    <td align="right">47.69</td>
    <td align="right">45.80</td>
    <td align="right">46.78</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">30.35</td>
    <td align="right">49.30</td>
    <td align="right">47.34</td>
    <td align="right">48.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">146.66</td>
    <td align="right">216.63</td>
    <td align="right">216.09</td>
    <td align="right">216.91</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.39</td>
    <td align="right">63.60</td>
    <td align="right">60.27</td>
    <td align="right">61.67</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">52.58</td>
    <td align="right">66.95</td>
    <td align="right">64.04</td>
    <td align="right">65.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">269.41</td>
    <td align="right">322.88</td>
    <td align="right">320.94</td>
    <td align="right">322.43</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.44</td>
    <td align="right">79.41</td>
    <td align="right">76.67</td>
    <td align="right">80.14</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.59</td>
    <td align="right">82.41</td>
    <td align="right">80.42</td>
    <td align="right">81.26</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.20</td>
    <td align="right">31.72</td>
    <td align="right">28.03</td>
    <td align="right">34.05</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">21.17</td>
    <td align="right">32.84</td>
    <td align="right">28.87</td>
    <td align="right">35.04</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">9.27</td>
    <td align="right">27.95</td>
    <td align="right">21.59</td>
    <td align="right">30.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.69</td>
    <td align="right">44.22</td>
    <td align="right">35.74</td>
    <td align="right">45.53</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">45.90</td>
    <td align="right">52.96</td>
    <td align="right">37.58</td>
    <td align="right">50.64</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.72</td>
    <td align="right">41.67</td>
    <td align="right">29.69</td>
    <td align="right">43.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.80</td>
    <td align="right">76.14</td>
    <td align="right">44.78</td>
    <td align="right">68.09</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.47</td>
    <td align="right">77.76</td>
    <td align="right">46.28</td>
    <td align="right">69.67</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.59</td>
    <td align="right">62.11</td>
    <td align="right">38.44</td>
    <td align="right">59.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.06</td>
    <td align="right">95.36</td>
    <td align="right">50.29</td>
    <td align="right">84.62</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">97.29</td>
    <td align="right">103.02</td>
    <td align="right">54.38</td>
    <td align="right">89.65</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.33</td>
    <td align="right">77.27</td>
    <td align="right">43.05</td>
    <td align="right">72.82</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.14</td>
    <td align="right">34.84</td>
    <td align="right">34.41</td>
    <td align="right">34.52</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.19</td>
    <td align="right">35.56</td>
    <td align="right">34.98</td>
    <td align="right">35.14</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">11.37</td>
    <td align="right">32.40</td>
    <td align="right">31.76</td>
    <td align="right">31.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.47</td>
    <td align="right">49.96</td>
    <td align="right">47.72</td>
    <td align="right">48.69</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.27</td>
    <td align="right">53.58</td>
    <td align="right">51.11</td>
    <td align="right">52.10</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">22.24</td>
    <td align="right">39.80</td>
    <td align="right">37.77</td>
    <td align="right">38.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.19</td>
    <td align="right">75.57</td>
    <td align="right">73.62</td>
    <td align="right">74.54</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.07</td>
    <td align="right">76.97</td>
    <td align="right">75.62</td>
    <td align="right">77.66</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.49</td>
    <td align="right">68.12</td>
    <td align="right">64.95</td>
    <td align="right">66.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.01</td>
    <td align="right">93.73</td>
    <td align="right">92.75</td>
    <td align="right">93.14</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.43</td>
    <td align="right">101.02</td>
    <td align="right">100.23</td>
    <td align="right">100.62</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.47</td>
    <td align="right">84.41</td>
    <td align="right">81.81</td>
    <td align="right">83.14</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.13</td>
    <td align="right">32.12</td>
    <td align="right">29.30</td>
    <td align="right">34.50</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.70</td>
    <td align="right">31.61</td>
    <td align="right">28.30</td>
    <td align="right">34.12</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">9.94</td>
    <td align="right">29.36</td>
    <td align="right">23.03</td>
    <td align="right">32.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.32</td>
    <td align="right">45.77</td>
    <td align="right">36.52</td>
    <td align="right">46.23</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.36</td>
    <td align="right">51.71</td>
    <td align="right">37.17</td>
    <td align="right">49.52</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.44</td>
    <td align="right">41.75</td>
    <td align="right">30.06</td>
    <td align="right">44.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.83</td>
    <td align="right">77.86</td>
    <td align="right">45.85</td>
    <td align="right">68.86</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.31</td>
    <td align="right">79.16</td>
    <td align="right">47.02</td>
    <td align="right">71.11</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.41</td>
    <td align="right">62.77</td>
    <td align="right">38.79</td>
    <td align="right">60.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.14</td>
    <td align="right">97.29</td>
    <td align="right">50.67</td>
    <td align="right">85.39</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.32</td>
    <td align="right">104.31</td>
    <td align="right">54.67</td>
    <td align="right">91.03</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">52.90</td>
    <td align="right">79.52</td>
    <td align="right">44.67</td>
    <td align="right">75.22</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.45</td>
    <td align="right">34.94</td>
    <td align="right">34.44</td>
    <td align="right">34.68</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.52</td>
    <td align="right">35.56</td>
    <td align="right">35.04</td>
    <td align="right">35.33</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">10.02</td>
    <td align="right">30.22</td>
    <td align="right">29.81</td>
    <td align="right">29.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.81</td>
    <td align="right">49.37</td>
    <td align="right">47.08</td>
    <td align="right">48.25</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.12</td>
    <td align="right">53.09</td>
    <td align="right">50.41</td>
    <td align="right">51.81</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.87</td>
    <td align="right">43.14</td>
    <td align="right">40.86</td>
    <td align="right">41.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.03</td>
    <td align="right">74.71</td>
    <td align="right">72.94</td>
    <td align="right">73.87</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.07</td>
    <td align="right">75.56</td>
    <td align="right">74.10</td>
    <td align="right">74.79</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.28</td>
    <td align="right">67.94</td>
    <td align="right">64.64</td>
    <td align="right">66.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.59</td>
    <td align="right">94.61</td>
    <td align="right">93.59</td>
    <td align="right">94.11</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.62</td>
    <td align="right">99.00</td>
    <td align="right">98.17</td>
    <td align="right">98.55</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.97</td>
    <td align="right">84.27</td>
    <td align="right">81.53</td>
    <td align="right">82.81</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">8.85</td>
    <td align="right">27.91</td>
    <td align="right">21.71</td>
    <td align="right">30.94</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.44</td>
    <td align="right">32.12</td>
    <td align="right">28.22</td>
    <td align="right">34.37</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.22</td>
    <td align="right">31.49</td>
    <td align="right">28.19</td>
    <td align="right">33.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">24.14</td>
    <td align="right">45.12</td>
    <td align="right">31.47</td>
    <td align="right">45.65</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.33</td>
    <td align="right">43.85</td>
    <td align="right">35.05</td>
    <td align="right">44.83</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.10</td>
    <td align="right">47.51</td>
    <td align="right">34.61</td>
    <td align="right">45.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.28</td>
    <td align="right">61.62</td>
    <td align="right">38.65</td>
    <td align="right">59.11</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.80</td>
    <td align="right">76.99</td>
    <td align="right">45.19</td>
    <td align="right">68.99</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.56</td>
    <td align="right">80.48</td>
    <td align="right">47.47</td>
    <td align="right">72.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.03</td>
    <td align="right">77.74</td>
    <td align="right">43.56</td>
    <td align="right">73.61</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.91</td>
    <td align="right">97.30</td>
    <td align="right">50.85</td>
    <td align="right">86.24</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.59</td>
    <td align="right">101.65</td>
    <td align="right">53.90</td>
    <td align="right">92.73</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.53</td>
    <td align="right">29.74</td>
    <td align="right">29.31</td>
    <td align="right">29.46</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.18</td>
    <td align="right">34.76</td>
    <td align="right">34.28</td>
    <td align="right">34.51</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.13</td>
    <td align="right">34.85</td>
    <td align="right">34.42</td>
    <td align="right">34.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.34</td>
    <td align="right">45.78</td>
    <td align="right">43.33</td>
    <td align="right">44.44</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.43</td>
    <td align="right">51.22</td>
    <td align="right">49.10</td>
    <td align="right">50.19</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">40.66</td>
    <td align="right">50.86</td>
    <td align="right">47.31</td>
    <td align="right">48.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.19</td>
    <td align="right">70.11</td>
    <td align="right">67.07</td>
    <td align="right">69.09</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.39</td>
    <td align="right">77.41</td>
    <td align="right">75.70</td>
    <td align="right">76.51</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.16</td>
    <td align="right">75.70</td>
    <td align="right">74.26</td>
    <td align="right">74.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.36</td>
    <td align="right">83.35</td>
    <td align="right">80.89</td>
    <td align="right">82.08</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.46</td>
    <td align="right">96.53</td>
    <td align="right">95.64</td>
    <td align="right">96.06</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">97.03</td>
    <td align="right">99.57</td>
    <td align="right">98.78</td>
    <td align="right">99.19</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.14</td>
    <td align="right">28.30</td>
    <td align="right">22.10</td>
    <td align="right">31.47</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.59</td>
    <td align="right">32.66</td>
    <td align="right">29.58</td>
    <td align="right">34.89</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.51</td>
    <td align="right">30.20</td>
    <td align="right">27.27</td>
    <td align="right">32.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">24.29</td>
    <td align="right">44.55</td>
    <td align="right">31.08</td>
    <td align="right">45.20</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.16</td>
    <td align="right">46.56</td>
    <td align="right">37.02</td>
    <td align="right">46.90</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.44</td>
    <td align="right">47.72</td>
    <td align="right">35.21</td>
    <td align="right">45.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.24</td>
    <td align="right">61.44</td>
    <td align="right">38.66</td>
    <td align="right">59.34</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">69.22</td>
    <td align="right">80.13</td>
    <td align="right">46.87</td>
    <td align="right">71.09</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.95</td>
    <td align="right">80.27</td>
    <td align="right">47.61</td>
    <td align="right">72.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.02</td>
    <td align="right">78.10</td>
    <td align="right">43.00</td>
    <td align="right">73.56</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.96</td>
    <td align="right">96.98</td>
    <td align="right">50.54</td>
    <td align="right">85.29</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.26</td>
    <td align="right">102.07</td>
    <td align="right">53.78</td>
    <td align="right">88.77</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">8.53</td>
    <td align="right">28.60</td>
    <td align="right">28.17</td>
    <td align="right">28.32</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.62</td>
    <td align="right">35.25</td>
    <td align="right">34.68</td>
    <td align="right">34.86</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.54</td>
    <td align="right">35.54</td>
    <td align="right">34.94</td>
    <td align="right">35.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.58</td>
    <td align="right">46.54</td>
    <td align="right">44.23</td>
    <td align="right">45.31</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.79</td>
    <td align="right">50.05</td>
    <td align="right">47.94</td>
    <td align="right">49.03</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">41.80</td>
    <td align="right">52.55</td>
    <td align="right">49.71</td>
    <td align="right">51.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.22</td>
    <td align="right">65.25</td>
    <td align="right">61.98</td>
    <td align="right">63.60</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.44</td>
    <td align="right">75.40</td>
    <td align="right">73.65</td>
    <td align="right">74.46</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.10</td>
    <td align="right">76.49</td>
    <td align="right">74.99</td>
    <td align="right">75.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.11</td>
    <td align="right">82.65</td>
    <td align="right">80.09</td>
    <td align="right">81.40</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.55</td>
    <td align="right">94.27</td>
    <td align="right">93.33</td>
    <td align="right">99.35</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.58</td>
    <td align="right">101.51</td>
    <td align="right">100.62</td>
    <td align="right">101.04</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.35</td>
    <td align="right">32.08</td>
    <td align="right">28.54</td>
    <td align="right">34.35</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">48.86</td>
    <td align="right">44.79</td>
    <td align="right">43.99</td>
    <td align="right">44.44</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">31.44</td>
    <td align="right">38.41</td>
    <td align="right">33.67</td>
    <td align="right">37.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.93</td>
    <td align="right">48.35</td>
    <td align="right">34.65</td>
    <td align="right">47.67</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">65.70</td>
    <td align="right">67.31</td>
    <td align="right">52.40</td>
    <td align="right">61.85</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">58.96</td>
    <td align="right">67.83</td>
    <td align="right">40.86</td>
    <td align="right">57.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.23</td>
    <td align="right">71.32</td>
    <td align="right">41.81</td>
    <td align="right">65.09</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">88.77</td>
    <td align="right">92.66</td>
    <td align="right">65.11</td>
    <td align="right">83.03</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.23</td>
    <td align="right">97.39</td>
    <td align="right">46.70</td>
    <td align="right">81.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.91</td>
    <td align="right">90.54</td>
    <td align="right">58.82</td>
    <td align="right">84.81</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">111.78</td>
    <td align="right">108.75</td>
    <td align="right">80.41</td>
    <td align="right">98.46</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.95</td>
    <td align="right">148.28</td>
    <td align="right">52.63</td>
    <td align="right">115.32</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.13</td>
    <td align="right">34.39</td>
    <td align="right">34.02</td>
    <td align="right">34.21</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">50.38</td>
    <td align="right">45.13</td>
    <td align="right">44.32</td>
    <td align="right">44.70</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">36.01</td>
    <td align="right">41.76</td>
    <td align="right">41.71</td>
    <td align="right">41.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.80</td>
    <td align="right">46.89</td>
    <td align="right">44.77</td>
    <td align="right">45.82</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">63.77</td>
    <td align="right">63.16</td>
    <td align="right">60.41</td>
    <td align="right">61.87</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">59.68</td>
    <td align="right">64.18</td>
    <td align="right">63.80</td>
    <td align="right">64.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.61</td>
    <td align="right">67.61</td>
    <td align="right">64.92</td>
    <td align="right">66.29</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">89.93</td>
    <td align="right">89.37</td>
    <td align="right">86.20</td>
    <td align="right">87.70</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.38</td>
    <td align="right">97.13</td>
    <td align="right">93.91</td>
    <td align="right">94.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.37</td>
    <td align="right">86.53</td>
    <td align="right">84.08</td>
    <td align="right">85.24</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.56</td>
    <td align="right">105.58</td>
    <td align="right">103.15</td>
    <td align="right">104.37</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.52</td>
    <td align="right">132.30</td>
    <td align="right">132.01</td>
    <td align="right">135.50</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">22.46</td>
    <td align="right">33.40</td>
    <td align="right">29.66</td>
    <td align="right">36.49</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">49.25</td>
    <td align="right">46.07</td>
    <td align="right">45.31</td>
    <td align="right">45.31</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">35.13</td>
    <td align="right">42.22</td>
    <td align="right">35.94</td>
    <td align="right">41.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.97</td>
    <td align="right">48.15</td>
    <td align="right">34.22</td>
    <td align="right">47.34</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">65.69</td>
    <td align="right">67.17</td>
    <td align="right">51.96</td>
    <td align="right">61.43</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">59.39</td>
    <td align="right">60.98</td>
    <td align="right">38.50</td>
    <td align="right">52.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">61.92</td>
    <td align="right">71.38</td>
    <td align="right">42.46</td>
    <td align="right">66.62</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">89.31</td>
    <td align="right">92.58</td>
    <td align="right">68.74</td>
    <td align="right">85.79</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.03</td>
    <td align="right">94.99</td>
    <td align="right">46.06</td>
    <td align="right">78.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.58</td>
    <td align="right">91.23</td>
    <td align="right">58.08</td>
    <td align="right">85.44</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.88</td>
    <td align="right">110.26</td>
    <td align="right">80.94</td>
    <td align="right">99.30</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.26</td>
    <td align="right">147.73</td>
    <td align="right">53.54</td>
    <td align="right">115.17</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">20.34</td>
    <td align="right">33.05</td>
    <td align="right">32.64</td>
    <td align="right">32.88</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">50.35</td>
    <td align="right">44.58</td>
    <td align="right">44.33</td>
    <td align="right">44.72</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">34.03</td>
    <td align="right">39.81</td>
    <td align="right">39.77</td>
    <td align="right">39.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.37</td>
    <td align="right">47.33</td>
    <td align="right">45.33</td>
    <td align="right">46.37</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">64.53</td>
    <td align="right">64.07</td>
    <td align="right">61.47</td>
    <td align="right">62.73</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">57.78</td>
    <td align="right">63.76</td>
    <td align="right">63.68</td>
    <td align="right">63.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.02</td>
    <td align="right">66.80</td>
    <td align="right">63.95</td>
    <td align="right">65.35</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">91.14</td>
    <td align="right">88.31</td>
    <td align="right">84.91</td>
    <td align="right">86.70</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.24</td>
    <td align="right">91.41</td>
    <td align="right">90.97</td>
    <td align="right">91.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.45</td>
    <td align="right">85.11</td>
    <td align="right">82.80</td>
    <td align="right">84.01</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.55</td>
    <td align="right">106.58</td>
    <td align="right">104.13</td>
    <td align="right">105.33</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">132.16</td>
    <td align="right">131.53</td>
    <td align="right">131.10</td>
    <td align="right">131.22</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.81</td>
    <td align="right">19.46</td>
    <td align="right">6.10</td>
    <td align="right">18.39</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.24</td>
    <td align="right">64.75</td>
    <td align="right">38.91</td>
    <td align="right">50.37</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">21.12</td>
    <td align="right">23.05</td>
    <td align="right">25.50</td>
    <td align="right">26.74</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.10</td>
    <td align="right">26.59</td>
    <td align="right">27.74</td>
    <td align="right">29.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">99.63</td>
    <td align="right">94.77</td>
    <td align="right">40.22</td>
    <td align="right">66.98</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.44</td>
    <td align="right">24.39</td>
    <td align="right">25.60</td>
    <td align="right">28.41</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.55</td>
    <td align="right">29.35</td>
    <td align="right">30.02</td>
    <td align="right">31.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">123.44</td>
    <td align="right">120.35</td>
    <td align="right">39.71</td>
    <td align="right">78.70</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.14</td>
    <td align="right">27.18</td>
    <td align="right">27.85</td>
    <td align="right">30.80</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.53</td>
    <td align="right">31.02</td>
    <td align="right">31.21</td>
    <td align="right">34.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">157.82</td>
    <td align="right">152.61</td>
    <td align="right">40.40</td>
    <td align="right">95.79</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.58</td>
    <td align="right">28.77</td>
    <td align="right">29.28</td>
    <td align="right">32.36</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">30.96</td>
    <td align="right">33.47</td>
    <td align="right">33.59</td>
    <td align="right">37.16</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">69.17</td>
    <td align="right">67.65</td>
    <td align="right">67.81</td>
    <td align="right">67.68</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.86</td>
    <td align="right">22.56</td>
    <td align="right">24.89</td>
    <td align="right">26.64</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.05</td>
    <td align="right">26.59</td>
    <td align="right">28.12</td>
    <td align="right">29.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">103.81</td>
    <td align="right">95.55</td>
    <td align="right">95.76</td>
    <td align="right">94.99</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.39</td>
    <td align="right">24.32</td>
    <td align="right">25.32</td>
    <td align="right">28.04</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.81</td>
    <td align="right">29.53</td>
    <td align="right">30.21</td>
    <td align="right">31.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">128.85</td>
    <td align="right">113.64</td>
    <td align="right">112.53</td>
    <td align="right">113.98</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.25</td>
    <td align="right">27.31</td>
    <td align="right">27.82</td>
    <td align="right">30.80</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">28.98</td>
    <td align="right">31.00</td>
    <td align="right">31.21</td>
    <td align="right">34.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">158.80</td>
    <td align="right">142.34</td>
    <td align="right">142.29</td>
    <td align="right">142.35</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.50</td>
    <td align="right">28.57</td>
    <td align="right">29.10</td>
    <td align="right">32.21</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">30.98</td>
    <td align="right">33.50</td>
    <td align="right">33.77</td>
    <td align="right">37.38</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.48</td>
    <td align="right">63.34</td>
    <td align="right">37.42</td>
    <td align="right">49.75</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">21.11</td>
    <td align="right">22.98</td>
    <td align="right">25.81</td>
    <td align="right">28.01</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.12</td>
    <td align="right">26.29</td>
    <td align="right">27.58</td>
    <td align="right">29.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">99.33</td>
    <td align="right">95.27</td>
    <td align="right">41.66</td>
    <td align="right">67.67</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.84</td>
    <td align="right">24.76</td>
    <td align="right">26.59</td>
    <td align="right">30.62</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.70</td>
    <td align="right">29.31</td>
    <td align="right">29.82</td>
    <td align="right">31.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">123.05</td>
    <td align="right">116.39</td>
    <td align="right">39.37</td>
    <td align="right">77.99</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.51</td>
    <td align="right">27.49</td>
    <td align="right">28.42</td>
    <td align="right">33.18</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.36</td>
    <td align="right">30.89</td>
    <td align="right">31.34</td>
    <td align="right">33.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">157.98</td>
    <td align="right">150.82</td>
    <td align="right">40.04</td>
    <td align="right">95.60</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.88</td>
    <td align="right">28.73</td>
    <td align="right">29.34</td>
    <td align="right">34.58</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.49</td>
    <td align="right">32.62</td>
    <td align="right">32.65</td>
    <td align="right">35.83</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">67.68</td>
    <td align="right">68.76</td>
    <td align="right">67.86</td>
    <td align="right">67.71</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.99</td>
    <td align="right">22.84</td>
    <td align="right">25.56</td>
    <td align="right">27.66</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.98</td>
    <td align="right">26.29</td>
    <td align="right">27.82</td>
    <td align="right">29.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">99.75</td>
    <td align="right">101.80</td>
    <td align="right">101.12</td>
    <td align="right">101.11</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.98</td>
    <td align="right">24.55</td>
    <td align="right">26.45</td>
    <td align="right">30.77</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.82</td>
    <td align="right">29.34</td>
    <td align="right">29.74</td>
    <td align="right">31.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">123.78</td>
    <td align="right">122.97</td>
    <td align="right">123.59</td>
    <td align="right">123.51</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.57</td>
    <td align="right">27.27</td>
    <td align="right">28.24</td>
    <td align="right">32.98</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.37</td>
    <td align="right">31.27</td>
    <td align="right">31.66</td>
    <td align="right">33.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">158.11</td>
    <td align="right">159.53</td>
    <td align="right">161.63</td>
    <td align="right">160.13</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.89</td>
    <td align="right">28.73</td>
    <td align="right">29.51</td>
    <td align="right">34.78</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.70</td>
    <td align="right">32.73</td>
    <td align="right">32.72</td>
    <td align="right">35.85</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.33</td>
    <td align="right">44.30</td>
    <td align="right">34.51</td>
    <td align="right">39.60</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.43</td>
    <td align="right">44.14</td>
    <td align="right">36.27</td>
    <td align="right">40.46</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.60</td>
    <td align="right">17.96</td>
    <td align="right">18.31</td>
    <td align="right">26.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.72</td>
    <td align="right">59.78</td>
    <td align="right">35.73</td>
    <td align="right">48.05</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.11</td>
    <td align="right">60.18</td>
    <td align="right">37.96</td>
    <td align="right">49.43</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.87</td>
    <td align="right">23.17</td>
    <td align="right">19.42</td>
    <td align="right">29.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">37.93</td>
    <td align="right">79.79</td>
    <td align="right">36.58</td>
    <td align="right">58.48</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.06</td>
    <td align="right">79.96</td>
    <td align="right">38.64</td>
    <td align="right">59.34</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.20</td>
    <td align="right">33.95</td>
    <td align="right">23.25</td>
    <td align="right">36.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.28</td>
    <td align="right">90.35</td>
    <td align="right">36.25</td>
    <td align="right">63.86</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.35</td>
    <td align="right">98.38</td>
    <td align="right">39.99</td>
    <td align="right">70.14</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.23</td>
    <td align="right">33.79</td>
    <td align="right">23.15</td>
    <td align="right">36.94</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.34</td>
    <td align="right">42.88</td>
    <td align="right">42.99</td>
    <td align="right">45.33</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.57</td>
    <td align="right">42.55</td>
    <td align="right">42.75</td>
    <td align="right">44.87</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.69</td>
    <td align="right">18.06</td>
    <td align="right">18.34</td>
    <td align="right">26.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.64</td>
    <td align="right">57.25</td>
    <td align="right">57.21</td>
    <td align="right">60.93</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.12</td>
    <td align="right">57.47</td>
    <td align="right">57.41</td>
    <td align="right">59.74</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.81</td>
    <td align="right">18.08</td>
    <td align="right">17.94</td>
    <td align="right">26.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">37.70</td>
    <td align="right">78.70</td>
    <td align="right">78.63</td>
    <td align="right">81.83</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.05</td>
    <td align="right">77.41</td>
    <td align="right">77.31</td>
    <td align="right">79.84</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.19</td>
    <td align="right">29.44</td>
    <td align="right">29.26</td>
    <td align="right">38.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.01</td>
    <td align="right">86.13</td>
    <td align="right">86.20</td>
    <td align="right">88.29</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.24</td>
    <td align="right">90.84</td>
    <td align="right">90.58</td>
    <td align="right">93.02</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.18</td>
    <td align="right">29.44</td>
    <td align="right">29.25</td>
    <td align="right">37.94</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.21</td>
    <td align="right">43.88</td>
    <td align="right">35.01</td>
    <td align="right">40.17</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.12</td>
    <td align="right">44.15</td>
    <td align="right">35.87</td>
    <td align="right">40.28</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.40</td>
    <td align="right">17.84</td>
    <td align="right">18.11</td>
    <td align="right">26.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.58</td>
    <td align="right">59.90</td>
    <td align="right">36.01</td>
    <td align="right">48.16</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.31</td>
    <td align="right">60.01</td>
    <td align="right">38.09</td>
    <td align="right">50.22</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.88</td>
    <td align="right">23.26</td>
    <td align="right">19.43</td>
    <td align="right">29.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">38.93</td>
    <td align="right">81.49</td>
    <td align="right">37.39</td>
    <td align="right">59.91</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.09</td>
    <td align="right">79.58</td>
    <td align="right">38.64</td>
    <td align="right">59.00</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.11</td>
    <td align="right">34.78</td>
    <td align="right">23.63</td>
    <td align="right">37.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.50</td>
    <td align="right">91.05</td>
    <td align="right">36.27</td>
    <td align="right">64.60</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.59</td>
    <td align="right">97.57</td>
    <td align="right">39.00</td>
    <td align="right">69.26</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.14</td>
    <td align="right">34.93</td>
    <td align="right">23.66</td>
    <td align="right">37.51</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.22</td>
    <td align="right">42.18</td>
    <td align="right">42.64</td>
    <td align="right">45.11</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.28</td>
    <td align="right">42.54</td>
    <td align="right">42.54</td>
    <td align="right">44.90</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.45</td>
    <td align="right">17.92</td>
    <td align="right">18.18</td>
    <td align="right">26.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.68</td>
    <td align="right">57.11</td>
    <td align="right">56.99</td>
    <td align="right">59.57</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.28</td>
    <td align="right">57.17</td>
    <td align="right">57.14</td>
    <td align="right">59.35</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.89</td>
    <td align="right">18.21</td>
    <td align="right">18.00</td>
    <td align="right">26.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">38.93</td>
    <td align="right">76.47</td>
    <td align="right">76.27</td>
    <td align="right">78.75</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">41.86</td>
    <td align="right">76.43</td>
    <td align="right">75.92</td>
    <td align="right">79.23</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.19</td>
    <td align="right">29.90</td>
    <td align="right">29.59</td>
    <td align="right">38.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.72</td>
    <td align="right">85.70</td>
    <td align="right">85.43</td>
    <td align="right">87.90</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.55</td>
    <td align="right">92.20</td>
    <td align="right">91.99</td>
    <td align="right">95.04</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.12</td>
    <td align="right">29.88</td>
    <td align="right">29.66</td>
    <td align="right">38.82</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.93</td>
    <td align="right">17.88</td>
    <td align="right">18.22</td>
    <td align="right">25.74</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.88</td>
    <td align="right">20.06</td>
    <td align="right">20.47</td>
    <td align="right">27.99</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.41</td>
    <td align="right">20.14</td>
    <td align="right">20.52</td>
    <td align="right">27.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.00</td>
    <td align="right">28.60</td>
    <td align="right">21.50</td>
    <td align="right">34.20</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.90</td>
    <td align="right">25.02</td>
    <td align="right">21.34</td>
    <td align="right">30.24</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.74</td>
    <td align="right">33.16</td>
    <td align="right">26.49</td>
    <td align="right">38.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.11</td>
    <td align="right">33.86</td>
    <td align="right">22.32</td>
    <td align="right">36.33</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.87</td>
    <td align="right">39.78</td>
    <td align="right">27.81</td>
    <td align="right">42.12</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.69</td>
    <td align="right">39.61</td>
    <td align="right">27.88</td>
    <td align="right">41.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.11</td>
    <td align="right">34.08</td>
    <td align="right">22.64</td>
    <td align="right">37.10</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.62</td>
    <td align="right">41.45</td>
    <td align="right">27.76</td>
    <td align="right">41.90</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.95</td>
    <td align="right">41.72</td>
    <td align="right">27.77</td>
    <td align="right">41.90</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">18.03</td>
    <td align="right">17.98</td>
    <td align="right">18.33</td>
    <td align="right">26.03</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.91</td>
    <td align="right">20.06</td>
    <td align="right">20.48</td>
    <td align="right">27.93</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.41</td>
    <td align="right">20.14</td>
    <td align="right">20.51</td>
    <td align="right">27.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.00</td>
    <td align="right">18.46</td>
    <td align="right">18.41</td>
    <td align="right">27.06</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.88</td>
    <td align="right">20.37</td>
    <td align="right">20.03</td>
    <td align="right">27.58</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.74</td>
    <td align="right">20.09</td>
    <td align="right">20.05</td>
    <td align="right">27.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.09</td>
    <td align="right">29.62</td>
    <td align="right">29.46</td>
    <td align="right">37.92</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.86</td>
    <td align="right">32.69</td>
    <td align="right">32.69</td>
    <td align="right">40.89</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.71</td>
    <td align="right">32.69</td>
    <td align="right">32.72</td>
    <td align="right">40.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.10</td>
    <td align="right">29.68</td>
    <td align="right">29.48</td>
    <td align="right">38.30</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.61</td>
    <td align="right">34.62</td>
    <td align="right">34.60</td>
    <td align="right">42.94</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.95</td>
    <td align="right">34.51</td>
    <td align="right">34.48</td>
    <td align="right">43.03</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.85</td>
    <td align="right">17.75</td>
    <td align="right">17.98</td>
    <td align="right">26.45</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.83</td>
    <td align="right">20.08</td>
    <td align="right">20.18</td>
    <td align="right">27.72</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.43</td>
    <td align="right">20.10</td>
    <td align="right">20.15</td>
    <td align="right">27.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.90</td>
    <td align="right">28.22</td>
    <td align="right">21.34</td>
    <td align="right">33.76</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.80</td>
    <td align="right">25.01</td>
    <td align="right">21.34</td>
    <td align="right">30.53</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.93</td>
    <td align="right">33.41</td>
    <td align="right">26.02</td>
    <td align="right">38.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.13</td>
    <td align="right">34.15</td>
    <td align="right">22.69</td>
    <td align="right">36.57</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.26</td>
    <td align="right">34.19</td>
    <td align="right">22.51</td>
    <td align="right">35.39</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.30</td>
    <td align="right">40.06</td>
    <td align="right">27.80</td>
    <td align="right">41.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.01</td>
    <td align="right">34.38</td>
    <td align="right">22.80</td>
    <td align="right">36.79</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.70</td>
    <td align="right">35.60</td>
    <td align="right">22.41</td>
    <td align="right">36.09</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.05</td>
    <td align="right">42.36</td>
    <td align="right">28.13</td>
    <td align="right">42.16</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.87</td>
    <td align="right">17.83</td>
    <td align="right">18.03</td>
    <td align="right">25.94</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.85</td>
    <td align="right">20.15</td>
    <td align="right">20.22</td>
    <td align="right">27.60</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.47</td>
    <td align="right">20.13</td>
    <td align="right">20.19</td>
    <td align="right">27.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.92</td>
    <td align="right">18.40</td>
    <td align="right">18.19</td>
    <td align="right">27.21</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.80</td>
    <td align="right">20.27</td>
    <td align="right">19.89</td>
    <td align="right">27.53</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.87</td>
    <td align="right">20.19</td>
    <td align="right">19.90</td>
    <td align="right">27.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.01</td>
    <td align="right">29.27</td>
    <td align="right">28.88</td>
    <td align="right">38.13</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.35</td>
    <td align="right">32.63</td>
    <td align="right">32.56</td>
    <td align="right">41.14</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.29</td>
    <td align="right">32.63</td>
    <td align="right">32.59</td>
    <td align="right">40.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.01</td>
    <td align="right">29.44</td>
    <td align="right">28.93</td>
    <td align="right">38.60</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.65</td>
    <td align="right">34.27</td>
    <td align="right">34.05</td>
    <td align="right">42.43</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.01</td>
    <td align="right">34.25</td>
    <td align="right">34.03</td>
    <td align="right">42.95</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">27.01</td>
    <td align="right">45.92</td>
    <td align="right">34.20</td>
    <td align="right">40.21</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.11</td>
    <td align="right">57.98</td>
    <td align="right">38.72</td>
    <td align="right">48.38</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.43</td>
    <td align="right">65.35</td>
    <td align="right">40.86</td>
    <td align="right">52.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.81</td>
    <td align="right">63.31</td>
    <td align="right">34.87</td>
    <td align="right">50.52</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.31</td>
    <td align="right">63.93</td>
    <td align="right">36.91</td>
    <td align="right">51.39</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.45</td>
    <td align="right">83.48</td>
    <td align="right">42.31</td>
    <td align="right">62.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.53</td>
    <td align="right">75.35</td>
    <td align="right">34.75</td>
    <td align="right">56.15</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">47.09</td>
    <td align="right">82.49</td>
    <td align="right">38.93</td>
    <td align="right">61.68</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">47.67</td>
    <td align="right">92.98</td>
    <td align="right">39.27</td>
    <td align="right">66.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.65</td>
    <td align="right">104.42</td>
    <td align="right">36.42</td>
    <td align="right">72.82</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.96</td>
    <td align="right">103.82</td>
    <td align="right">37.84</td>
    <td align="right">72.30</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">63.49</td>
    <td align="right">124.87</td>
    <td align="right">41.48</td>
    <td align="right">83.91</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">27.15</td>
    <td align="right">47.34</td>
    <td align="right">47.46</td>
    <td align="right">49.88</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.68</td>
    <td align="right">52.30</td>
    <td align="right">52.56</td>
    <td align="right">55.13</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.41</td>
    <td align="right">62.16</td>
    <td align="right">62.46</td>
    <td align="right">65.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.87</td>
    <td align="right">57.62</td>
    <td align="right">57.61</td>
    <td align="right">59.42</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.03</td>
    <td align="right">61.53</td>
    <td align="right">61.01</td>
    <td align="right">63.23</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.71</td>
    <td align="right">80.41</td>
    <td align="right">79.77</td>
    <td align="right">82.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.95</td>
    <td align="right">68.92</td>
    <td align="right">68.25</td>
    <td align="right">71.08</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.95</td>
    <td align="right">79.39</td>
    <td align="right">78.33</td>
    <td align="right">81.29</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">47.12</td>
    <td align="right">85.79</td>
    <td align="right">85.46</td>
    <td align="right">88.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.61</td>
    <td align="right">92.18</td>
    <td align="right">91.90</td>
    <td align="right">96.14</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.99</td>
    <td align="right">91.94</td>
    <td align="right">92.22</td>
    <td align="right">96.33</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">63.04</td>
    <td align="right">119.01</td>
    <td align="right">119.20</td>
    <td align="right">121.86</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">28.28</td>
    <td align="right">45.43</td>
    <td align="right">34.72</td>
    <td align="right">40.52</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.79</td>
    <td align="right">57.98</td>
    <td align="right">38.93</td>
    <td align="right">48.65</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">38.27</td>
    <td align="right">65.21</td>
    <td align="right">41.60</td>
    <td align="right">53.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">38.08</td>
    <td align="right">63.42</td>
    <td align="right">36.62</td>
    <td align="right">51.08</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.08</td>
    <td align="right">63.59</td>
    <td align="right">36.96</td>
    <td align="right">51.35</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">46.46</td>
    <td align="right">83.10</td>
    <td align="right">41.34</td>
    <td align="right">62.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">43.33</td>
    <td align="right">75.83</td>
    <td align="right">36.12</td>
    <td align="right">56.87</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">47.08</td>
    <td align="right">82.23</td>
    <td align="right">37.79</td>
    <td align="right">60.77</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">49.39</td>
    <td align="right">93.52</td>
    <td align="right">39.67</td>
    <td align="right">67.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">54.68</td>
    <td align="right">104.52</td>
    <td align="right">37.75</td>
    <td align="right">72.98</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.85</td>
    <td align="right">105.06</td>
    <td align="right">38.12</td>
    <td align="right">73.00</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">65.01</td>
    <td align="right">126.43</td>
    <td align="right">40.77</td>
    <td align="right">85.74</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">28.25</td>
    <td align="right">46.77</td>
    <td align="right">46.89</td>
    <td align="right">49.33</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.88</td>
    <td align="right">52.33</td>
    <td align="right">52.24</td>
    <td align="right">54.34</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">38.67</td>
    <td align="right">62.32</td>
    <td align="right">62.27</td>
    <td align="right">64.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">38.05</td>
    <td align="right">58.29</td>
    <td align="right">57.43</td>
    <td align="right">60.32</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">39.96</td>
    <td align="right">61.47</td>
    <td align="right">61.07</td>
    <td align="right">63.31</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">46.25</td>
    <td align="right">79.18</td>
    <td align="right">79.34</td>
    <td align="right">81.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">43.22</td>
    <td align="right">68.95</td>
    <td align="right">68.25</td>
    <td align="right">71.22</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">47.17</td>
    <td align="right">78.49</td>
    <td align="right">78.19</td>
    <td align="right">80.67</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">49.34</td>
    <td align="right">84.65</td>
    <td align="right">84.60</td>
    <td align="right">87.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">54.39</td>
    <td align="right">92.40</td>
    <td align="right">92.78</td>
    <td align="right">96.49</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.79</td>
    <td align="right">92.76</td>
    <td align="right">92.67</td>
    <td align="right">96.65</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">64.99</td>
    <td align="right">118.85</td>
    <td align="right">119.03</td>
    <td align="right">124.18</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">60.78</td>
    <td align="right">69.53</td>
    <td align="right">16.08</td>
    <td align="right">54.16</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">70.33</td>
    <td align="right">69.73</td>
    <td align="right">42.73</td>
    <td align="right">55.80</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.04</td>
    <td align="right">22.55</td>
    <td align="right">25.26</td>
    <td align="right">27.52</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.72</td>
    <td align="right">27.83</td>
    <td align="right">29.55</td>
    <td align="right">30.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">107.62</td>
    <td align="right">103.08</td>
    <td align="right">45.21</td>
    <td align="right">73.40</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">23.95</td>
    <td align="right">27.51</td>
    <td align="right">26.98</td>
    <td align="right">31.10</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">30.11</td>
    <td align="right">33.23</td>
    <td align="right">31.80</td>
    <td align="right">34.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">259.97</td>
    <td align="right">259.39</td>
    <td align="right">70.06</td>
    <td align="right">164.33</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.62</td>
    <td align="right">43.10</td>
    <td align="right">40.81</td>
    <td align="right">46.95</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.88</td>
    <td align="right">51.59</td>
    <td align="right">49.47</td>
    <td align="right">53.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">438.25</td>
    <td align="right">435.82</td>
    <td align="right">91.34</td>
    <td align="right">261.65</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.09</td>
    <td align="right">53.13</td>
    <td align="right">52.26</td>
    <td align="right">57.94</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.54</td>
    <td align="right">65.34</td>
    <td align="right">64.09</td>
    <td align="right">67.93</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">72.43</td>
    <td align="right">71.38</td>
    <td align="right">71.35</td>
    <td align="right">70.52</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.15</td>
    <td align="right">22.57</td>
    <td align="right">25.33</td>
    <td align="right">27.62</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.71</td>
    <td align="right">27.86</td>
    <td align="right">29.51</td>
    <td align="right">30.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">109.04</td>
    <td align="right">101.34</td>
    <td align="right">100.47</td>
    <td align="right">101.12</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.02</td>
    <td align="right">27.67</td>
    <td align="right">26.86</td>
    <td align="right">30.80</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">30.03</td>
    <td align="right">33.19</td>
    <td align="right">32.08</td>
    <td align="right">34.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">258.92</td>
    <td align="right">229.85</td>
    <td align="right">228.43</td>
    <td align="right">229.52</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.48</td>
    <td align="right">43.00</td>
    <td align="right">40.70</td>
    <td align="right">46.96</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.40</td>
    <td align="right">51.95</td>
    <td align="right">49.54</td>
    <td align="right">53.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">439.73</td>
    <td align="right">369.00</td>
    <td align="right">368.38</td>
    <td align="right">368.76</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.06</td>
    <td align="right">53.07</td>
    <td align="right">52.24</td>
    <td align="right">57.80</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.85</td>
    <td align="right">65.37</td>
    <td align="right">63.89</td>
    <td align="right">67.87</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">72.51</td>
    <td align="right">68.96</td>
    <td align="right">42.54</td>
    <td align="right">55.08</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.26</td>
    <td align="right">23.03</td>
    <td align="right">26.54</td>
    <td align="right">29.52</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.85</td>
    <td align="right">27.87</td>
    <td align="right">29.07</td>
    <td align="right">30.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">108.33</td>
    <td align="right">103.71</td>
    <td align="right">46.16</td>
    <td align="right">74.07</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.99</td>
    <td align="right">28.75</td>
    <td align="right">28.52</td>
    <td align="right">35.01</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">30.42</td>
    <td align="right">34.44</td>
    <td align="right">32.33</td>
    <td align="right">35.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">261.63</td>
    <td align="right">257.84</td>
    <td align="right">69.68</td>
    <td align="right">163.03</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">41.69</td>
    <td align="right">44.96</td>
    <td align="right">44.05</td>
    <td align="right">51.14</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.77</td>
    <td align="right">51.67</td>
    <td align="right">49.92</td>
    <td align="right">53.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">439.70</td>
    <td align="right">436.21</td>
    <td align="right">91.00</td>
    <td align="right">261.76</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">54.51</td>
    <td align="right">57.34</td>
    <td align="right">56.05</td>
    <td align="right">63.44</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.78</td>
    <td align="right">63.65</td>
    <td align="right">62.51</td>
    <td align="right">66.08</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">71.99</td>
    <td align="right">75.22</td>
    <td align="right">75.73</td>
    <td align="right">75.51</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.28</td>
    <td align="right">23.13</td>
    <td align="right">26.60</td>
    <td align="right">29.54</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.84</td>
    <td align="right">27.88</td>
    <td align="right">29.12</td>
    <td align="right">30.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">110.11</td>
    <td align="right">111.46</td>
    <td align="right">110.89</td>
    <td align="right">111.14</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.74</td>
    <td align="right">28.71</td>
    <td align="right">28.34</td>
    <td align="right">34.66</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">30.60</td>
    <td align="right">34.43</td>
    <td align="right">32.21</td>
    <td align="right">35.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">259.86</td>
    <td align="right">259.51</td>
    <td align="right">259.47</td>
    <td align="right">258.73</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">41.76</td>
    <td align="right">45.15</td>
    <td align="right">44.34</td>
    <td align="right">51.50</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">48.16</td>
    <td align="right">51.94</td>
    <td align="right">50.27</td>
    <td align="right">53.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">441.06</td>
    <td align="right">437.58</td>
    <td align="right">436.61</td>
    <td align="right">436.50</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">54.11</td>
    <td align="right">57.24</td>
    <td align="right">55.84</td>
    <td align="right">63.40</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.13</td>
    <td align="right">63.88</td>
    <td align="right">62.58</td>
    <td align="right">66.31</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">26.08</td>
    <td align="right">44.27</td>
    <td align="right">36.15</td>
    <td align="right">40.61</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.87</td>
    <td align="right">44.19</td>
    <td align="right">37.97</td>
    <td align="right">41.82</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.06</td>
    <td align="right">18.42</td>
    <td align="right">18.83</td>
    <td align="right">28.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">32.75</td>
    <td align="right">62.85</td>
    <td align="right">38.59</td>
    <td align="right">51.38</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">35.04</td>
    <td align="right">63.37</td>
    <td align="right">41.17</td>
    <td align="right">52.97</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">18.33</td>
    <td align="right">27.73</td>
    <td align="right">20.76</td>
    <td align="right">32.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">57.83</td>
    <td align="right">93.85</td>
    <td align="right">51.64</td>
    <td align="right">73.35</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">64.30</td>
    <td align="right">97.39</td>
    <td align="right">59.39</td>
    <td align="right">78.74</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">47.22</td>
    <td align="right">62.14</td>
    <td align="right">48.42</td>
    <td align="right">62.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">75.48</td>
    <td align="right">113.37</td>
    <td align="right">62.44</td>
    <td align="right">89.15</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.19</td>
    <td align="right">129.69</td>
    <td align="right">75.82</td>
    <td align="right">104.05</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.98</td>
    <td align="right">73.83</td>
    <td align="right">61.53</td>
    <td align="right">74.86</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">26.37</td>
    <td align="right">43.20</td>
    <td align="right">43.39</td>
    <td align="right">45.72</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.01</td>
    <td align="right">42.52</td>
    <td align="right">43.01</td>
    <td align="right">45.38</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.12</td>
    <td align="right">18.48</td>
    <td align="right">18.84</td>
    <td align="right">28.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">32.91</td>
    <td align="right">60.25</td>
    <td align="right">58.51</td>
    <td align="right">63.64</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">35.27</td>
    <td align="right">61.53</td>
    <td align="right">59.49</td>
    <td align="right">63.02</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">18.59</td>
    <td align="right">22.02</td>
    <td align="right">19.60</td>
    <td align="right">30.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">58.16</td>
    <td align="right">92.65</td>
    <td align="right">92.03</td>
    <td align="right">95.29</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">64.37</td>
    <td align="right">94.63</td>
    <td align="right">93.88</td>
    <td align="right">96.79</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">47.27</td>
    <td align="right">57.16</td>
    <td align="right">53.84</td>
    <td align="right">63.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">75.47</td>
    <td align="right">109.66</td>
    <td align="right">109.37</td>
    <td align="right">111.81</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.36</td>
    <td align="right">120.77</td>
    <td align="right">120.17</td>
    <td align="right">122.86</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.95</td>
    <td align="right">67.80</td>
    <td align="right">66.35</td>
    <td align="right">75.16</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">26.21</td>
    <td align="right">44.04</td>
    <td align="right">36.53</td>
    <td align="right">41.20</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.08</td>
    <td align="right">44.38</td>
    <td align="right">38.33</td>
    <td align="right">41.65</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.29</td>
    <td align="right">18.29</td>
    <td align="right">18.60</td>
    <td align="right">27.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">32.91</td>
    <td align="right">63.13</td>
    <td align="right">38.64</td>
    <td align="right">51.61</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">37.44</td>
    <td align="right">65.43</td>
    <td align="right">41.78</td>
    <td align="right">55.26</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">18.69</td>
    <td align="right">29.43</td>
    <td align="right">20.95</td>
    <td align="right">32.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">62.02</td>
    <td align="right">96.93</td>
    <td align="right">53.68</td>
    <td align="right">76.16</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">66.47</td>
    <td align="right">99.04</td>
    <td align="right">61.89</td>
    <td align="right">80.63</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">50.04</td>
    <td align="right">63.83</td>
    <td align="right">50.09</td>
    <td align="right">64.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">78.34</td>
    <td align="right">116.62</td>
    <td align="right">62.91</td>
    <td align="right">90.70</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.81</td>
    <td align="right">128.34</td>
    <td align="right">75.36</td>
    <td align="right">103.31</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">61.16</td>
    <td align="right">75.02</td>
    <td align="right">62.56</td>
    <td align="right">76.29</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">26.21</td>
    <td align="right">42.44</td>
    <td align="right">42.87</td>
    <td align="right">45.31</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.01</td>
    <td align="right">42.85</td>
    <td align="right">43.12</td>
    <td align="right">45.55</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.33</td>
    <td align="right">18.32</td>
    <td align="right">18.59</td>
    <td align="right">27.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">32.61</td>
    <td align="right">59.93</td>
    <td align="right">58.06</td>
    <td align="right">61.99</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">37.12</td>
    <td align="right">61.47</td>
    <td align="right">59.41</td>
    <td align="right">62.60</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">18.49</td>
    <td align="right">21.83</td>
    <td align="right">19.41</td>
    <td align="right">30.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">61.71</td>
    <td align="right">92.36</td>
    <td align="right">91.19</td>
    <td align="right">94.36</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">65.69</td>
    <td align="right">95.97</td>
    <td align="right">93.80</td>
    <td align="right">98.21</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">49.72</td>
    <td align="right">57.91</td>
    <td align="right">55.29</td>
    <td align="right">65.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">78.47</td>
    <td align="right">110.16</td>
    <td align="right">109.85</td>
    <td align="right">112.74</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.81</td>
    <td align="right">122.30</td>
    <td align="right">121.62</td>
    <td align="right">124.85</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">60.86</td>
    <td align="right">68.82</td>
    <td align="right">67.42</td>
    <td align="right">76.91</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.19</td>
    <td align="right">18.22</td>
    <td align="right">18.54</td>
    <td align="right">27.07</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.13</td>
    <td align="right">20.09</td>
    <td align="right">20.51</td>
    <td align="right">29.26</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.59</td>
    <td align="right">20.29</td>
    <td align="right">20.63</td>
    <td align="right">28.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">19.55</td>
    <td align="right">34.26</td>
    <td align="right">24.08</td>
    <td align="right">37.88</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">20.25</td>
    <td align="right">30.32</td>
    <td align="right">22.85</td>
    <td align="right">34.00</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">22.68</td>
    <td align="right">38.37</td>
    <td align="right">30.72</td>
    <td align="right">43.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">50.37</td>
    <td align="right">63.39</td>
    <td align="right">47.99</td>
    <td align="right">63.19</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.79</td>
    <td align="right">65.83</td>
    <td align="right">51.77</td>
    <td align="right">66.88</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.93</td>
    <td align="right">65.24</td>
    <td align="right">52.82</td>
    <td align="right">66.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">60.97</td>
    <td align="right">75.25</td>
    <td align="right">60.12</td>
    <td align="right">76.08</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.59</td>
    <td align="right">79.27</td>
    <td align="right">65.62</td>
    <td align="right">80.50</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">65.21</td>
    <td align="right">81.10</td>
    <td align="right">67.06</td>
    <td align="right">81.44</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.28</td>
    <td align="right">18.26</td>
    <td align="right">18.55</td>
    <td align="right">27.06</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.12</td>
    <td align="right">20.05</td>
    <td align="right">20.60</td>
    <td align="right">29.36</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.65</td>
    <td align="right">20.40</td>
    <td align="right">20.68</td>
    <td align="right">28.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">19.64</td>
    <td align="right">23.56</td>
    <td align="right">20.61</td>
    <td align="right">30.41</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">20.49</td>
    <td align="right">24.14</td>
    <td align="right">21.68</td>
    <td align="right">30.62</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">22.55</td>
    <td align="right">26.44</td>
    <td align="right">22.52</td>
    <td align="right">32.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">50.59</td>
    <td align="right">58.52</td>
    <td align="right">55.77</td>
    <td align="right">65.39</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.76</td>
    <td align="right">56.07</td>
    <td align="right">55.16</td>
    <td align="right">65.35</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">54.25</td>
    <td align="right">57.07</td>
    <td align="right">56.13</td>
    <td align="right">66.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">60.92</td>
    <td align="right">69.80</td>
    <td align="right">68.29</td>
    <td align="right">77.32</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.66</td>
    <td align="right">70.83</td>
    <td align="right">69.94</td>
    <td align="right">80.11</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">65.12</td>
    <td align="right">72.72</td>
    <td align="right">71.73</td>
    <td align="right">81.12</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.79</td>
    <td align="right">18.14</td>
    <td align="right">18.52</td>
    <td align="right">27.75</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.15</td>
    <td align="right">20.18</td>
    <td align="right">20.43</td>
    <td align="right">28.81</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.62</td>
    <td align="right">20.27</td>
    <td align="right">20.39</td>
    <td align="right">29.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.70</td>
    <td align="right">35.71</td>
    <td align="right">25.15</td>
    <td align="right">39.56</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">20.47</td>
    <td align="right">29.67</td>
    <td align="right">22.81</td>
    <td align="right">33.79</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">23.06</td>
    <td align="right">40.55</td>
    <td align="right">31.06</td>
    <td align="right">44.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">50.72</td>
    <td align="right">64.43</td>
    <td align="right">50.67</td>
    <td align="right">65.33</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">53.57</td>
    <td align="right">57.10</td>
    <td align="right">44.50</td>
    <td align="right">58.20</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.61</td>
    <td align="right">65.25</td>
    <td align="right">52.46</td>
    <td align="right">66.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.65</td>
    <td align="right">75.73</td>
    <td align="right">63.53</td>
    <td align="right">77.13</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">66.10</td>
    <td align="right">72.36</td>
    <td align="right">59.24</td>
    <td align="right">72.73</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">66.87</td>
    <td align="right">81.67</td>
    <td align="right">66.99</td>
    <td align="right">81.57</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.79</td>
    <td align="right">18.11</td>
    <td align="right">18.54</td>
    <td align="right">27.77</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.15</td>
    <td align="right">20.20</td>
    <td align="right">20.35</td>
    <td align="right">28.75</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.64</td>
    <td align="right">20.38</td>
    <td align="right">20.37</td>
    <td align="right">29.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.15</td>
    <td align="right">23.65</td>
    <td align="right">20.80</td>
    <td align="right">31.62</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">20.21</td>
    <td align="right">24.04</td>
    <td align="right">21.46</td>
    <td align="right">31.24</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">22.92</td>
    <td align="right">27.00</td>
    <td align="right">22.71</td>
    <td align="right">33.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">50.68</td>
    <td align="right">58.53</td>
    <td align="right">53.88</td>
    <td align="right">65.56</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">53.66</td>
    <td align="right">59.49</td>
    <td align="right">57.89</td>
    <td align="right">68.45</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.64</td>
    <td align="right">61.52</td>
    <td align="right">59.48</td>
    <td align="right">68.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.60</td>
    <td align="right">69.91</td>
    <td align="right">66.44</td>
    <td align="right">77.69</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">65.96</td>
    <td align="right">70.70</td>
    <td align="right">70.23</td>
    <td align="right">79.99</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">66.72</td>
    <td align="right">71.59</td>
    <td align="right">71.16</td>
    <td align="right">80.95</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">28.86</td>
    <td align="right">46.14</td>
    <td align="right">35.63</td>
    <td align="right">41.38</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.71</td>
    <td align="right">58.20</td>
    <td align="right">40.90</td>
    <td align="right">49.69</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">38.29</td>
    <td align="right">65.75</td>
    <td align="right">42.21</td>
    <td align="right">53.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">38.56</td>
    <td align="right">66.78</td>
    <td align="right">37.68</td>
    <td align="right">54.21</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">43.84</td>
    <td align="right">68.71</td>
    <td align="right">40.08</td>
    <td align="right">56.54</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">47.84</td>
    <td align="right">84.42</td>
    <td align="right">42.06</td>
    <td align="right">62.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">57.43</td>
    <td align="right">89.40</td>
    <td align="right">51.22</td>
    <td align="right">72.19</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">71.70</td>
    <td align="right">103.29</td>
    <td align="right">61.88</td>
    <td align="right">84.39</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">78.46</td>
    <td align="right">112.64</td>
    <td align="right">52.39</td>
    <td align="right">82.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">78.86</td>
    <td align="right">126.21</td>
    <td align="right">63.42</td>
    <td align="right">97.58</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">93.15</td>
    <td align="right">136.63</td>
    <td align="right">74.01</td>
    <td align="right">107.30</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">109.71</td>
    <td align="right">152.99</td>
    <td align="right">64.09</td>
    <td align="right">109.95</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">28.79</td>
    <td align="right">47.01</td>
    <td align="right">47.05</td>
    <td align="right">49.69</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.49</td>
    <td align="right">52.91</td>
    <td align="right">52.80</td>
    <td align="right">55.10</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">38.24</td>
    <td align="right">62.53</td>
    <td align="right">62.71</td>
    <td align="right">65.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">38.40</td>
    <td align="right">60.32</td>
    <td align="right">58.67</td>
    <td align="right">61.61</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">43.66</td>
    <td align="right">68.16</td>
    <td align="right">65.55</td>
    <td align="right">69.47</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">47.59</td>
    <td align="right">80.95</td>
    <td align="right">80.21</td>
    <td align="right">83.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">57.82</td>
    <td align="right">78.35</td>
    <td align="right">76.61</td>
    <td align="right">80.03</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">71.88</td>
    <td align="right">107.18</td>
    <td align="right">104.45</td>
    <td align="right">108.75</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">78.14</td>
    <td align="right">105.73</td>
    <td align="right">105.12</td>
    <td align="right">107.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">78.99</td>
    <td align="right">111.90</td>
    <td align="right">110.63</td>
    <td align="right">115.27</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">93.78</td>
    <td align="right">128.59</td>
    <td align="right">127.26</td>
    <td align="right">132.26</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">109.18</td>
    <td align="right">147.49</td>
    <td align="right">147.47</td>
    <td align="right">150.21</td>
  </tr>
  <tr><th colspan="19">branchful no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">30.81</td>
    <td align="right">45.68</td>
    <td align="right">36.41</td>
    <td align="right">41.75</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.32</td>
    <td align="right">58.26</td>
    <td align="right">40.62</td>
    <td align="right">49.57</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">41.96</td>
    <td align="right">66.29</td>
    <td align="right">43.99</td>
    <td align="right">54.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.65</td>
    <td align="right">67.43</td>
    <td align="right">39.57</td>
    <td align="right">55.53</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">43.88</td>
    <td align="right">68.72</td>
    <td align="right">41.03</td>
    <td align="right">55.95</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">49.73</td>
    <td align="right">86.43</td>
    <td align="right">44.18</td>
    <td align="right">65.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">61.26</td>
    <td align="right">91.03</td>
    <td align="right">53.13</td>
    <td align="right">73.40</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">74.05</td>
    <td align="right">104.64</td>
    <td align="right">62.61</td>
    <td align="right">85.00</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">81.07</td>
    <td align="right">118.47</td>
    <td align="right">43.32</td>
    <td align="right">86.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.85</td>
    <td align="right">127.90</td>
    <td align="right">65.06</td>
    <td align="right">98.43</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">94.87</td>
    <td align="right">137.94</td>
    <td align="right">74.62</td>
    <td align="right">108.40</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">118.68</td>
    <td align="right">165.75</td>
    <td align="right">46.28</td>
    <td align="right">114.86</td>
  </tr>
  <tr><th colspan="19">branchless no prefetch</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">30.87</td>
    <td align="right">46.90</td>
    <td align="right">46.71</td>
    <td align="right">49.31</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.24</td>
    <td align="right">52.01</td>
    <td align="right">51.72</td>
    <td align="right">54.01</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">41.89</td>
    <td align="right">62.55</td>
    <td align="right">62.89</td>
    <td align="right">64.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.91</td>
    <td align="right">61.99</td>
    <td align="right">59.34</td>
    <td align="right">63.25</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">44.23</td>
    <td align="right">68.61</td>
    <td align="right">65.51</td>
    <td align="right">69.07</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">49.24</td>
    <td align="right">80.59</td>
    <td align="right">80.23</td>
    <td align="right">82.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">61.53</td>
    <td align="right">81.95</td>
    <td align="right">79.79</td>
    <td align="right">83.63</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">74.40</td>
    <td align="right">107.65</td>
    <td align="right">106.16</td>
    <td align="right">110.26</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">81.21</td>
    <td align="right">109.51</td>
    <td align="right">107.91</td>
    <td align="right">113.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.68</td>
    <td align="right">115.33</td>
    <td align="right">114.44</td>
    <td align="right">118.85</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">95.11</td>
    <td align="right">129.60</td>
    <td align="right">127.72</td>
    <td align="right">132.88</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">118.13</td>
    <td align="right">153.98</td>
    <td align="right">158.55</td>
    <td align="right">159.15</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
