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
    <td align="right">39.18</td>
    <td align="right">5.48</td>
    <td align="right">4.28</td>
    <td align="right">13.12</td>
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
    <td align="right">11.06</td>
    <td align="right">12.34</td>
    <td align="right">19.66</td>
    <td align="right">17.08</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.91</td>
    <td align="right">4.49</td>
    <td align="right">4.50</td>
    <td align="right">4.49</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.59</td>
    <td align="right">5.12</td>
    <td align="right">5.13</td>
    <td align="right">5.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.46</td>
    <td align="right">18.39</td>
    <td align="right">20.58</td>
    <td align="right">20.90</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.41</td>
    <td align="right">5.18</td>
    <td align="right">5.19</td>
    <td align="right">5.18</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.12</td>
    <td align="right">5.56</td>
    <td align="right">5.55</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.35</td>
    <td align="right">21.98</td>
    <td align="right">20.42</td>
    <td align="right">23.26</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">5.61</td>
    <td align="right">5.61</td>
    <td align="right">5.62</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.56</td>
    <td align="right">6.04</td>
    <td align="right">6.04</td>
    <td align="right">6.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.30</td>
    <td align="right">28.42</td>
    <td align="right">20.86</td>
    <td align="right">29.34</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.98</td>
    <td align="right">5.99</td>
    <td align="right">5.99</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.80</td>
    <td align="right">6.28</td>
    <td align="right">6.28</td>
    <td align="right">6.28</td>
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
    <td align="right">11.06</td>
    <td align="right">13.27</td>
    <td align="right">13.25</td>
    <td align="right">13.21</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.00</td>
    <td align="right">4.59</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.46</td>
    <td align="right">5.12</td>
    <td align="right">5.12</td>
    <td align="right">5.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.60</td>
    <td align="right">20.19</td>
    <td align="right">20.13</td>
    <td align="right">20.12</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.39</td>
    <td align="right">5.16</td>
    <td align="right">5.18</td>
    <td align="right">5.17</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.09</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.44</td>
    <td align="right">24.56</td>
    <td align="right">24.54</td>
    <td align="right">24.44</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.02</td>
    <td align="right">5.64</td>
    <td align="right">5.64</td>
    <td align="right">5.64</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.55</td>
    <td align="right">6.03</td>
    <td align="right">6.03</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.32</td>
    <td align="right">29.18</td>
    <td align="right">29.25</td>
    <td align="right">29.26</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.97</td>
    <td align="right">5.98</td>
    <td align="right">5.97</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.82</td>
    <td align="right">6.29</td>
    <td align="right">6.31</td>
    <td align="right">6.31</td>
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
    <td align="right">9.91</td>
    <td align="right">11.35</td>
    <td align="right">18.88</td>
    <td align="right">15.75</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.00</td>
    <td align="right">4.43</td>
    <td align="right">4.42</td>
    <td align="right">4.43</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.42</td>
    <td align="right">4.85</td>
    <td align="right">4.85</td>
    <td align="right">4.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">14.89</td>
    <td align="right">16.91</td>
    <td align="right">20.28</td>
    <td align="right">19.95</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.34</td>
    <td align="right">4.96</td>
    <td align="right">4.96</td>
    <td align="right">4.95</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.07</td>
    <td align="right">5.27</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">17.52</td>
    <td align="right">20.39</td>
    <td align="right">19.47</td>
    <td align="right">22.50</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.01</td>
    <td align="right">5.30</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.53</td>
    <td align="right">5.93</td>
    <td align="right">5.93</td>
    <td align="right">5.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">21.60</td>
    <td align="right">25.36</td>
    <td align="right">19.84</td>
    <td align="right">26.09</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.94</td>
    <td align="right">5.93</td>
    <td align="right">5.94</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.96</td>
    <td align="right">6.21</td>
    <td align="right">6.23</td>
    <td align="right">6.22</td>
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
    <td align="right">9.89</td>
    <td align="right">13.31</td>
    <td align="right">13.32</td>
    <td align="right">13.34</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.98</td>
    <td align="right">4.42</td>
    <td align="right">4.41</td>
    <td align="right">4.42</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.91</td>
    <td align="right">4.87</td>
    <td align="right">4.86</td>
    <td align="right">4.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.09</td>
    <td align="right">20.39</td>
    <td align="right">20.35</td>
    <td align="right">20.38</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.35</td>
    <td align="right">4.96</td>
    <td align="right">4.95</td>
    <td align="right">4.96</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.06</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
    <td align="right">5.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">17.85</td>
    <td align="right">25.77</td>
    <td align="right">25.79</td>
    <td align="right">25.82</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.52</td>
    <td align="right">5.92</td>
    <td align="right">5.92</td>
    <td align="right">5.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">21.65</td>
    <td align="right">32.02</td>
    <td align="right">32.12</td>
    <td align="right">32.09</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.94</td>
    <td align="right">5.94</td>
    <td align="right">5.94</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.98</td>
    <td align="right">6.22</td>
    <td align="right">6.22</td>
    <td align="right">6.22</td>
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
    <td align="right">5.00</td>
    <td align="right">5.81</td>
    <td align="right">14.05</td>
    <td align="right">11.78</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.54</td>
    <td align="right">7.64</td>
    <td align="right">14.80</td>
    <td align="right">13.22</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.24</td>
    <td align="right">2.97</td>
    <td align="right">2.96</td>
    <td align="right">2.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.86</td>
    <td align="right">8.48</td>
    <td align="right">14.77</td>
    <td align="right">13.61</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.06</td>
    <td align="right">9.72</td>
    <td align="right">16.33</td>
    <td align="right">15.28</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
    <td align="right">2.74</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.21</td>
    <td align="right">12.37</td>
    <td align="right">16.11</td>
    <td align="right">17.57</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.12</td>
    <td align="right">13.00</td>
    <td align="right">17.74</td>
    <td align="right">17.96</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.82</td>
    <td align="right">5.90</td>
    <td align="right">4.20</td>
    <td align="right">14.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.53</td>
    <td align="right">13.61</td>
    <td align="right">15.44</td>
    <td align="right">18.21</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.80</td>
    <td align="right">14.89</td>
    <td align="right">18.67</td>
    <td align="right">19.40</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.87</td>
    <td align="right">5.94</td>
    <td align="right">4.21</td>
    <td align="right">14.79</td>
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
    <td align="right">5.04</td>
    <td align="right">5.67</td>
    <td align="right">5.66</td>
    <td align="right">5.67</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.54</td>
    <td align="right">6.97</td>
    <td align="right">6.96</td>
    <td align="right">6.98</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.26</td>
    <td align="right">2.98</td>
    <td align="right">2.97</td>
    <td align="right">2.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.86</td>
    <td align="right">9.26</td>
    <td align="right">9.26</td>
    <td align="right">9.26</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.08</td>
    <td align="right">9.78</td>
    <td align="right">9.77</td>
    <td align="right">9.77</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.71</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.80</td>
    <td align="right">11.81</td>
    <td align="right">11.73</td>
    <td align="right">11.86</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.11</td>
    <td align="right">13.66</td>
    <td align="right">13.60</td>
    <td align="right">13.76</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.80</td>
    <td align="right">5.91</td>
    <td align="right">5.90</td>
    <td align="right">5.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.50</td>
    <td align="right">12.76</td>
    <td align="right">12.58</td>
    <td align="right">12.76</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.74</td>
    <td align="right">15.17</td>
    <td align="right">15.07</td>
    <td align="right">15.20</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.86</td>
    <td align="right">5.94</td>
    <td align="right">5.93</td>
    <td align="right">5.94</td>
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
    <td align="right">4.70</td>
    <td align="right">5.76</td>
    <td align="right">14.03</td>
    <td align="right">11.59</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.48</td>
    <td align="right">7.42</td>
    <td align="right">14.42</td>
    <td align="right">14.41</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.98</td>
    <td align="right">3.07</td>
    <td align="right">3.07</td>
    <td align="right">3.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.10</td>
    <td align="right">8.53</td>
    <td align="right">14.80</td>
    <td align="right">13.57</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">6.88</td>
    <td align="right">9.57</td>
    <td align="right">16.29</td>
    <td align="right">15.21</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.58</td>
    <td align="right">2.91</td>
    <td align="right">2.91</td>
    <td align="right">2.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">8.60</td>
    <td align="right">12.18</td>
    <td align="right">15.99</td>
    <td align="right">17.10</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.15</td>
    <td align="right">12.80</td>
    <td align="right">17.20</td>
    <td align="right">17.44</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.31</td>
    <td align="right">5.83</td>
    <td align="right">3.84</td>
    <td align="right">14.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.17</td>
    <td align="right">13.79</td>
    <td align="right">15.47</td>
    <td align="right">18.33</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.56</td>
    <td align="right">14.71</td>
    <td align="right">18.16</td>
    <td align="right">19.23</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.38</td>
    <td align="right">5.89</td>
    <td align="right">3.85</td>
    <td align="right">14.67</td>
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
    <td align="right">4.69</td>
    <td align="right">5.57</td>
    <td align="right">5.56</td>
    <td align="right">5.57</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.50</td>
    <td align="right">6.85</td>
    <td align="right">6.84</td>
    <td align="right">6.84</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.97</td>
    <td align="right">3.06</td>
    <td align="right">3.05</td>
    <td align="right">3.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.09</td>
    <td align="right">9.23</td>
    <td align="right">9.23</td>
    <td align="right">9.23</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">6.82</td>
    <td align="right">9.68</td>
    <td align="right">9.69</td>
    <td align="right">9.71</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.57</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">8.60</td>
    <td align="right">10.88</td>
    <td align="right">10.87</td>
    <td align="right">10.88</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.17</td>
    <td align="right">11.86</td>
    <td align="right">11.82</td>
    <td align="right">11.86</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.32</td>
    <td align="right">5.66</td>
    <td align="right">5.66</td>
    <td align="right">5.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.17</td>
    <td align="right">12.44</td>
    <td align="right">12.40</td>
    <td align="right">12.44</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.57</td>
    <td align="right">14.70</td>
    <td align="right">14.56</td>
    <td align="right">14.70</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.37</td>
    <td align="right">5.70</td>
    <td align="right">5.70</td>
    <td align="right">5.69</td>
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
    <td align="right">3.21</td>
    <td align="right">2.79</td>
    <td align="right">2.79</td>
    <td align="right">2.80</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.66</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.78</td>
    <td align="right">4.44</td>
    <td align="right">4.44</td>
    <td align="right">4.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.33</td>
    <td align="right">2.85</td>
    <td align="right">2.88</td>
    <td align="right">2.87</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.49</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.84</td>
    <td align="right">4.57</td>
    <td align="right">4.56</td>
    <td align="right">4.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.58</td>
    <td align="right">5.72</td>
    <td align="right">3.96</td>
    <td align="right">14.34</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.65</td>
    <td align="right">8.26</td>
    <td align="right">6.14</td>
    <td align="right">17.91</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.88</td>
    <td align="right">7.99</td>
    <td align="right">6.14</td>
    <td align="right">17.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.64</td>
    <td align="right">5.76</td>
    <td align="right">3.97</td>
    <td align="right">14.38</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.44</td>
    <td align="right">9.29</td>
    <td align="right">6.15</td>
    <td align="right">18.68</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.65</td>
    <td align="right">9.07</td>
    <td align="right">6.26</td>
    <td align="right">18.38</td>
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
    <td align="right">2.80</td>
    <td align="right">2.78</td>
    <td align="right">2.81</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.63</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.81</td>
    <td align="right">4.44</td>
    <td align="right">4.44</td>
    <td align="right">4.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.34</td>
    <td align="right">2.86</td>
    <td align="right">2.87</td>
    <td align="right">2.86</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.47</td>
    <td align="right">4.17</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.83</td>
    <td align="right">4.55</td>
    <td align="right">4.55</td>
    <td align="right">4.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.57</td>
    <td align="right">5.72</td>
    <td align="right">5.70</td>
    <td align="right">5.73</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.68</td>
    <td align="right">7.90</td>
    <td align="right">7.84</td>
    <td align="right">7.92</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.75</td>
    <td align="right">7.76</td>
    <td align="right">7.68</td>
    <td align="right">7.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.65</td>
    <td align="right">5.77</td>
    <td align="right">5.75</td>
    <td align="right">5.77</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.55</td>
    <td align="right">8.61</td>
    <td align="right">8.75</td>
    <td align="right">8.67</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.57</td>
    <td align="right">8.24</td>
    <td align="right">8.26</td>
    <td align="right">8.54</td>
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
    <td align="right">2.86</td>
    <td align="right">2.86</td>
    <td align="right">2.86</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.50</td>
    <td align="right">4.47</td>
    <td align="right">4.48</td>
    <td align="right">4.48</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.68</td>
    <td align="right">4.29</td>
    <td align="right">4.28</td>
    <td align="right">4.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.05</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.43</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.61</td>
    <td align="right">4.39</td>
    <td align="right">4.39</td>
    <td align="right">4.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.50</td>
    <td align="right">5.55</td>
    <td align="right">3.69</td>
    <td align="right">14.14</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.39</td>
    <td align="right">8.01</td>
    <td align="right">5.93</td>
    <td align="right">17.74</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.43</td>
    <td align="right">7.79</td>
    <td align="right">5.86</td>
    <td align="right">17.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.53</td>
    <td align="right">5.56</td>
    <td align="right">3.68</td>
    <td align="right">14.35</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.03</td>
    <td align="right">9.06</td>
    <td align="right">5.86</td>
    <td align="right">18.53</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.69</td>
    <td align="right">8.65</td>
    <td align="right">5.73</td>
    <td align="right">17.96</td>
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
    <td align="right">2.93</td>
    <td align="right">2.85</td>
    <td align="right">2.85</td>
    <td align="right">2.85</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.47</td>
    <td align="right">4.47</td>
    <td align="right">4.46</td>
    <td align="right">4.47</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.67</td>
    <td align="right">4.28</td>
    <td align="right">4.28</td>
    <td align="right">4.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.03</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.43</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.60</td>
    <td align="right">4.40</td>
    <td align="right">4.40</td>
    <td align="right">4.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.48</td>
    <td align="right">5.47</td>
    <td align="right">5.46</td>
    <td align="right">5.47</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.32</td>
    <td align="right">7.47</td>
    <td align="right">7.45</td>
    <td align="right">7.54</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.45</td>
    <td align="right">7.30</td>
    <td align="right">7.21</td>
    <td align="right">7.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.56</td>
    <td align="right">5.53</td>
    <td align="right">5.52</td>
    <td align="right">5.53</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.04</td>
    <td align="right">8.50</td>
    <td align="right">8.29</td>
    <td align="right">8.40</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.75</td>
    <td align="right">8.21</td>
    <td align="right">8.33</td>
    <td align="right">8.33</td>
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
    <td align="right">7.35</td>
    <td align="right">14.47</td>
    <td align="right">12.71</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.73</td>
    <td align="right">8.85</td>
    <td align="right">18.85</td>
    <td align="right">15.80</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.15</td>
    <td align="right">11.46</td>
    <td align="right">19.40</td>
    <td align="right">16.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.76</td>
    <td align="right">10.39</td>
    <td align="right">14.38</td>
    <td align="right">15.80</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.55</td>
    <td align="right">10.61</td>
    <td align="right">16.19</td>
    <td align="right">17.26</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.96</td>
    <td align="right">14.26</td>
    <td align="right">20.13</td>
    <td align="right">18.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.66</td>
    <td align="right">11.93</td>
    <td align="right">14.09</td>
    <td align="right">16.80</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.99</td>
    <td align="right">13.05</td>
    <td align="right">17.36</td>
    <td align="right">19.66</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.50</td>
    <td align="right">14.82</td>
    <td align="right">18.94</td>
    <td align="right">19.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.87</td>
    <td align="right">14.38</td>
    <td align="right">14.80</td>
    <td align="right">18.52</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.68</td>
    <td align="right">15.37</td>
    <td align="right">16.97</td>
    <td align="right">20.27</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.71</td>
    <td align="right">20.25</td>
    <td align="right">21.20</td>
    <td align="right">23.19</td>
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
    <td align="right">6.42</td>
    <td align="right">6.92</td>
    <td align="right">6.92</td>
    <td align="right">6.92</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.75</td>
    <td align="right">8.47</td>
    <td align="right">8.47</td>
    <td align="right">8.47</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.30</td>
    <td align="right">11.20</td>
    <td align="right">10.86</td>
    <td align="right">11.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.76</td>
    <td align="right">9.90</td>
    <td align="right">9.91</td>
    <td align="right">9.92</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.57</td>
    <td align="right">11.05</td>
    <td align="right">11.04</td>
    <td align="right">11.05</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.07</td>
    <td align="right">14.47</td>
    <td align="right">14.38</td>
    <td align="right">14.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.68</td>
    <td align="right">11.09</td>
    <td align="right">11.08</td>
    <td align="right">11.09</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.97</td>
    <td align="right">13.33</td>
    <td align="right">13.33</td>
    <td align="right">13.34</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.47</td>
    <td align="right">16.38</td>
    <td align="right">16.20</td>
    <td align="right">16.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.88</td>
    <td align="right">14.22</td>
    <td align="right">14.21</td>
    <td align="right">14.23</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.71</td>
    <td align="right">16.28</td>
    <td align="right">16.26</td>
    <td align="right">16.26</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.62</td>
    <td align="right">20.90</td>
    <td align="right">20.99</td>
    <td align="right">21.08</td>
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
    <td align="right">7.32</td>
    <td align="right">14.52</td>
    <td align="right">13.32</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.22</td>
    <td align="right">8.81</td>
    <td align="right">18.50</td>
    <td align="right">15.73</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.10</td>
    <td align="right">10.78</td>
    <td align="right">18.95</td>
    <td align="right">15.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.08</td>
    <td align="right">10.48</td>
    <td align="right">14.32</td>
    <td align="right">15.64</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.66</td>
    <td align="right">10.58</td>
    <td align="right">15.89</td>
    <td align="right">17.20</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.57</td>
    <td align="right">13.68</td>
    <td align="right">19.41</td>
    <td align="right">18.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.09</td>
    <td align="right">11.99</td>
    <td align="right">13.95</td>
    <td align="right">16.98</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.36</td>
    <td align="right">13.05</td>
    <td align="right">16.84</td>
    <td align="right">19.65</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.26</td>
    <td align="right">15.52</td>
    <td align="right">17.37</td>
    <td align="right">19.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.24</td>
    <td align="right">14.52</td>
    <td align="right">14.80</td>
    <td align="right">18.30</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.70</td>
    <td align="right">15.57</td>
    <td align="right">16.51</td>
    <td align="right">20.40</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.63</td>
    <td align="right">19.87</td>
    <td align="right">17.90</td>
    <td align="right">22.55</td>
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
    <td align="right">6.92</td>
    <td align="right">6.92</td>
    <td align="right">6.92</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.19</td>
    <td align="right">8.40</td>
    <td align="right">8.40</td>
    <td align="right">8.40</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">9.85</td>
    <td align="right">10.60</td>
    <td align="right">10.96</td>
    <td align="right">11.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.10</td>
    <td align="right">10.06</td>
    <td align="right">10.04</td>
    <td align="right">10.03</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.59</td>
    <td align="right">11.01</td>
    <td align="right">11.02</td>
    <td align="right">11.01</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.27</td>
    <td align="right">13.15</td>
    <td align="right">13.55</td>
    <td align="right">13.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.08</td>
    <td align="right">11.17</td>
    <td align="right">11.17</td>
    <td align="right">11.18</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.36</td>
    <td align="right">13.38</td>
    <td align="right">13.41</td>
    <td align="right">13.43</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.17</td>
    <td align="right">15.90</td>
    <td align="right">15.91</td>
    <td align="right">15.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.26</td>
    <td align="right">14.43</td>
    <td align="right">14.43</td>
    <td align="right">14.43</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.69</td>
    <td align="right">16.29</td>
    <td align="right">16.31</td>
    <td align="right">16.31</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.06</td>
    <td align="right">19.94</td>
    <td align="right">19.72</td>
    <td align="right">19.95</td>
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
    <td align="right">58.81</td>
    <td align="right">23.35</td>
    <td align="right">14.52</td>
    <td align="right">31.43</td>
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
    <td align="right">18.46</td>
    <td align="right">20.83</td>
    <td align="right">23.54</td>
    <td align="right">22.66</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.17</td>
    <td align="right">5.79</td>
    <td align="right">5.78</td>
    <td align="right">5.74</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.28</td>
    <td align="right">7.02</td>
    <td align="right">7.02</td>
    <td align="right">6.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">46.47</td>
    <td align="right">51.38</td>
    <td align="right">28.62</td>
    <td align="right">40.77</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.80</td>
    <td align="right">11.79</td>
    <td align="right">11.82</td>
    <td align="right">11.83</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.24</td>
    <td align="right">12.25</td>
    <td align="right">12.30</td>
    <td align="right">12.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">85.10</td>
    <td align="right">96.89</td>
    <td align="right">35.73</td>
    <td align="right">67.24</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.66</td>
    <td align="right">18.34</td>
    <td align="right">18.34</td>
    <td align="right">18.34</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">19.21</td>
    <td align="right">19.32</td>
    <td align="right">19.32</td>
    <td align="right">19.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">124.64</td>
    <td align="right">139.51</td>
    <td align="right">42.03</td>
    <td align="right">93.76</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.92</td>
    <td align="right">22.07</td>
    <td align="right">22.07</td>
    <td align="right">22.08</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.93</td>
    <td align="right">25.38</td>
    <td align="right">25.37</td>
    <td align="right">25.38</td>
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
    <td align="right">15.87</td>
    <td align="right">19.09</td>
    <td align="right">19.30</td>
    <td align="right">19.26</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">6.04</td>
    <td align="right">6.37</td>
    <td align="right">6.37</td>
    <td align="right">6.35</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.11</td>
    <td align="right">5.80</td>
    <td align="right">5.80</td>
    <td align="right">5.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">48.48</td>
    <td align="right">52.46</td>
    <td align="right">52.57</td>
    <td align="right">52.55</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.43</td>
    <td align="right">12.47</td>
    <td align="right">12.48</td>
    <td align="right">12.46</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.52</td>
    <td align="right">12.55</td>
    <td align="right">12.60</td>
    <td align="right">12.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.49</td>
    <td align="right">81.27</td>
    <td align="right">81.24</td>
    <td align="right">81.25</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.71</td>
    <td align="right">18.40</td>
    <td align="right">18.39</td>
    <td align="right">18.39</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.78</td>
    <td align="right">18.91</td>
    <td align="right">18.90</td>
    <td align="right">18.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">124.44</td>
    <td align="right">127.35</td>
    <td align="right">127.56</td>
    <td align="right">127.42</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.83</td>
    <td align="right">21.94</td>
    <td align="right">21.94</td>
    <td align="right">21.95</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.81</td>
    <td align="right">25.21</td>
    <td align="right">25.23</td>
    <td align="right">25.24</td>
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
    <td align="right">16.23</td>
    <td align="right">18.70</td>
    <td align="right">22.43</td>
    <td align="right">20.65</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.63</td>
    <td align="right">5.96</td>
    <td align="right">5.92</td>
    <td align="right">5.93</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.91</td>
    <td align="right">6.51</td>
    <td align="right">6.50</td>
    <td align="right">6.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">41.05</td>
    <td align="right">45.40</td>
    <td align="right">27.24</td>
    <td align="right">36.77</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.70</td>
    <td align="right">11.72</td>
    <td align="right">11.71</td>
    <td align="right">11.67</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">12.46</td>
    <td align="right">12.78</td>
    <td align="right">12.78</td>
    <td align="right">12.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">79.48</td>
    <td align="right">91.09</td>
    <td align="right">34.13</td>
    <td align="right">63.89</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.88</td>
    <td align="right">18.12</td>
    <td align="right">18.12</td>
    <td align="right">18.11</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.60</td>
    <td align="right">20.66</td>
    <td align="right">20.66</td>
    <td align="right">20.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">115.47</td>
    <td align="right">131.40</td>
    <td align="right">40.41</td>
    <td align="right">88.63</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.61</td>
    <td align="right">24.55</td>
    <td align="right">24.52</td>
    <td align="right">24.51</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">25.16</td>
    <td align="right">25.22</td>
    <td align="right">25.23</td>
    <td align="right">25.26</td>
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
    <td align="right">14.76</td>
    <td align="right">19.47</td>
    <td align="right">19.50</td>
    <td align="right">19.49</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.43</td>
    <td align="right">5.96</td>
    <td align="right">5.97</td>
    <td align="right">5.97</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.64</td>
    <td align="right">6.22</td>
    <td align="right">6.25</td>
    <td align="right">6.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">48.86</td>
    <td align="right">57.55</td>
    <td align="right">57.53</td>
    <td align="right">57.57</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.92</td>
    <td align="right">11.96</td>
    <td align="right">11.94</td>
    <td align="right">11.95</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">12.86</td>
    <td align="right">13.11</td>
    <td align="right">13.12</td>
    <td align="right">13.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">82.17</td>
    <td align="right">112.05</td>
    <td align="right">111.83</td>
    <td align="right">111.82</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.69</td>
    <td align="right">17.93</td>
    <td align="right">17.96</td>
    <td align="right">18.17</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.67</td>
    <td align="right">20.78</td>
    <td align="right">20.76</td>
    <td align="right">20.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">114.72</td>
    <td align="right">161.16</td>
    <td align="right">160.73</td>
    <td align="right">161.03</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.55</td>
    <td align="right">24.45</td>
    <td align="right">24.44</td>
    <td align="right">24.46</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">25.20</td>
    <td align="right">25.21</td>
    <td align="right">25.21</td>
    <td align="right">25.24</td>
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
    <td align="right">6.30</td>
    <td align="right">7.18</td>
    <td align="right">15.06</td>
    <td align="right">13.83</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.24</td>
    <td align="right">9.65</td>
    <td align="right">16.86</td>
    <td align="right">15.63</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.91</td>
    <td align="right">3.62</td>
    <td align="right">3.65</td>
    <td align="right">3.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">12.77</td>
    <td align="right">15.31</td>
    <td align="right">18.87</td>
    <td align="right">19.76</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.82</td>
    <td align="right">19.16</td>
    <td align="right">23.68</td>
    <td align="right">24.22</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.77</td>
    <td align="right">8.08</td>
    <td align="right">8.05</td>
    <td align="right">8.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.98</td>
    <td align="right">31.66</td>
    <td align="right">25.99</td>
    <td align="right">33.36</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.05</td>
    <td align="right">32.83</td>
    <td align="right">30.14</td>
    <td align="right">34.65</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.04</td>
    <td align="right">20.62</td>
    <td align="right">14.89</td>
    <td align="right">24.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.46</td>
    <td align="right">39.81</td>
    <td align="right">26.61</td>
    <td align="right">39.33</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.47</td>
    <td align="right">44.29</td>
    <td align="right">34.88</td>
    <td align="right">45.98</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.04</td>
    <td align="right">23.74</td>
    <td align="right">16.74</td>
    <td align="right">27.72</td>
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
    <td align="right">6.58</td>
    <td align="right">7.30</td>
    <td align="right">7.27</td>
    <td align="right">7.28</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.42</td>
    <td align="right">9.17</td>
    <td align="right">9.17</td>
    <td align="right">9.18</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.28</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">12.63</td>
    <td align="right">15.95</td>
    <td align="right">15.97</td>
    <td align="right">16.09</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.59</td>
    <td align="right">20.65</td>
    <td align="right">20.67</td>
    <td align="right">20.67</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.59</td>
    <td align="right">7.86</td>
    <td align="right">7.90</td>
    <td align="right">7.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.25</td>
    <td align="right">30.63</td>
    <td align="right">30.66</td>
    <td align="right">30.63</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.02</td>
    <td align="right">34.49</td>
    <td align="right">34.49</td>
    <td align="right">34.53</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.13</td>
    <td align="right">20.93</td>
    <td align="right">20.94</td>
    <td align="right">20.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.52</td>
    <td align="right">41.31</td>
    <td align="right">39.88</td>
    <td align="right">39.63</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.74</td>
    <td align="right">50.72</td>
    <td align="right">52.27</td>
    <td align="right">50.87</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.11</td>
    <td align="right">24.09</td>
    <td align="right">24.08</td>
    <td align="right">24.08</td>
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
    <td align="right">6.67</td>
    <td align="right">7.81</td>
    <td align="right">15.47</td>
    <td align="right">14.00</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.54</td>
    <td align="right">9.85</td>
    <td align="right">16.62</td>
    <td align="right">15.60</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.79</td>
    <td align="right">4.07</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.90</td>
    <td align="right">15.82</td>
    <td align="right">19.13</td>
    <td align="right">20.17</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.58</td>
    <td align="right">19.64</td>
    <td align="right">23.54</td>
    <td align="right">23.58</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.61</td>
    <td align="right">8.49</td>
    <td align="right">8.45</td>
    <td align="right">8.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.31</td>
    <td align="right">30.23</td>
    <td align="right">24.02</td>
    <td align="right">30.57</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.28</td>
    <td align="right">33.07</td>
    <td align="right">29.05</td>
    <td align="right">34.05</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">18.29</td>
    <td align="right">20.39</td>
    <td align="right">14.52</td>
    <td align="right">23.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.23</td>
    <td align="right">38.96</td>
    <td align="right">25.02</td>
    <td align="right">39.01</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.22</td>
    <td align="right">43.21</td>
    <td align="right">33.51</td>
    <td align="right">44.89</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.43</td>
    <td align="right">23.62</td>
    <td align="right">16.35</td>
    <td align="right">27.53</td>
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
    <td align="right">6.36</td>
    <td align="right">7.46</td>
    <td align="right">7.45</td>
    <td align="right">7.44</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">6.71</td>
    <td align="right">8.42</td>
    <td align="right">8.40</td>
    <td align="right">8.41</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.74</td>
    <td align="right">3.97</td>
    <td align="right">3.98</td>
    <td align="right">4.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.52</td>
    <td align="right">16.68</td>
    <td align="right">16.65</td>
    <td align="right">16.61</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.17</td>
    <td align="right">19.63</td>
    <td align="right">19.57</td>
    <td align="right">19.58</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.52</td>
    <td align="right">8.33</td>
    <td align="right">8.35</td>
    <td align="right">8.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.31</td>
    <td align="right">31.21</td>
    <td align="right">31.21</td>
    <td align="right">32.91</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.11</td>
    <td align="right">32.06</td>
    <td align="right">32.06</td>
    <td align="right">32.05</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">18.52</td>
    <td align="right">20.81</td>
    <td align="right">20.82</td>
    <td align="right">20.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.28</td>
    <td align="right">39.16</td>
    <td align="right">39.17</td>
    <td align="right">39.19</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.07</td>
    <td align="right">50.31</td>
    <td align="right">50.33</td>
    <td align="right">50.31</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.39</td>
    <td align="right">23.72</td>
    <td align="right">23.73</td>
    <td align="right">23.74</td>
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
    <td align="right">4.68</td>
    <td align="right">4.32</td>
    <td align="right">4.30</td>
    <td align="right">4.34</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.97</td>
    <td align="right">6.05</td>
    <td align="right">6.09</td>
    <td align="right">6.06</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.74</td>
    <td align="right">5.43</td>
    <td align="right">5.43</td>
    <td align="right">5.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.81</td>
    <td align="right">8.64</td>
    <td align="right">8.63</td>
    <td align="right">8.62</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.33</td>
    <td align="right">10.38</td>
    <td align="right">10.34</td>
    <td align="right">10.33</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.18</td>
    <td align="right">12.22</td>
    <td align="right">12.13</td>
    <td align="right">12.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.82</td>
    <td align="right">20.65</td>
    <td align="right">14.95</td>
    <td align="right">24.76</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.33</td>
    <td align="right">26.57</td>
    <td align="right">21.89</td>
    <td align="right">31.16</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.08</td>
    <td align="right">26.63</td>
    <td align="right">21.95</td>
    <td align="right">30.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.95</td>
    <td align="right">23.79</td>
    <td align="right">16.58</td>
    <td align="right">27.95</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.24</td>
    <td align="right">36.34</td>
    <td align="right">25.04</td>
    <td align="right">36.75</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.62</td>
    <td align="right">35.47</td>
    <td align="right">25.25</td>
    <td align="right">36.74</td>
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
    <td align="right">4.43</td>
    <td align="right">4.11</td>
    <td align="right">4.12</td>
    <td align="right">4.11</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.73</td>
    <td align="right">6.87</td>
    <td align="right">6.89</td>
    <td align="right">6.88</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.41</td>
    <td align="right">6.25</td>
    <td align="right">6.28</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.32</td>
    <td align="right">8.16</td>
    <td align="right">8.15</td>
    <td align="right">8.14</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.40</td>
    <td align="right">10.43</td>
    <td align="right">10.45</td>
    <td align="right">10.40</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.24</td>
    <td align="right">12.23</td>
    <td align="right">12.16</td>
    <td align="right">12.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.92</td>
    <td align="right">20.95</td>
    <td align="right">21.03</td>
    <td align="right">20.98</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.51</td>
    <td align="right">26.30</td>
    <td align="right">26.29</td>
    <td align="right">26.35</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.39</td>
    <td align="right">26.71</td>
    <td align="right">26.70</td>
    <td align="right">26.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.92</td>
    <td align="right">24.08</td>
    <td align="right">24.09</td>
    <td align="right">24.09</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.23</td>
    <td align="right">31.84</td>
    <td align="right">31.87</td>
    <td align="right">31.84</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.47</td>
    <td align="right">32.56</td>
    <td align="right">32.99</td>
    <td align="right">32.30</td>
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
    <td align="right">4.18</td>
    <td align="right">4.38</td>
    <td align="right">4.36</td>
    <td align="right">4.40</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.84</td>
    <td align="right">5.99</td>
    <td align="right">6.00</td>
    <td align="right">6.00</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.10</td>
    <td align="right">5.87</td>
    <td align="right">5.86</td>
    <td align="right">5.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.99</td>
    <td align="right">8.75</td>
    <td align="right">8.76</td>
    <td align="right">8.75</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.42</td>
    <td align="right">10.41</td>
    <td align="right">10.42</td>
    <td align="right">10.40</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.15</td>
    <td align="right">12.04</td>
    <td align="right">12.01</td>
    <td align="right">11.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.46</td>
    <td align="right">18.90</td>
    <td align="right">14.47</td>
    <td align="right">23.32</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.50</td>
    <td align="right">26.30</td>
    <td align="right">19.95</td>
    <td align="right">30.04</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.82</td>
    <td align="right">26.20</td>
    <td align="right">19.90</td>
    <td align="right">29.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.61</td>
    <td align="right">21.48</td>
    <td align="right">16.18</td>
    <td align="right">27.27</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">30.83</td>
    <td align="right">31.84</td>
    <td align="right">22.80</td>
    <td align="right">36.10</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.37</td>
    <td align="right">31.71</td>
    <td align="right">22.83</td>
    <td align="right">35.66</td>
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
    <td align="right">3.93</td>
    <td align="right">4.08</td>
    <td align="right">4.06</td>
    <td align="right">4.11</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.21</td>
    <td align="right">6.30</td>
    <td align="right">6.28</td>
    <td align="right">6.29</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.59</td>
    <td align="right">5.22</td>
    <td align="right">5.22</td>
    <td align="right">5.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.74</td>
    <td align="right">8.48</td>
    <td align="right">8.47</td>
    <td align="right">8.54</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.25</td>
    <td align="right">10.24</td>
    <td align="right">10.23</td>
    <td align="right">10.23</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.44</td>
    <td align="right">12.38</td>
    <td align="right">12.36</td>
    <td align="right">12.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.52</td>
    <td align="right">20.72</td>
    <td align="right">20.72</td>
    <td align="right">20.73</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.37</td>
    <td align="right">25.79</td>
    <td align="right">25.81</td>
    <td align="right">25.79</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.29</td>
    <td align="right">26.07</td>
    <td align="right">26.07</td>
    <td align="right">26.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.51</td>
    <td align="right">23.70</td>
    <td align="right">23.69</td>
    <td align="right">23.71</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">30.82</td>
    <td align="right">31.32</td>
    <td align="right">31.28</td>
    <td align="right">31.29</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.22</td>
    <td align="right">31.70</td>
    <td align="right">31.73</td>
    <td align="right">31.69</td>
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
    <td align="right">7.92</td>
    <td align="right">8.88</td>
    <td align="right">15.80</td>
    <td align="right">14.78</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.41</td>
    <td align="right">11.23</td>
    <td align="right">20.84</td>
    <td align="right">18.56</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.56</td>
    <td align="right">16.24</td>
    <td align="right">21.71</td>
    <td align="right">21.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.00</td>
    <td align="right">19.26</td>
    <td align="right">18.74</td>
    <td align="right">22.65</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.68</td>
    <td align="right">21.73</td>
    <td align="right">22.31</td>
    <td align="right">25.94</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.33</td>
    <td align="right">30.86</td>
    <td align="right">27.92</td>
    <td align="right">31.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.48</td>
    <td align="right">28.05</td>
    <td align="right">21.85</td>
    <td align="right">31.27</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.46</td>
    <td align="right">34.04</td>
    <td align="right">27.24</td>
    <td align="right">37.74</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.44</td>
    <td align="right">46.53</td>
    <td align="right">31.94</td>
    <td align="right">41.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.91</td>
    <td align="right">42.66</td>
    <td align="right">25.02</td>
    <td align="right">43.05</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.49</td>
    <td align="right">51.09</td>
    <td align="right">29.75</td>
    <td align="right">49.22</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">74.74</td>
    <td align="right">68.54</td>
    <td align="right">39.01</td>
    <td align="right">56.92</td>
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
    <td align="right">8.36</td>
    <td align="right">8.96</td>
    <td align="right">8.99</td>
    <td align="right">8.98</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.57</td>
    <td align="right">11.31</td>
    <td align="right">11.33</td>
    <td align="right">11.35</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.53</td>
    <td align="right">13.61</td>
    <td align="right">13.62</td>
    <td align="right">13.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.19</td>
    <td align="right">17.36</td>
    <td align="right">17.44</td>
    <td align="right">17.39</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.47</td>
    <td align="right">22.98</td>
    <td align="right">22.94</td>
    <td align="right">23.01</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.58</td>
    <td align="right">31.94</td>
    <td align="right">32.11</td>
    <td align="right">31.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.07</td>
    <td align="right">28.18</td>
    <td align="right">28.09</td>
    <td align="right">28.10</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.76</td>
    <td align="right">41.03</td>
    <td align="right">41.08</td>
    <td align="right">40.94</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.89</td>
    <td align="right">50.17</td>
    <td align="right">50.11</td>
    <td align="right">50.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.07</td>
    <td align="right">43.23</td>
    <td align="right">43.20</td>
    <td align="right">43.34</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.17</td>
    <td align="right">51.60</td>
    <td align="right">51.60</td>
    <td align="right">51.52</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">74.81</td>
    <td align="right">74.64</td>
    <td align="right">74.62</td>
    <td align="right">74.63</td>
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
    <td align="right">8.26</td>
    <td align="right">9.19</td>
    <td align="right">16.04</td>
    <td align="right">15.65</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.32</td>
    <td align="right">10.49</td>
    <td align="right">20.12</td>
    <td align="right">17.82</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.03</td>
    <td align="right">14.86</td>
    <td align="right">21.89</td>
    <td align="right">18.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.36</td>
    <td align="right">18.33</td>
    <td align="right">18.65</td>
    <td align="right">24.09</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.72</td>
    <td align="right">20.94</td>
    <td align="right">21.11</td>
    <td align="right">25.24</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">26.04</td>
    <td align="right">27.35</td>
    <td align="right">23.08</td>
    <td align="right">28.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.57</td>
    <td align="right">27.73</td>
    <td align="right">21.51</td>
    <td align="right">31.01</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.86</td>
    <td align="right">34.02</td>
    <td align="right">26.00</td>
    <td align="right">37.52</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.80</td>
    <td align="right">46.88</td>
    <td align="right">24.62</td>
    <td align="right">40.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.46</td>
    <td align="right">43.02</td>
    <td align="right">25.00</td>
    <td align="right">42.59</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">50.98</td>
    <td align="right">50.89</td>
    <td align="right">28.06</td>
    <td align="right">48.47</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">74.02</td>
    <td align="right">66.19</td>
    <td align="right">27.28</td>
    <td align="right">55.17</td>
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
    <td align="right">8.39</td>
    <td align="right">9.05</td>
    <td align="right">9.00</td>
    <td align="right">9.03</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.86</td>
    <td align="right">11.01</td>
    <td align="right">11.02</td>
    <td align="right">11.07</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.19</td>
    <td align="right">14.34</td>
    <td align="right">14.33</td>
    <td align="right">14.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.84</td>
    <td align="right">17.75</td>
    <td align="right">17.77</td>
    <td align="right">17.82</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.97</td>
    <td align="right">22.06</td>
    <td align="right">22.10</td>
    <td align="right">22.17</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.32</td>
    <td align="right">30.07</td>
    <td align="right">30.15</td>
    <td align="right">30.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.26</td>
    <td align="right">31.44</td>
    <td align="right">31.40</td>
    <td align="right">31.37</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.76</td>
    <td align="right">40.59</td>
    <td align="right">40.46</td>
    <td align="right">40.45</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.80</td>
    <td align="right">49.24</td>
    <td align="right">49.30</td>
    <td align="right">49.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.47</td>
    <td align="right">43.26</td>
    <td align="right">43.30</td>
    <td align="right">43.41</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.12</td>
    <td align="right">51.58</td>
    <td align="right">51.59</td>
    <td align="right">51.62</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">74.26</td>
    <td align="right">72.34</td>
    <td align="right">72.36</td>
    <td align="right">72.30</td>
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
    <td align="right">26.31</td>
    <td align="right">6.51</td>
    <td align="right">4.36</td>
    <td align="right">13.26</td>
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
    <td align="right">10.74</td>
    <td align="right">10.81</td>
    <td align="right">18.90</td>
    <td align="right">15.91</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.07</td>
    <td align="right">4.10</td>
    <td align="right">4.11</td>
    <td align="right">4.09</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.06</td>
    <td align="right">4.61</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.62</td>
    <td align="right">15.51</td>
    <td align="right">20.18</td>
    <td align="right">19.59</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.58</td>
    <td align="right">4.69</td>
    <td align="right">4.69</td>
    <td align="right">4.69</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.56</td>
    <td align="right">5.26</td>
    <td align="right">5.25</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.91</td>
    <td align="right">18.94</td>
    <td align="right">19.19</td>
    <td align="right">21.74</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.93</td>
    <td align="right">5.75</td>
    <td align="right">5.74</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.28</td>
    <td align="right">23.17</td>
    <td align="right">19.85</td>
    <td align="right">24.26</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.41</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.31</td>
    <td align="right">3.44</td>
    <td align="right">3.45</td>
    <td align="right">3.45</td>
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
    <td align="right">10.30</td>
    <td align="right">10.93</td>
    <td align="right">10.92</td>
    <td align="right">10.95</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="right">4.08</td>
    <td align="right">4.10</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.07</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="right">4.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.66</td>
    <td align="right">14.68</td>
    <td align="right">14.66</td>
    <td align="right">14.68</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.60</td>
    <td align="right">4.69</td>
    <td align="right">4.69</td>
    <td align="right">4.69</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.57</td>
    <td align="right">5.27</td>
    <td align="right">5.27</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.74</td>
    <td align="right">17.50</td>
    <td align="right">17.50</td>
    <td align="right">17.55</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">5.30</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.95</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.36</td>
    <td align="right">25.10</td>
    <td align="right">25.10</td>
    <td align="right">25.07</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.42</td>
    <td align="right">5.75</td>
    <td align="right">5.76</td>
    <td align="right">5.76</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.30</td>
    <td align="right">3.43</td>
    <td align="right">3.44</td>
    <td align="right">3.45</td>
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
    <td align="right">10.37</td>
    <td align="right">10.44</td>
    <td align="right">18.57</td>
    <td align="right">16.14</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.49</td>
    <td align="right">2.49</td>
    <td align="right">2.46</td>
    <td align="right">2.47</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.04</td>
    <td align="right">1.96</td>
    <td align="right">1.96</td>
    <td align="right">1.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.28</td>
    <td align="right">15.36</td>
    <td align="right">20.22</td>
    <td align="right">19.20</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.03</td>
    <td align="right">2.71</td>
    <td align="right">2.73</td>
    <td align="right">2.74</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.47</td>
    <td align="right">2.22</td>
    <td align="right">2.24</td>
    <td align="right">2.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.49</td>
    <td align="right">18.67</td>
    <td align="right">19.25</td>
    <td align="right">21.72</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.43</td>
    <td align="right">2.90</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.91</td>
    <td align="right">2.40</td>
    <td align="right">2.38</td>
    <td align="right">2.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.79</td>
    <td align="right">22.94</td>
    <td align="right">19.51</td>
    <td align="right">24.07</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">4.83</td>
    <td align="right">3.20</td>
    <td align="right">3.19</td>
    <td align="right">3.19</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.25</td>
    <td align="right">2.53</td>
    <td align="right">2.52</td>
    <td align="right">2.53</td>
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
    <td align="right">10.34</td>
    <td align="right">11.42</td>
    <td align="right">11.43</td>
    <td align="right">11.28</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.50</td>
    <td align="right">2.51</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.04</td>
    <td align="right">1.95</td>
    <td align="right">1.97</td>
    <td align="right">1.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.36</td>
    <td align="right">16.88</td>
    <td align="right">17.22</td>
    <td align="right">17.56</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.02</td>
    <td align="right">2.72</td>
    <td align="right">2.72</td>
    <td align="right">2.72</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.46</td>
    <td align="right">2.23</td>
    <td align="right">2.22</td>
    <td align="right">2.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.54</td>
    <td align="right">21.14</td>
    <td align="right">21.13</td>
    <td align="right">21.00</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.45</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="right">2.90</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.90</td>
    <td align="right">2.40</td>
    <td align="right">2.40</td>
    <td align="right">2.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.86</td>
    <td align="right">26.73</td>
    <td align="right">26.39</td>
    <td align="right">26.18</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">4.83</td>
    <td align="right">3.23</td>
    <td align="right">3.22</td>
    <td align="right">3.21</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.23</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="right">2.57</td>
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
    <td align="right">3.23</td>
    <td align="right">5.57</td>
    <td align="right">13.76</td>
    <td align="right">11.71</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.34</td>
    <td align="right">5.57</td>
    <td align="right">13.13</td>
    <td align="right">11.01</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.89</td>
    <td align="right">2.69</td>
    <td align="right">2.69</td>
    <td align="right">2.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.35</td>
    <td align="right">8.22</td>
    <td align="right">14.55</td>
    <td align="right">13.63</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.01</td>
    <td align="right">8.20</td>
    <td align="right">14.47</td>
    <td align="right">13.77</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.77</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.81</td>
    <td align="right">11.61</td>
    <td align="right">15.85</td>
    <td align="right">16.68</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.98</td>
    <td align="right">11.24</td>
    <td align="right">15.29</td>
    <td align="right">16.19</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.40</td>
    <td align="right">4.45</td>
    <td align="right">3.11</td>
    <td align="right">13.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.21</td>
    <td align="right">12.74</td>
    <td align="right">15.19</td>
    <td align="right">17.71</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.95</td>
    <td align="right">12.92</td>
    <td align="right">15.58</td>
    <td align="right">17.33</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.44</td>
    <td align="right">4.49</td>
    <td align="right">3.10</td>
    <td align="right">13.64</td>
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
    <td align="right">3.88</td>
    <td align="right">3.88</td>
    <td align="right">3.87</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.34</td>
    <td align="right">3.73</td>
    <td align="right">3.70</td>
    <td align="right">3.72</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.93</td>
    <td align="right">2.67</td>
    <td align="right">2.67</td>
    <td align="right">2.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.43</td>
    <td align="right">4.82</td>
    <td align="right">4.83</td>
    <td align="right">4.83</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.06</td>
    <td align="right">4.93</td>
    <td align="right">4.93</td>
    <td align="right">4.93</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.79</td>
    <td align="right">7.71</td>
    <td align="right">7.71</td>
    <td align="right">7.74</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">6.02</td>
    <td align="right">7.43</td>
    <td align="right">7.42</td>
    <td align="right">7.51</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.40</td>
    <td align="right">4.47</td>
    <td align="right">4.47</td>
    <td align="right">4.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.20</td>
    <td align="right">8.20</td>
    <td align="right">8.21</td>
    <td align="right">8.22</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.91</td>
    <td align="right">8.19</td>
    <td align="right">8.34</td>
    <td align="right">8.33</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.44</td>
    <td align="right">4.50</td>
    <td align="right">4.50</td>
    <td align="right">4.50</td>
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
    <td align="right">3.12</td>
    <td align="right">5.63</td>
    <td align="right">14.93</td>
    <td align="right">11.27</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.17</td>
    <td align="right">5.34</td>
    <td align="right">12.91</td>
    <td align="right">10.82</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.64</td>
    <td align="right">2.62</td>
    <td align="right">2.62</td>
    <td align="right">2.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.95</td>
    <td align="right">8.09</td>
    <td align="right">15.07</td>
    <td align="right">13.80</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">3.82</td>
    <td align="right">7.99</td>
    <td align="right">14.78</td>
    <td align="right">13.21</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.23</td>
    <td align="right">2.51</td>
    <td align="right">2.51</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.33</td>
    <td align="right">11.38</td>
    <td align="right">15.50</td>
    <td align="right">16.15</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.58</td>
    <td align="right">11.04</td>
    <td align="right">14.75</td>
    <td align="right">15.38</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.22</td>
    <td align="right">4.07</td>
    <td align="right">2.99</td>
    <td align="right">13.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">5.76</td>
    <td align="right">12.91</td>
    <td align="right">15.30</td>
    <td align="right">17.07</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.69</td>
    <td align="right">12.97</td>
    <td align="right">15.14</td>
    <td align="right">17.21</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.27</td>
    <td align="right">4.10</td>
    <td align="right">2.98</td>
    <td align="right">13.19</td>
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
    <td align="right">3.19</td>
    <td align="right">3.20</td>
    <td align="right">3.19</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.19</td>
    <td align="right">3.28</td>
    <td align="right">3.28</td>
    <td align="right">3.32</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.61</td>
    <td align="right">2.64</td>
    <td align="right">2.62</td>
    <td align="right">2.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.98</td>
    <td align="right">4.94</td>
    <td align="right">4.98</td>
    <td align="right">5.00</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">3.91</td>
    <td align="right">4.92</td>
    <td align="right">4.91</td>
    <td align="right">4.90</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.25</td>
    <td align="right">2.52</td>
    <td align="right">2.52</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.37</td>
    <td align="right">7.16</td>
    <td align="right">7.19</td>
    <td align="right">7.21</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.57</td>
    <td align="right">7.36</td>
    <td align="right">7.23</td>
    <td align="right">7.36</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.21</td>
    <td align="right">4.29</td>
    <td align="right">4.29</td>
    <td align="right">4.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">5.80</td>
    <td align="right">8.60</td>
    <td align="right">8.45</td>
    <td align="right">8.55</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.79</td>
    <td align="right">8.77</td>
    <td align="right">8.81</td>
    <td align="right">9.03</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.26</td>
    <td align="right">4.32</td>
    <td align="right">4.32</td>
    <td align="right">4.34</td>
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
    <td align="right">2.48</td>
    <td align="right">2.49</td>
    <td align="right">2.48</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.89</td>
    <td align="right">4.18</td>
    <td align="right">4.17</td>
    <td align="right">4.18</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.06</td>
    <td align="right">4.02</td>
    <td align="right">4.01</td>
    <td align="right">4.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.01</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.49</td>
    <td align="right">3.88</td>
    <td align="right">3.88</td>
    <td align="right">3.88</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.24</td>
    <td align="right">4.11</td>
    <td align="right">4.10</td>
    <td align="right">4.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.47</td>
    <td align="right">4.23</td>
    <td align="right">2.91</td>
    <td align="right">13.33</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.82</td>
    <td align="right">5.98</td>
    <td align="right">4.90</td>
    <td align="right">16.55</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.02</td>
    <td align="right">6.11</td>
    <td align="right">4.39</td>
    <td align="right">15.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.51</td>
    <td align="right">4.26</td>
    <td align="right">2.93</td>
    <td align="right">13.41</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.91</td>
    <td align="right">6.97</td>
    <td align="right">4.94</td>
    <td align="right">17.17</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.20</td>
    <td align="right">6.77</td>
    <td align="right">4.91</td>
    <td align="right">16.66</td>
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
    <td align="right">2.84</td>
    <td align="right">2.47</td>
    <td align="right">2.48</td>
    <td align="right">2.49</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.89</td>
    <td align="right">4.17</td>
    <td align="right">4.17</td>
    <td align="right">4.18</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.06</td>
    <td align="right">4.02</td>
    <td align="right">4.03</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.98</td>
    <td align="right">2.53</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.54</td>
    <td align="right">3.90</td>
    <td align="right">3.90</td>
    <td align="right">3.88</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.25</td>
    <td align="right">4.12</td>
    <td align="right">4.12</td>
    <td align="right">4.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.47</td>
    <td align="right">4.21</td>
    <td align="right">4.20</td>
    <td align="right">4.21</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.83</td>
    <td align="right">6.20</td>
    <td align="right">6.45</td>
    <td align="right">6.48</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.02</td>
    <td align="right">6.22</td>
    <td align="right">6.23</td>
    <td align="right">6.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.51</td>
    <td align="right">4.22</td>
    <td align="right">4.22</td>
    <td align="right">4.23</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.92</td>
    <td align="right">7.31</td>
    <td align="right">7.21</td>
    <td align="right">7.38</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.24</td>
    <td align="right">6.99</td>
    <td align="right">7.11</td>
    <td align="right">7.12</td>
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
    <td align="right">2.67</td>
    <td align="right">2.35</td>
    <td align="right">2.35</td>
    <td align="right">2.37</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.67</td>
    <td align="right">3.98</td>
    <td align="right">3.97</td>
    <td align="right">3.99</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.87</td>
    <td align="right">3.96</td>
    <td align="right">3.94</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.73</td>
    <td align="right">2.39</td>
    <td align="right">2.42</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.15</td>
    <td align="right">3.82</td>
    <td align="right">3.82</td>
    <td align="right">3.82</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.05</td>
    <td align="right">4.04</td>
    <td align="right">4.04</td>
    <td align="right">4.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.47</td>
    <td align="right">4.09</td>
    <td align="right">2.78</td>
    <td align="right">13.04</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.51</td>
    <td align="right">5.64</td>
    <td align="right">4.01</td>
    <td align="right">16.16</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">5.85</td>
    <td align="right">5.51</td>
    <td align="right">3.83</td>
    <td align="right">16.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.45</td>
    <td align="right">4.09</td>
    <td align="right">2.76</td>
    <td align="right">12.94</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.49</td>
    <td align="right">6.53</td>
    <td align="right">4.01</td>
    <td align="right">16.81</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.17</td>
    <td align="right">6.87</td>
    <td align="right">3.88</td>
    <td align="right">16.63</td>
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
    <td align="right">2.62</td>
    <td align="right">2.35</td>
    <td align="right">2.34</td>
    <td align="right">2.36</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.65</td>
    <td align="right">3.99</td>
    <td align="right">3.98</td>
    <td align="right">3.99</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.93</td>
    <td align="right">3.95</td>
    <td align="right">3.95</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.70</td>
    <td align="right">2.41</td>
    <td align="right">2.40</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.15</td>
    <td align="right">3.82</td>
    <td align="right">3.82</td>
    <td align="right">3.82</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.06</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.44</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.45</td>
    <td align="right">5.89</td>
    <td align="right">5.92</td>
    <td align="right">5.92</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">5.86</td>
    <td align="right">5.53</td>
    <td align="right">5.47</td>
    <td align="right">5.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.46</td>
    <td align="right">4.08</td>
    <td align="right">4.09</td>
    <td align="right">4.09</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.74</td>
    <td align="right">7.16</td>
    <td align="right">6.90</td>
    <td align="right">7.16</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.16</td>
    <td align="right">7.11</td>
    <td align="right">6.71</td>
    <td align="right">7.09</td>
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
    <td align="right">6.33</td>
    <td align="right">6.48</td>
    <td align="right">13.77</td>
    <td align="right">12.30</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.77</td>
    <td align="right">7.85</td>
    <td align="right">18.11</td>
    <td align="right">14.96</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.15</td>
    <td align="right">9.58</td>
    <td align="right">18.48</td>
    <td align="right">14.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.72</td>
    <td align="right">8.93</td>
    <td align="right">13.42</td>
    <td align="right">14.43</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.55</td>
    <td align="right">9.27</td>
    <td align="right">15.38</td>
    <td align="right">16.15</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.75</td>
    <td align="right">13.43</td>
    <td align="right">19.91</td>
    <td align="right">18.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.95</td>
    <td align="right">10.70</td>
    <td align="right">13.08</td>
    <td align="right">16.16</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">16.13</td>
    <td align="right">12.04</td>
    <td align="right">16.50</td>
    <td align="right">18.11</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.69</td>
    <td align="right">14.39</td>
    <td align="right">18.23</td>
    <td align="right">19.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.30</td>
    <td align="right">13.05</td>
    <td align="right">13.97</td>
    <td align="right">17.63</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.47</td>
    <td align="right">13.95</td>
    <td align="right">15.65</td>
    <td align="right">19.43</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.83</td>
    <td align="right">20.11</td>
    <td align="right">22.67</td>
    <td align="right">23.11</td>
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
    <td align="right">6.35</td>
    <td align="right">6.65</td>
    <td align="right">6.67</td>
    <td align="right">6.68</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.76</td>
    <td align="right">8.02</td>
    <td align="right">8.02</td>
    <td align="right">8.05</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.25</td>
    <td align="right">10.46</td>
    <td align="right">10.10</td>
    <td align="right">10.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.71</td>
    <td align="right">9.03</td>
    <td align="right">9.03</td>
    <td align="right">9.03</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.56</td>
    <td align="right">10.28</td>
    <td align="right">10.28</td>
    <td align="right">10.28</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.82</td>
    <td align="right">14.37</td>
    <td align="right">13.89</td>
    <td align="right">14.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.99</td>
    <td align="right">10.87</td>
    <td align="right">10.86</td>
    <td align="right">10.87</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">16.10</td>
    <td align="right">12.43</td>
    <td align="right">12.41</td>
    <td align="right">12.42</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.63</td>
    <td align="right">15.51</td>
    <td align="right">14.54</td>
    <td align="right">15.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.31</td>
    <td align="right">13.77</td>
    <td align="right">13.76</td>
    <td align="right">13.77</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.13</td>
    <td align="right">15.45</td>
    <td align="right">15.43</td>
    <td align="right">15.43</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.45</td>
    <td align="right">20.44</td>
    <td align="right">20.60</td>
    <td align="right">20.58</td>
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
    <td align="right">6.00</td>
    <td align="right">6.60</td>
    <td align="right">14.19</td>
    <td align="right">12.40</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.74</td>
    <td align="right">7.75</td>
    <td align="right">17.81</td>
    <td align="right">15.25</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.35</td>
    <td align="right">9.76</td>
    <td align="right">18.34</td>
    <td align="right">14.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.15</td>
    <td align="right">9.14</td>
    <td align="right">13.89</td>
    <td align="right">15.52</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.72</td>
    <td align="right">9.25</td>
    <td align="right">15.02</td>
    <td align="right">16.00</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.81</td>
    <td align="right">12.39</td>
    <td align="right">19.55</td>
    <td align="right">17.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.02</td>
    <td align="right">11.16</td>
    <td align="right">13.78</td>
    <td align="right">16.53</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">16.18</td>
    <td align="right">11.91</td>
    <td align="right">16.17</td>
    <td align="right">18.30</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.78</td>
    <td align="right">14.89</td>
    <td align="right">16.63</td>
    <td align="right">18.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.35</td>
    <td align="right">13.44</td>
    <td align="right">14.22</td>
    <td align="right">17.44</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.81</td>
    <td align="right">13.45</td>
    <td align="right">15.59</td>
    <td align="right">19.47</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.62</td>
    <td align="right">20.89</td>
    <td align="right">19.72</td>
    <td align="right">23.20</td>
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
    <td align="right">5.96</td>
    <td align="right">4.14</td>
    <td align="right">4.14</td>
    <td align="right">4.20</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.72</td>
    <td align="right">7.99</td>
    <td align="right">7.99</td>
    <td align="right">7.97</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.16</td>
    <td align="right">9.07</td>
    <td align="right">9.73</td>
    <td align="right">9.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.20</td>
    <td align="right">6.48</td>
    <td align="right">6.45</td>
    <td align="right">6.40</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">14.75</td>
    <td align="right">10.18</td>
    <td align="right">10.18</td>
    <td align="right">10.17</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.55</td>
    <td align="right">12.73</td>
    <td align="right">12.16</td>
    <td align="right">11.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.05</td>
    <td align="right">7.37</td>
    <td align="right">7.28</td>
    <td align="right">7.31</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.67</td>
    <td align="right">12.41</td>
    <td align="right">12.39</td>
    <td align="right">12.40</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.65</td>
    <td align="right">14.07</td>
    <td align="right">14.32</td>
    <td align="right">14.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.36</td>
    <td align="right">9.29</td>
    <td align="right">9.20</td>
    <td align="right">9.31</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.15</td>
    <td align="right">15.24</td>
    <td align="right">15.24</td>
    <td align="right">15.23</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">22.08</td>
    <td align="right">19.62</td>
    <td align="right">19.43</td>
    <td align="right">19.74</td>
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
    <td align="right">52.14</td>
    <td align="right">23.66</td>
    <td align="right">14.52</td>
    <td align="right">31.44</td>
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
    <td align="right">14.84</td>
    <td align="right">14.92</td>
    <td align="right">21.52</td>
    <td align="right">18.79</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.30</td>
    <td align="right">5.34</td>
    <td align="right">5.33</td>
    <td align="right">5.35</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.38</td>
    <td align="right">5.98</td>
    <td align="right">6.00</td>
    <td align="right">6.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">46.81</td>
    <td align="right">47.24</td>
    <td align="right">27.56</td>
    <td align="right">37.73</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.66</td>
    <td align="right">10.64</td>
    <td align="right">10.64</td>
    <td align="right">10.65</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.04</td>
    <td align="right">12.01</td>
    <td align="right">12.03</td>
    <td align="right">12.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">82.98</td>
    <td align="right">82.02</td>
    <td align="right">32.29</td>
    <td align="right">58.27</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.24</td>
    <td align="right">18.15</td>
    <td align="right">18.16</td>
    <td align="right">18.21</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.11</td>
    <td align="right">18.91</td>
    <td align="right">18.92</td>
    <td align="right">18.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">120.31</td>
    <td align="right">114.53</td>
    <td align="right">38.22</td>
    <td align="right">78.78</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.01</td>
    <td align="right">21.76</td>
    <td align="right">21.80</td>
    <td align="right">21.76</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.73</td>
    <td align="right">15.31</td>
    <td align="right">15.31</td>
    <td align="right">15.30</td>
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
    <td align="right">16.04</td>
    <td align="right">16.73</td>
    <td align="right">16.78</td>
    <td align="right">16.80</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.54</td>
    <td align="right">5.56</td>
    <td align="right">5.61</td>
    <td align="right">5.55</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.32</td>
    <td align="right">5.88</td>
    <td align="right">5.89</td>
    <td align="right">5.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">43.15</td>
    <td align="right">37.98</td>
    <td align="right">37.95</td>
    <td align="right">37.97</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.05</td>
    <td align="right">10.97</td>
    <td align="right">10.97</td>
    <td align="right">10.99</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">12.03</td>
    <td align="right">13.11</td>
    <td align="right">13.13</td>
    <td align="right">13.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.02</td>
    <td align="right">68.75</td>
    <td align="right">68.76</td>
    <td align="right">68.75</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.88</td>
    <td align="right">17.88</td>
    <td align="right">17.92</td>
    <td align="right">17.94</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.97</td>
    <td align="right">18.79</td>
    <td align="right">18.78</td>
    <td align="right">18.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">119.92</td>
    <td align="right">114.06</td>
    <td align="right">113.93</td>
    <td align="right">110.55</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.07</td>
    <td align="right">21.80</td>
    <td align="right">21.81</td>
    <td align="right">21.81</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.78</td>
    <td align="right">15.35</td>
    <td align="right">15.37</td>
    <td align="right">15.38</td>
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
    <td align="right">14.01</td>
    <td align="right">13.87</td>
    <td align="right">21.33</td>
    <td align="right">18.96</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.67</td>
    <td align="right">3.92</td>
    <td align="right">3.90</td>
    <td align="right">3.99</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.25</td>
    <td align="right">3.09</td>
    <td align="right">3.10</td>
    <td align="right">3.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">48.96</td>
    <td align="right">48.72</td>
    <td align="right">28.04</td>
    <td align="right">38.43</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.35</td>
    <td align="right">8.19</td>
    <td align="right">8.17</td>
    <td align="right">8.19</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.62</td>
    <td align="right">7.27</td>
    <td align="right">7.26</td>
    <td align="right">7.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.82</td>
    <td align="right">82.33</td>
    <td align="right">32.49</td>
    <td align="right">58.83</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.40</td>
    <td align="right">11.95</td>
    <td align="right">11.95</td>
    <td align="right">11.94</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.49</td>
    <td align="right">9.53</td>
    <td align="right">9.54</td>
    <td align="right">9.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">122.41</td>
    <td align="right">115.75</td>
    <td align="right">38.18</td>
    <td align="right">79.18</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.51</td>
    <td align="right">14.65</td>
    <td align="right">14.64</td>
    <td align="right">14.69</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.20</td>
    <td align="right">11.10</td>
    <td align="right">11.10</td>
    <td align="right">11.11</td>
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
    <td align="right">14.26</td>
    <td align="right">15.79</td>
    <td align="right">15.86</td>
    <td align="right">15.95</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.98</td>
    <td align="right">4.22</td>
    <td align="right">4.17</td>
    <td align="right">4.24</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.93</td>
    <td align="right">2.85</td>
    <td align="right">2.92</td>
    <td align="right">2.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">47.36</td>
    <td align="right">51.03</td>
    <td align="right">48.96</td>
    <td align="right">48.54</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.48</td>
    <td align="right">8.04</td>
    <td align="right">8.06</td>
    <td align="right">8.06</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.30</td>
    <td align="right">7.22</td>
    <td align="right">7.21</td>
    <td align="right">7.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">85.78</td>
    <td align="right">85.84</td>
    <td align="right">85.27</td>
    <td align="right">84.59</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.47</td>
    <td align="right">11.93</td>
    <td align="right">11.95</td>
    <td align="right">11.92</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.45</td>
    <td align="right">9.59</td>
    <td align="right">9.59</td>
    <td align="right">9.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">121.84</td>
    <td align="right">116.96</td>
    <td align="right">117.02</td>
    <td align="right">117.07</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.42</td>
    <td align="right">14.56</td>
    <td align="right">14.56</td>
    <td align="right">14.56</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.11</td>
    <td align="right">11.09</td>
    <td align="right">11.09</td>
    <td align="right">11.09</td>
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
    <td align="right">4.19</td>
    <td align="right">6.93</td>
    <td align="right">14.63</td>
    <td align="right">13.33</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.86</td>
    <td align="right">7.60</td>
    <td align="right">14.39</td>
    <td align="right">13.36</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.91</td>
    <td align="right">3.82</td>
    <td align="right">3.87</td>
    <td align="right">3.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.66</td>
    <td align="right">14.97</td>
    <td align="right">18.84</td>
    <td align="right">19.74</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.53</td>
    <td align="right">16.95</td>
    <td align="right">18.29</td>
    <td align="right">20.07</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.96</td>
    <td align="right">7.65</td>
    <td align="right">7.65</td>
    <td align="right">7.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.54</td>
    <td align="right">29.83</td>
    <td align="right">24.27</td>
    <td align="right">30.60</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.66</td>
    <td align="right">29.54</td>
    <td align="right">23.49</td>
    <td align="right">30.09</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.21</td>
    <td align="right">16.39</td>
    <td align="right">11.82</td>
    <td align="right">20.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">24.57</td>
    <td align="right">38.67</td>
    <td align="right">26.35</td>
    <td align="right">38.57</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.89</td>
    <td align="right">40.17</td>
    <td align="right">26.80</td>
    <td align="right">39.56</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.36</td>
    <td align="right">18.44</td>
    <td align="right">13.21</td>
    <td align="right">23.52</td>
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
    <td align="right">4.49</td>
    <td align="right">5.34</td>
    <td align="right">5.37</td>
    <td align="right">5.34</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">5.55</td>
    <td align="right">6.34</td>
    <td align="right">6.31</td>
    <td align="right">6.31</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.83</td>
    <td align="right">3.65</td>
    <td align="right">3.67</td>
    <td align="right">3.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">9.12</td>
    <td align="right">10.92</td>
    <td align="right">10.93</td>
    <td align="right">10.93</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.44</td>
    <td align="right">11.91</td>
    <td align="right">11.88</td>
    <td align="right">11.92</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">8.52</td>
    <td align="right">8.17</td>
    <td align="right">8.19</td>
    <td align="right">8.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.02</td>
    <td align="right">22.07</td>
    <td align="right">22.11</td>
    <td align="right">22.09</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.71</td>
    <td align="right">22.60</td>
    <td align="right">22.64</td>
    <td align="right">22.62</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.30</td>
    <td align="right">16.48</td>
    <td align="right">16.47</td>
    <td align="right">16.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.78</td>
    <td align="right">29.58</td>
    <td align="right">29.63</td>
    <td align="right">29.57</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.81</td>
    <td align="right">30.77</td>
    <td align="right">30.80</td>
    <td align="right">30.79</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.38</td>
    <td align="right">18.40</td>
    <td align="right">18.43</td>
    <td align="right">18.42</td>
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
    <td align="right">4.42</td>
    <td align="right">7.37</td>
    <td align="right">15.90</td>
    <td align="right">13.55</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.54</td>
    <td align="right">7.28</td>
    <td align="right">14.42</td>
    <td align="right">13.16</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.30</td>
    <td align="right">3.48</td>
    <td align="right">3.50</td>
    <td align="right">3.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">7.96</td>
    <td align="right">14.79</td>
    <td align="right">19.30</td>
    <td align="right">20.07</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">8.69</td>
    <td align="right">16.07</td>
    <td align="right">18.94</td>
    <td align="right">19.31</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.76</td>
    <td align="right">7.44</td>
    <td align="right">7.42</td>
    <td align="right">7.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">17.35</td>
    <td align="right">28.52</td>
    <td align="right">23.10</td>
    <td align="right">29.09</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.22</td>
    <td align="right">29.03</td>
    <td align="right">22.82</td>
    <td align="right">29.92</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.97</td>
    <td align="right">15.75</td>
    <td align="right">11.32</td>
    <td align="right">20.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.06</td>
    <td align="right">38.41</td>
    <td align="right">24.95</td>
    <td align="right">37.82</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.76</td>
    <td align="right">40.21</td>
    <td align="right">25.06</td>
    <td align="right">39.45</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.99</td>
    <td align="right">18.89</td>
    <td align="right">13.31</td>
    <td align="right">23.21</td>
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
    <td align="right">4.18</td>
    <td align="right">4.55</td>
    <td align="right">4.54</td>
    <td align="right">4.58</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.11</td>
    <td align="right">4.64</td>
    <td align="right">4.61</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.24</td>
    <td align="right">3.43</td>
    <td align="right">3.44</td>
    <td align="right">3.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.00</td>
    <td align="right">12.14</td>
    <td align="right">12.10</td>
    <td align="right">12.09</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">8.63</td>
    <td align="right">11.97</td>
    <td align="right">11.98</td>
    <td align="right">11.96</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.93</td>
    <td align="right">7.62</td>
    <td align="right">7.61</td>
    <td align="right">7.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">17.54</td>
    <td align="right">26.44</td>
    <td align="right">26.43</td>
    <td align="right">26.44</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">17.96</td>
    <td align="right">27.27</td>
    <td align="right">27.28</td>
    <td align="right">27.29</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.91</td>
    <td align="right">16.25</td>
    <td align="right">16.26</td>
    <td align="right">16.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.23</td>
    <td align="right">34.65</td>
    <td align="right">34.64</td>
    <td align="right">34.63</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.52</td>
    <td align="right">36.61</td>
    <td align="right">36.61</td>
    <td align="right">36.61</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.96</td>
    <td align="right">18.19</td>
    <td align="right">18.20</td>
    <td align="right">18.20</td>
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
    <td align="right">4.14</td>
    <td align="right">3.92</td>
    <td align="right">3.94</td>
    <td align="right">3.92</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.83</td>
    <td align="right">5.30</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.26</td>
    <td align="right">5.48</td>
    <td align="right">5.50</td>
    <td align="right">5.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.50</td>
    <td align="right">7.50</td>
    <td align="right">7.50</td>
    <td align="right">7.49</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.03</td>
    <td align="right">9.64</td>
    <td align="right">9.63</td>
    <td align="right">9.66</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.44</td>
    <td align="right">11.74</td>
    <td align="right">11.74</td>
    <td align="right">11.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.47</td>
    <td align="right">16.28</td>
    <td align="right">11.19</td>
    <td align="right">20.51</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">20.17</td>
    <td align="right">21.77</td>
    <td align="right">17.04</td>
    <td align="right">27.52</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.75</td>
    <td align="right">21.20</td>
    <td align="right">16.64</td>
    <td align="right">26.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.58</td>
    <td align="right">18.36</td>
    <td align="right">12.52</td>
    <td align="right">22.91</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.06</td>
    <td align="right">29.48</td>
    <td align="right">19.82</td>
    <td align="right">32.72</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.50</td>
    <td align="right">27.07</td>
    <td align="right">19.21</td>
    <td align="right">32.22</td>
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
    <td align="right">3.77</td>
    <td align="right">3.53</td>
    <td align="right">3.53</td>
    <td align="right">3.51</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.40</td>
    <td align="right">5.90</td>
    <td align="right">5.91</td>
    <td align="right">5.91</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.18</td>
    <td align="right">5.35</td>
    <td align="right">5.36</td>
    <td align="right">5.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.93</td>
    <td align="right">7.95</td>
    <td align="right">7.91</td>
    <td align="right">7.90</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.37</td>
    <td align="right">10.02</td>
    <td align="right">10.02</td>
    <td align="right">10.00</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.39</td>
    <td align="right">11.69</td>
    <td align="right">11.70</td>
    <td align="right">11.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.41</td>
    <td align="right">16.12</td>
    <td align="right">16.13</td>
    <td align="right">16.14</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.86</td>
    <td align="right">21.60</td>
    <td align="right">21.61</td>
    <td align="right">22.12</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.71</td>
    <td align="right">21.47</td>
    <td align="right">21.48</td>
    <td align="right">21.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.53</td>
    <td align="right">18.10</td>
    <td align="right">18.12</td>
    <td align="right">18.12</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.68</td>
    <td align="right">30.22</td>
    <td align="right">30.25</td>
    <td align="right">30.28</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.82</td>
    <td align="right">29.12</td>
    <td align="right">29.15</td>
    <td align="right">29.14</td>
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
    <td align="right">3.75</td>
    <td align="right">3.76</td>
    <td align="right">3.76</td>
    <td align="right">3.75</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.11</td>
    <td align="right">5.71</td>
    <td align="right">5.68</td>
    <td align="right">5.71</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.48</td>
    <td align="right">5.72</td>
    <td align="right">5.77</td>
    <td align="right">5.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.21</td>
    <td align="right">7.74</td>
    <td align="right">7.72</td>
    <td align="right">7.73</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.20</td>
    <td align="right">9.40</td>
    <td align="right">9.38</td>
    <td align="right">9.39</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">9.83</td>
    <td align="right">11.22</td>
    <td align="right">11.22</td>
    <td align="right">11.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.14</td>
    <td align="right">16.07</td>
    <td align="right">11.06</td>
    <td align="right">20.46</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.16</td>
    <td align="right">18.99</td>
    <td align="right">14.54</td>
    <td align="right">26.19</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.70</td>
    <td align="right">19.12</td>
    <td align="right">14.72</td>
    <td align="right">25.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.38</td>
    <td align="right">18.11</td>
    <td align="right">12.24</td>
    <td align="right">22.60</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">24.89</td>
    <td align="right">26.89</td>
    <td align="right">16.43</td>
    <td align="right">31.85</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">27.00</td>
    <td align="right">27.25</td>
    <td align="right">16.69</td>
    <td align="right">30.98</td>
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
    <td align="right">3.27</td>
    <td align="right">3.19</td>
    <td align="right">3.21</td>
    <td align="right">3.18</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.62</td>
    <td align="right">5.04</td>
    <td align="right">5.05</td>
    <td align="right">5.08</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.84</td>
    <td align="right">5.14</td>
    <td align="right">5.14</td>
    <td align="right">5.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.14</td>
    <td align="right">7.64</td>
    <td align="right">7.67</td>
    <td align="right">7.64</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.42</td>
    <td align="right">9.65</td>
    <td align="right">9.67</td>
    <td align="right">9.66</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.05</td>
    <td align="right">11.45</td>
    <td align="right">11.49</td>
    <td align="right">11.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.05</td>
    <td align="right">15.76</td>
    <td align="right">15.72</td>
    <td align="right">15.72</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.09</td>
    <td align="right">21.06</td>
    <td align="right">21.07</td>
    <td align="right">21.05</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.76</td>
    <td align="right">20.83</td>
    <td align="right">20.85</td>
    <td align="right">20.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.39</td>
    <td align="right">17.77</td>
    <td align="right">17.73</td>
    <td align="right">17.74</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">24.92</td>
    <td align="right">27.10</td>
    <td align="right">27.11</td>
    <td align="right">27.11</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">26.73</td>
    <td align="right">26.92</td>
    <td align="right">26.94</td>
    <td align="right">26.89</td>
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
    <td align="right">8.17</td>
    <td align="right">15.43</td>
    <td align="right">14.51</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.89</td>
    <td align="right">9.99</td>
    <td align="right">19.75</td>
    <td align="right">17.45</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.14</td>
    <td align="right">13.40</td>
    <td align="right">20.69</td>
    <td align="right">17.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">18.73</td>
    <td align="right">16.83</td>
    <td align="right">18.13</td>
    <td align="right">21.74</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.31</td>
    <td align="right">19.33</td>
    <td align="right">19.63</td>
    <td align="right">24.14</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.60</td>
    <td align="right">27.46</td>
    <td align="right">25.64</td>
    <td align="right">27.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">29.09</td>
    <td align="right">26.77</td>
    <td align="right">21.14</td>
    <td align="right">29.35</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.41</td>
    <td align="right">32.85</td>
    <td align="right">24.77</td>
    <td align="right">34.99</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.28</td>
    <td align="right">43.43</td>
    <td align="right">29.64</td>
    <td align="right">38.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.20</td>
    <td align="right">34.78</td>
    <td align="right">24.33</td>
    <td align="right">37.98</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.80</td>
    <td align="right">42.35</td>
    <td align="right">26.32</td>
    <td align="right">44.10</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">77.33</td>
    <td align="right">65.86</td>
    <td align="right">40.14</td>
    <td align="right">56.32</td>
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
    <td align="right">8.08</td>
    <td align="right">8.53</td>
    <td align="right">8.55</td>
    <td align="right">8.52</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">14.01</td>
    <td align="right">11.28</td>
    <td align="right">11.28</td>
    <td align="right">11.24</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.27</td>
    <td align="right">13.18</td>
    <td align="right">13.17</td>
    <td align="right">13.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.72</td>
    <td align="right">16.84</td>
    <td align="right">16.84</td>
    <td align="right">16.86</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.56</td>
    <td align="right">21.77</td>
    <td align="right">21.77</td>
    <td align="right">21.73</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">30.75</td>
    <td align="right">32.24</td>
    <td align="right">32.28</td>
    <td align="right">32.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.80</td>
    <td align="right">30.65</td>
    <td align="right">30.66</td>
    <td align="right">30.65</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.33</td>
    <td align="right">38.53</td>
    <td align="right">38.53</td>
    <td align="right">38.56</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.14</td>
    <td align="right">48.11</td>
    <td align="right">48.05</td>
    <td align="right">48.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.18</td>
    <td align="right">42.69</td>
    <td align="right">42.61</td>
    <td align="right">42.60</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.69</td>
    <td align="right">51.28</td>
    <td align="right">51.29</td>
    <td align="right">51.24</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">76.77</td>
    <td align="right">73.04</td>
    <td align="right">72.75</td>
    <td align="right">72.67</td>
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
    <td align="right">7.25</td>
    <td align="right">7.91</td>
    <td align="right">15.50</td>
    <td align="right">14.48</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.20</td>
    <td align="right">10.22</td>
    <td align="right">19.52</td>
    <td align="right">18.01</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.81</td>
    <td align="right">13.87</td>
    <td align="right">19.97</td>
    <td align="right">17.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.69</td>
    <td align="right">16.80</td>
    <td align="right">18.32</td>
    <td align="right">22.08</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.85</td>
    <td align="right">19.70</td>
    <td align="right">19.36</td>
    <td align="right">24.28</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">32.60</td>
    <td align="right">28.75</td>
    <td align="right">24.02</td>
    <td align="right">28.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.09</td>
    <td align="right">27.11</td>
    <td align="right">21.84</td>
    <td align="right">29.95</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.05</td>
    <td align="right">32.68</td>
    <td align="right">24.55</td>
    <td align="right">34.75</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">51.07</td>
    <td align="right">43.91</td>
    <td align="right">23.22</td>
    <td align="right">38.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.49</td>
    <td align="right">37.98</td>
    <td align="right">24.80</td>
    <td align="right">40.37</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.69</td>
    <td align="right">43.42</td>
    <td align="right">26.17</td>
    <td align="right">44.89</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.86</td>
    <td align="right">67.83</td>
    <td align="right">28.93</td>
    <td align="right">56.25</td>
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
    <td align="right">7.51</td>
    <td align="right">5.65</td>
    <td align="right">5.64</td>
    <td align="right">5.65</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.10</td>
    <td align="right">9.31</td>
    <td align="right">9.32</td>
    <td align="right">9.32</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.99</td>
    <td align="right">14.37</td>
    <td align="right">14.39</td>
    <td align="right">14.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.94</td>
    <td align="right">13.84</td>
    <td align="right">13.87</td>
    <td align="right">13.84</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.42</td>
    <td align="right">20.03</td>
    <td align="right">19.95</td>
    <td align="right">20.04</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.80</td>
    <td align="right">23.92</td>
    <td align="right">23.59</td>
    <td align="right">23.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.18</td>
    <td align="right">19.95</td>
    <td align="right">19.90</td>
    <td align="right">19.91</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.10</td>
    <td align="right">38.56</td>
    <td align="right">38.55</td>
    <td align="right">38.63</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">50.08</td>
    <td align="right">36.23</td>
    <td align="right">36.50</td>
    <td align="right">36.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.77</td>
    <td align="right">24.37</td>
    <td align="right">24.40</td>
    <td align="right">24.42</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.90</td>
    <td align="right">51.30</td>
    <td align="right">51.25</td>
    <td align="right">51.21</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.83</td>
    <td align="right">53.06</td>
    <td align="right">52.92</td>
    <td align="right">53.05</td>
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
    <td align="right">18.64</td>
    <td align="right">2.54</td>
    <td align="right">1.97</td>
    <td align="right">9.53</td>
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
    <td align="right">6.33</td>
    <td align="right">4.10</td>
    <td align="right">11.89</td>
    <td align="right">8.64</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.29</td>
    <td align="right">1.22</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.62</td>
    <td align="right">1.29</td>
    <td align="right">1.28</td>
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.51</td>
    <td align="right">6.04</td>
    <td align="right">12.52</td>
    <td align="right">10.36</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.70</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.60</td>
    <td align="right">7.27</td>
    <td align="right">11.87</td>
    <td align="right">10.93</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.75</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">15.05</td>
    <td align="right">9.29</td>
    <td align="right">12.12</td>
    <td align="right">12.28</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.80</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.80</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
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
    <td align="right">3.86</td>
    <td align="right">3.87</td>
    <td align="right">3.85</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.30</td>
    <td align="right">1.22</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.62</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.44</td>
    <td align="right">5.76</td>
    <td align="right">5.77</td>
    <td align="right">5.78</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.69</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.61</td>
    <td align="right">7.04</td>
    <td align="right">7.04</td>
    <td align="right">7.04</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.60</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.74</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.99</td>
    <td align="right">9.11</td>
    <td align="right">9.11</td>
    <td align="right">9.06</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="right">1.82</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.79</td>
    <td align="right">1.56</td>
    <td align="right">1.56</td>
    <td align="right">1.56</td>
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
    <td align="right">5.50</td>
    <td align="right">3.59</td>
    <td align="right">11.69</td>
    <td align="right">8.24</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.18</td>
    <td align="right">1.14</td>
    <td align="right">1.14</td>
    <td align="right">1.14</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.29</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
    <td align="right">1.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">8.43</td>
    <td align="right">5.37</td>
    <td align="right">12.39</td>
    <td align="right">9.91</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.32</td>
    <td align="right">1.33</td>
    <td align="right">1.33</td>
    <td align="right">1.33</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.45</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
    <td align="right">1.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">10.51</td>
    <td align="right">6.56</td>
    <td align="right">11.61</td>
    <td align="right">10.83</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.53</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.63</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">12.55</td>
    <td align="right">8.48</td>
    <td align="right">11.81</td>
    <td align="right">11.73</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.71</td>
    <td align="right">1.76</td>
    <td align="right">1.76</td>
    <td align="right">1.76</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.61</td>
    <td align="right">1.56</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
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
    <td align="right">3.48</td>
    <td align="right">3.48</td>
    <td align="right">3.48</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.20</td>
    <td align="right">1.14</td>
    <td align="right">1.15</td>
    <td align="right">1.16</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.32</td>
    <td align="right">1.21</td>
    <td align="right">1.21</td>
    <td align="right">1.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">8.37</td>
    <td align="right">5.33</td>
    <td align="right">5.32</td>
    <td align="right">5.32</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.34</td>
    <td align="right">1.35</td>
    <td align="right">1.33</td>
    <td align="right">1.33</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.48</td>
    <td align="right">1.40</td>
    <td align="right">1.39</td>
    <td align="right">1.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">10.56</td>
    <td align="right">6.61</td>
    <td align="right">6.60</td>
    <td align="right">6.62</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.55</td>
    <td align="right">1.56</td>
    <td align="right">1.56</td>
    <td align="right">1.56</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.65</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">12.61</td>
    <td align="right">8.53</td>
    <td align="right">8.50</td>
    <td align="right">8.49</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.70</td>
    <td align="right">1.75</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.61</td>
    <td align="right">1.55</td>
    <td align="right">1.55</td>
    <td align="right">1.56</td>
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
    <td align="right">2.54</td>
    <td align="right">9.37</td>
    <td align="right">7.27</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.27</td>
    <td align="right">2.53</td>
    <td align="right">8.75</td>
    <td align="right">7.13</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.00</td>
    <td align="right">1.71</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.19</td>
    <td align="right">3.89</td>
    <td align="right">10.76</td>
    <td align="right">8.85</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.81</td>
    <td align="right">3.54</td>
    <td align="right">9.71</td>
    <td align="right">8.10</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.52</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
    <td align="right">1.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.04</td>
    <td align="right">4.90</td>
    <td align="right">10.58</td>
    <td align="right">9.48</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.07</td>
    <td align="right">4.82</td>
    <td align="right">10.02</td>
    <td align="right">8.92</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.89</td>
    <td align="right">2.38</td>
    <td align="right">1.75</td>
    <td align="right">11.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.51</td>
    <td align="right">5.56</td>
    <td align="right">10.24</td>
    <td align="right">9.72</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.74</td>
    <td align="right">5.83</td>
    <td align="right">10.21</td>
    <td align="right">9.62</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.91</td>
    <td align="right">2.91</td>
    <td align="right">1.71</td>
    <td align="right">11.39</td>
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
    <td align="right">2.24</td>
    <td align="right">1.71</td>
    <td align="right">1.70</td>
    <td align="right">1.72</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.32</td>
    <td align="right">1.75</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.03</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.17</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.72</td>
    <td align="right">2.14</td>
    <td align="right">2.14</td>
    <td align="right">2.14</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.50</td>
    <td align="right">1.39</td>
    <td align="right">1.39</td>
    <td align="right">1.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.04</td>
    <td align="right">2.90</td>
    <td align="right">2.89</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">3.00</td>
    <td align="right">3.01</td>
    <td align="right">3.01</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.90</td>
    <td align="right">2.35</td>
    <td align="right">2.35</td>
    <td align="right">2.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.63</td>
    <td align="right">3.34</td>
    <td align="right">3.36</td>
    <td align="right">3.34</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.65</td>
    <td align="right">3.57</td>
    <td align="right">3.56</td>
    <td align="right">3.55</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.95</td>
    <td align="right">2.93</td>
    <td align="right">2.92</td>
    <td align="right">2.94</td>
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
    <td align="right">1.91</td>
    <td align="right">2.51</td>
    <td align="right">9.38</td>
    <td align="right">7.28</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.98</td>
    <td align="right">2.54</td>
    <td align="right">8.97</td>
    <td align="right">6.90</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.62</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="right">1.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.08</td>
    <td align="right">3.85</td>
    <td align="right">10.60</td>
    <td align="right">8.59</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.52</td>
    <td align="right">3.51</td>
    <td align="right">9.89</td>
    <td align="right">7.89</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.41</td>
    <td align="right">1.38</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.57</td>
    <td align="right">4.73</td>
    <td align="right">10.61</td>
    <td align="right">9.24</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.50</td>
    <td align="right">4.72</td>
    <td align="right">10.23</td>
    <td align="right">9.23</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.68</td>
    <td align="right">2.46</td>
    <td align="right">1.60</td>
    <td align="right">11.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.19</td>
    <td align="right">5.38</td>
    <td align="right">10.20</td>
    <td align="right">9.59</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.33</td>
    <td align="right">5.73</td>
    <td align="right">10.39</td>
    <td align="right">9.56</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.75</td>
    <td align="right">2.95</td>
    <td align="right">1.59</td>
    <td align="right">11.28</td>
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
    <td align="right">1.90</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.95</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.63</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.09</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.52</td>
    <td align="right">2.17</td>
    <td align="right">2.17</td>
    <td align="right">2.18</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.40</td>
    <td align="right">1.37</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.64</td>
    <td align="right">2.65</td>
    <td align="right">2.53</td>
    <td align="right">2.63</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.52</td>
    <td align="right">2.70</td>
    <td align="right">2.70</td>
    <td align="right">2.68</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.68</td>
    <td align="right">2.44</td>
    <td align="right">2.43</td>
    <td align="right">2.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.28</td>
    <td align="right">3.22</td>
    <td align="right">3.08</td>
    <td align="right">3.12</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.33</td>
    <td align="right">3.32</td>
    <td align="right">3.33</td>
    <td align="right">3.32</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.74</td>
    <td align="right">2.91</td>
    <td align="right">2.94</td>
    <td align="right">2.95</td>
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
    <td align="right">2.02</td>
    <td align="right">1.68</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.28</td>
    <td align="right">2.53</td>
    <td align="right">9.29</td>
    <td align="right">7.33</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.33</td>
    <td align="right">2.54</td>
    <td align="right">8.79</td>
    <td align="right">7.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.02</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">3.89</td>
    <td align="right">10.77</td>
    <td align="right">8.85</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.74</td>
    <td align="right">3.53</td>
    <td align="right">9.71</td>
    <td align="right">8.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.88</td>
    <td align="right">2.38</td>
    <td align="right">1.75</td>
    <td align="right">11.29</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.05</td>
    <td align="right">4.93</td>
    <td align="right">10.62</td>
    <td align="right">9.49</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.06</td>
    <td align="right">4.81</td>
    <td align="right">10.02</td>
    <td align="right">8.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.95</td>
    <td align="right">2.83</td>
    <td align="right">1.71</td>
    <td align="right">11.34</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.65</td>
    <td align="right">5.56</td>
    <td align="right">10.24</td>
    <td align="right">9.73</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.66</td>
    <td align="right">5.81</td>
    <td align="right">10.19</td>
    <td align="right">9.58</td>
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
    <td align="right">2.00</td>
    <td align="right">1.71</td>
    <td align="right">1.69</td>
    <td align="right">1.68</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.25</td>
    <td align="right">1.73</td>
    <td align="right">1.68</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.32</td>
    <td align="right">1.76</td>
    <td align="right">1.74</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.05</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="right">1.58</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.17</td>
    <td align="right">1.84</td>
    <td align="right">1.85</td>
    <td align="right">1.84</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.79</td>
    <td align="right">2.17</td>
    <td align="right">2.16</td>
    <td align="right">2.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.93</td>
    <td align="right">2.32</td>
    <td align="right">2.33</td>
    <td align="right">2.33</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.07</td>
    <td align="right">2.90</td>
    <td align="right">2.90</td>
    <td align="right">2.90</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.10</td>
    <td align="right">3.05</td>
    <td align="right">3.04</td>
    <td align="right">3.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.96</td>
    <td align="right">2.82</td>
    <td align="right">2.81</td>
    <td align="right">2.81</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.65</td>
    <td align="right">3.35</td>
    <td align="right">3.35</td>
    <td align="right">3.35</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.76</td>
    <td align="right">3.56</td>
    <td align="right">3.56</td>
    <td align="right">3.56</td>
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
    <td align="right">1.62</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.90</td>
    <td align="right">2.49</td>
    <td align="right">9.35</td>
    <td align="right">7.28</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.97</td>
    <td align="right">2.54</td>
    <td align="right">8.98</td>
    <td align="right">6.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">1.66</td>
    <td align="right">1.44</td>
    <td align="right">1.44</td>
    <td align="right">1.44</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.08</td>
    <td align="right">3.87</td>
    <td align="right">10.60</td>
    <td align="right">8.57</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.54</td>
    <td align="right">3.50</td>
    <td align="right">9.86</td>
    <td align="right">7.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.65</td>
    <td align="right">2.43</td>
    <td align="right">1.60</td>
    <td align="right">11.18</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.50</td>
    <td align="right">4.73</td>
    <td align="right">10.57</td>
    <td align="right">9.22</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.51</td>
    <td align="right">4.72</td>
    <td align="right">10.24</td>
    <td align="right">9.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.69</td>
    <td align="right">2.89</td>
    <td align="right">1.59</td>
    <td align="right">11.27</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.24</td>
    <td align="right">5.41</td>
    <td align="right">10.22</td>
    <td align="right">9.60</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.41</td>
    <td align="right">5.73</td>
    <td align="right">10.41</td>
    <td align="right">9.60</td>
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
    <td align="right">1.62</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.90</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.01</td>
    <td align="right">1.55</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">1.66</td>
    <td align="right">1.43</td>
    <td align="right">1.44</td>
    <td align="right">1.44</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.07</td>
    <td align="right">1.83</td>
    <td align="right">1.83</td>
    <td align="right">1.85</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.52</td>
    <td align="right">2.17</td>
    <td align="right">2.17</td>
    <td align="right">2.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.67</td>
    <td align="right">2.43</td>
    <td align="right">2.43</td>
    <td align="right">2.42</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.52</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="right">2.66</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.52</td>
    <td align="right">2.67</td>
    <td align="right">2.67</td>
    <td align="right">2.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.68</td>
    <td align="right">2.87</td>
    <td align="right">2.87</td>
    <td align="right">2.87</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.25</td>
    <td align="right">3.19</td>
    <td align="right">3.20</td>
    <td align="right">3.10</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.42</td>
    <td align="right">3.30</td>
    <td align="right">3.29</td>
    <td align="right">3.29</td>
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
    <td align="right">3.22</td>
    <td align="right">10.10</td>
    <td align="right">8.40</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">7.01</td>
    <td align="right">3.96</td>
    <td align="right">12.77</td>
    <td align="right">9.36</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.71</td>
    <td align="right">5.14</td>
    <td align="right">13.11</td>
    <td align="right">9.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.39</td>
    <td align="right">4.34</td>
    <td align="right">9.94</td>
    <td align="right">9.44</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.40</td>
    <td align="right">4.52</td>
    <td align="right">10.54</td>
    <td align="right">10.26</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.92</td>
    <td align="right">7.16</td>
    <td align="right">13.55</td>
    <td align="right">11.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.48</td>
    <td align="right">5.17</td>
    <td align="right">9.70</td>
    <td align="right">9.71</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.50</td>
    <td align="right">5.74</td>
    <td align="right">11.32</td>
    <td align="right">11.10</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.10</td>
    <td align="right">7.91</td>
    <td align="right">12.46</td>
    <td align="right">11.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.01</td>
    <td align="right">6.49</td>
    <td align="right">10.25</td>
    <td align="right">10.48</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.41</td>
    <td align="right">6.34</td>
    <td align="right">10.82</td>
    <td align="right">11.26</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.17</td>
    <td align="right">10.76</td>
    <td align="right">14.55</td>
    <td align="right">14.11</td>
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
    <td align="right">2.85</td>
    <td align="right">2.86</td>
    <td align="right">2.85</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">7.05</td>
    <td align="right">3.85</td>
    <td align="right">3.84</td>
    <td align="right">3.85</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.69</td>
    <td align="right">4.86</td>
    <td align="right">4.86</td>
    <td align="right">4.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.36</td>
    <td align="right">3.82</td>
    <td align="right">3.82</td>
    <td align="right">3.82</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.36</td>
    <td align="right">4.25</td>
    <td align="right">4.24</td>
    <td align="right">4.25</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.86</td>
    <td align="right">6.78</td>
    <td align="right">6.78</td>
    <td align="right">6.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.49</td>
    <td align="right">4.55</td>
    <td align="right">4.55</td>
    <td align="right">4.55</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.47</td>
    <td align="right">5.24</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.03</td>
    <td align="right">7.54</td>
    <td align="right">7.54</td>
    <td align="right">7.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.98</td>
    <td align="right">5.78</td>
    <td align="right">5.78</td>
    <td align="right">5.79</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.38</td>
    <td align="right">6.01</td>
    <td align="right">6.01</td>
    <td align="right">6.01</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.13</td>
    <td align="right">10.67</td>
    <td align="right">10.68</td>
    <td align="right">10.67</td>
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
    <td align="right">3.17</td>
    <td align="right">3.19</td>
    <td align="right">10.14</td>
    <td align="right">8.29</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.80</td>
    <td align="right">3.72</td>
    <td align="right">12.71</td>
    <td align="right">9.28</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">6.61</td>
    <td align="right">5.01</td>
    <td align="right">13.31</td>
    <td align="right">9.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.36</td>
    <td align="right">4.32</td>
    <td align="right">9.91</td>
    <td align="right">9.35</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.64</td>
    <td align="right">4.48</td>
    <td align="right">10.48</td>
    <td align="right">10.29</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">9.64</td>
    <td align="right">6.84</td>
    <td align="right">13.54</td>
    <td align="right">10.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.46</td>
    <td align="right">5.17</td>
    <td align="right">9.67</td>
    <td align="right">9.98</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.46</td>
    <td align="right">5.74</td>
    <td align="right">11.25</td>
    <td align="right">11.08</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">10.72</td>
    <td align="right">7.67</td>
    <td align="right">12.08</td>
    <td align="right">11.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.03</td>
    <td align="right">6.49</td>
    <td align="right">10.26</td>
    <td align="right">10.48</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.49</td>
    <td align="right">6.42</td>
    <td align="right">10.84</td>
    <td align="right">11.82</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">15.00</td>
    <td align="right">10.92</td>
    <td align="right">13.28</td>
    <td align="right">13.27</td>
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
    <td align="right">3.18</td>
    <td align="right">2.84</td>
    <td align="right">2.84</td>
    <td align="right">2.85</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.87</td>
    <td align="right">3.68</td>
    <td align="right">3.68</td>
    <td align="right">3.68</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">6.62</td>
    <td align="right">4.82</td>
    <td align="right">4.82</td>
    <td align="right">4.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.36</td>
    <td align="right">3.81</td>
    <td align="right">3.81</td>
    <td align="right">3.82</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.22</td>
    <td align="right">4.20</td>
    <td align="right">4.20</td>
    <td align="right">4.20</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">9.62</td>
    <td align="right">6.60</td>
    <td align="right">6.60</td>
    <td align="right">6.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.43</td>
    <td align="right">4.53</td>
    <td align="right">4.53</td>
    <td align="right">4.53</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.42</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="right">5.29</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">10.70</td>
    <td align="right">7.49</td>
    <td align="right">7.49</td>
    <td align="right">7.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.97</td>
    <td align="right">5.77</td>
    <td align="right">5.77</td>
    <td align="right">5.77</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.39</td>
    <td align="right">6.07</td>
    <td align="right">6.05</td>
    <td align="right">6.06</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">15.01</td>
    <td align="right">10.93</td>
    <td align="right">10.90</td>
    <td align="right">10.89</td>
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
    <td align="right">23.68</td>
    <td align="right">10.85</td>
    <td align="right">5.89</td>
    <td align="right">15.44</td>
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
    <td align="right">6.31</td>
    <td align="right">13.84</td>
    <td align="right">10.45</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.09</td>
    <td align="right">2.04</td>
    <td align="right">2.07</td>
    <td align="right">2.06</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.15</td>
    <td align="right">2.05</td>
    <td align="right">2.09</td>
    <td align="right">2.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.29</td>
    <td align="right">11.26</td>
    <td align="right">17.12</td>
    <td align="right">14.82</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.36</td>
    <td align="right">3.34</td>
    <td align="right">3.40</td>
    <td align="right">3.49</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.87</td>
    <td align="right">3.10</td>
    <td align="right">3.06</td>
    <td align="right">3.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">30.68</td>
    <td align="right">22.97</td>
    <td align="right">19.52</td>
    <td align="right">22.39</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">7.00</td>
    <td align="right">6.70</td>
    <td align="right">6.47</td>
    <td align="right">6.34</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.70</td>
    <td align="right">6.26</td>
    <td align="right">6.34</td>
    <td align="right">6.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">54.55</td>
    <td align="right">40.09</td>
    <td align="right">22.05</td>
    <td align="right">31.81</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.47</td>
    <td align="right">8.30</td>
    <td align="right">8.00</td>
    <td align="right">7.97</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.22</td>
    <td align="right">6.66</td>
    <td align="right">6.68</td>
    <td align="right">6.45</td>
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
    <td align="right">7.79</td>
    <td align="right">6.60</td>
    <td align="right">6.61</td>
    <td align="right">6.61</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.09</td>
    <td align="right">2.03</td>
    <td align="right">2.03</td>
    <td align="right">2.03</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.14</td>
    <td align="right">2.05</td>
    <td align="right">2.07</td>
    <td align="right">2.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">12.92</td>
    <td align="right">12.21</td>
    <td align="right">11.55</td>
    <td align="right">12.60</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.53</td>
    <td align="right">3.72</td>
    <td align="right">3.58</td>
    <td align="right">3.43</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.28</td>
    <td align="right">3.12</td>
    <td align="right">3.11</td>
    <td align="right">3.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">31.45</td>
    <td align="right">27.96</td>
    <td align="right">27.76</td>
    <td align="right">27.61</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">7.15</td>
    <td align="right">6.54</td>
    <td align="right">6.64</td>
    <td align="right">7.01</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.82</td>
    <td align="right">6.24</td>
    <td align="right">6.77</td>
    <td align="right">6.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">54.77</td>
    <td align="right">46.66</td>
    <td align="right">46.64</td>
    <td align="right">41.50</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.28</td>
    <td align="right">7.46</td>
    <td align="right">7.43</td>
    <td align="right">7.43</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">6.93</td>
    <td align="right">5.94</td>
    <td align="right">5.95</td>
    <td align="right">5.93</td>
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
    <td align="right">6.64</td>
    <td align="right">5.47</td>
    <td align="right">13.39</td>
    <td align="right">9.81</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.91</td>
    <td align="right">1.90</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.91</td>
    <td align="right">1.89</td>
    <td align="right">1.89</td>
    <td align="right">1.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">10.82</td>
    <td align="right">9.45</td>
    <td align="right">16.43</td>
    <td align="right">13.81</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">2.96</td>
    <td align="right">2.94</td>
    <td align="right">2.92</td>
    <td align="right">2.95</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">2.96</td>
    <td align="right">2.96</td>
    <td align="right">2.96</td>
    <td align="right">2.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">24.45</td>
    <td align="right">20.25</td>
    <td align="right">18.72</td>
    <td align="right">19.69</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">5.99</td>
    <td align="right">5.67</td>
    <td align="right">5.68</td>
    <td align="right">5.68</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">5.99</td>
    <td align="right">5.66</td>
    <td align="right">5.66</td>
    <td align="right">5.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">45.23</td>
    <td align="right">32.35</td>
    <td align="right">21.32</td>
    <td align="right">27.09</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.18</td>
    <td align="right">7.29</td>
    <td align="right">7.25</td>
    <td align="right">7.24</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">6.91</td>
    <td align="right">6.10</td>
    <td align="right">6.13</td>
    <td align="right">6.10</td>
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
    <td align="right">6.64</td>
    <td align="right">5.84</td>
    <td align="right">5.85</td>
    <td align="right">5.85</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.91</td>
    <td align="right">1.88</td>
    <td align="right">1.89</td>
    <td align="right">1.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">10.83</td>
    <td align="right">10.52</td>
    <td align="right">10.53</td>
    <td align="right">10.57</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">2.94</td>
    <td align="right">2.92</td>
    <td align="right">2.94</td>
    <td align="right">2.92</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">2.99</td>
    <td align="right">2.97</td>
    <td align="right">2.95</td>
    <td align="right">2.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">24.32</td>
    <td align="right">22.68</td>
    <td align="right">22.77</td>
    <td align="right">22.69</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">5.99</td>
    <td align="right">5.67</td>
    <td align="right">5.89</td>
    <td align="right">5.68</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">5.97</td>
    <td align="right">5.65</td>
    <td align="right">5.64</td>
    <td align="right">5.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">45.24</td>
    <td align="right">38.25</td>
    <td align="right">38.30</td>
    <td align="right">38.19</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.13</td>
    <td align="right">7.25</td>
    <td align="right">7.23</td>
    <td align="right">7.26</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">6.90</td>
    <td align="right">6.13</td>
    <td align="right">6.12</td>
    <td align="right">6.10</td>
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
    <td align="right">2.71</td>
    <td align="right">3.41</td>
    <td align="right">10.15</td>
    <td align="right">8.42</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.72</td>
    <td align="right">3.45</td>
    <td align="right">9.63</td>
    <td align="right">8.26</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.39</td>
    <td align="right">2.54</td>
    <td align="right">2.57</td>
    <td align="right">2.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.57</td>
    <td align="right">6.35</td>
    <td align="right">13.10</td>
    <td align="right">11.92</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.03</td>
    <td align="right">6.42</td>
    <td align="right">11.74</td>
    <td align="right">11.10</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.54</td>
    <td align="right">3.13</td>
    <td align="right">3.14</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.69</td>
    <td align="right">12.53</td>
    <td align="right">14.72</td>
    <td align="right">15.70</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.68</td>
    <td align="right">12.54</td>
    <td align="right">14.07</td>
    <td align="right">15.37</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.40</td>
    <td align="right">7.51</td>
    <td align="right">5.38</td>
    <td align="right">14.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.18</td>
    <td align="right">16.80</td>
    <td align="right">15.22</td>
    <td align="right">19.13</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.66</td>
    <td align="right">17.64</td>
    <td align="right">15.66</td>
    <td align="right">19.84</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.30</td>
    <td align="right">10.16</td>
    <td align="right">5.97</td>
    <td align="right">16.07</td>
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
    <td align="right">2.70</td>
    <td align="right">2.54</td>
    <td align="right">2.60</td>
    <td align="right">2.59</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.72</td>
    <td align="right">2.61</td>
    <td align="right">2.64</td>
    <td align="right">2.64</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.39</td>
    <td align="right">2.55</td>
    <td align="right">2.57</td>
    <td align="right">2.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.56</td>
    <td align="right">3.82</td>
    <td align="right">3.86</td>
    <td align="right">3.83</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.04</td>
    <td align="right">4.58</td>
    <td align="right">4.40</td>
    <td align="right">4.34</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.53</td>
    <td align="right">3.14</td>
    <td align="right">3.14</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.68</td>
    <td align="right">8.96</td>
    <td align="right">8.94</td>
    <td align="right">8.93</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.69</td>
    <td align="right">8.84</td>
    <td align="right">8.93</td>
    <td align="right">8.89</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.47</td>
    <td align="right">7.58</td>
    <td align="right">7.60</td>
    <td align="right">7.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">13.98</td>
    <td align="right">11.85</td>
    <td align="right">11.86</td>
    <td align="right">11.83</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.51</td>
    <td align="right">12.60</td>
    <td align="right">12.61</td>
    <td align="right">12.60</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.25</td>
    <td align="right">10.30</td>
    <td align="right">10.35</td>
    <td align="right">10.27</td>
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
    <td align="right">2.30</td>
    <td align="right">3.35</td>
    <td align="right">10.34</td>
    <td align="right">8.49</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.39</td>
    <td align="right">3.44</td>
    <td align="right">9.95</td>
    <td align="right">8.04</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.02</td>
    <td align="right">2.61</td>
    <td align="right">2.66</td>
    <td align="right">2.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.47</td>
    <td align="right">6.36</td>
    <td align="right">12.95</td>
    <td align="right">11.74</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.11</td>
    <td align="right">6.53</td>
    <td align="right">12.01</td>
    <td align="right">10.93</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.47</td>
    <td align="right">3.15</td>
    <td align="right">3.14</td>
    <td align="right">3.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.75</td>
    <td align="right">12.49</td>
    <td align="right">15.01</td>
    <td align="right">15.62</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.86</td>
    <td align="right">12.69</td>
    <td align="right">14.50</td>
    <td align="right">15.72</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.20</td>
    <td align="right">7.93</td>
    <td align="right">5.41</td>
    <td align="right">14.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.91</td>
    <td align="right">16.59</td>
    <td align="right">15.14</td>
    <td align="right">18.98</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.62</td>
    <td align="right">18.03</td>
    <td align="right">15.82</td>
    <td align="right">19.74</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.33</td>
    <td align="right">10.63</td>
    <td align="right">6.56</td>
    <td align="right">16.14</td>
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
    <td align="right">2.30</td>
    <td align="right">2.38</td>
    <td align="right">2.43</td>
    <td align="right">2.43</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.39</td>
    <td align="right">2.49</td>
    <td align="right">2.53</td>
    <td align="right">2.52</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.01</td>
    <td align="right">2.60</td>
    <td align="right">2.65</td>
    <td align="right">2.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.48</td>
    <td align="right">4.17</td>
    <td align="right">3.82</td>
    <td align="right">3.80</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.11</td>
    <td align="right">4.74</td>
    <td align="right">4.61</td>
    <td align="right">4.58</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.50</td>
    <td align="right">3.13</td>
    <td align="right">3.11</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.79</td>
    <td align="right">8.94</td>
    <td align="right">8.94</td>
    <td align="right">8.92</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.88</td>
    <td align="right">8.92</td>
    <td align="right">8.93</td>
    <td align="right">8.95</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.19</td>
    <td align="right">7.92</td>
    <td align="right">7.96</td>
    <td align="right">7.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.77</td>
    <td align="right">12.20</td>
    <td align="right">12.20</td>
    <td align="right">12.22</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.60</td>
    <td align="right">12.72</td>
    <td align="right">12.72</td>
    <td align="right">12.74</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.35</td>
    <td align="right">10.73</td>
    <td align="right">10.75</td>
    <td align="right">10.74</td>
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
    <td align="right">2.37</td>
    <td align="right">2.54</td>
    <td align="right">2.56</td>
    <td align="right">2.56</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.70</td>
    <td align="right">3.41</td>
    <td align="right">10.16</td>
    <td align="right">8.45</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.72</td>
    <td align="right">3.46</td>
    <td align="right">9.64</td>
    <td align="right">8.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.79</td>
    <td align="right">2.88</td>
    <td align="right">3.02</td>
    <td align="right">3.00</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.57</td>
    <td align="right">6.34</td>
    <td align="right">13.09</td>
    <td align="right">11.93</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.03</td>
    <td align="right">6.45</td>
    <td align="right">11.74</td>
    <td align="right">11.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.47</td>
    <td align="right">7.53</td>
    <td align="right">5.17</td>
    <td align="right">14.16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.67</td>
    <td align="right">12.53</td>
    <td align="right">14.72</td>
    <td align="right">15.75</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.63</td>
    <td align="right">12.51</td>
    <td align="right">14.07</td>
    <td align="right">15.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.37</td>
    <td align="right">10.20</td>
    <td align="right">5.98</td>
    <td align="right">15.83</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.18</td>
    <td align="right">16.80</td>
    <td align="right">15.22</td>
    <td align="right">19.13</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.65</td>
    <td align="right">17.66</td>
    <td align="right">15.68</td>
    <td align="right">19.90</td>
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
    <td align="right">2.37</td>
    <td align="right">2.53</td>
    <td align="right">2.56</td>
    <td align="right">2.55</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.70</td>
    <td align="right">2.54</td>
    <td align="right">2.60</td>
    <td align="right">2.59</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.72</td>
    <td align="right">2.60</td>
    <td align="right">2.64</td>
    <td align="right">2.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.80</td>
    <td align="right">2.88</td>
    <td align="right">3.02</td>
    <td align="right">3.00</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.56</td>
    <td align="right">3.81</td>
    <td align="right">3.86</td>
    <td align="right">3.83</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.03</td>
    <td align="right">4.58</td>
    <td align="right">4.39</td>
    <td align="right">4.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.44</td>
    <td align="right">7.58</td>
    <td align="right">7.59</td>
    <td align="right">7.23</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.70</td>
    <td align="right">8.95</td>
    <td align="right">8.96</td>
    <td align="right">8.93</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.65</td>
    <td align="right">8.87</td>
    <td align="right">8.84</td>
    <td align="right">8.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.32</td>
    <td align="right">10.33</td>
    <td align="right">10.34</td>
    <td align="right">10.34</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.00</td>
    <td align="right">11.76</td>
    <td align="right">11.76</td>
    <td align="right">11.80</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.51</td>
    <td align="right">12.60</td>
    <td align="right">12.61</td>
    <td align="right">12.59</td>
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
    <td align="right">2.03</td>
    <td align="right">2.59</td>
    <td align="right">2.65</td>
    <td align="right">2.65</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.30</td>
    <td align="right">3.36</td>
    <td align="right">10.36</td>
    <td align="right">8.50</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.40</td>
    <td align="right">3.45</td>
    <td align="right">9.96</td>
    <td align="right">8.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.62</td>
    <td align="right">3.21</td>
    <td align="right">3.19</td>
    <td align="right">3.18</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.47</td>
    <td align="right">6.35</td>
    <td align="right">12.94</td>
    <td align="right">11.74</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.13</td>
    <td align="right">6.55</td>
    <td align="right">12.01</td>
    <td align="right">10.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.30</td>
    <td align="right">7.96</td>
    <td align="right">5.52</td>
    <td align="right">14.15</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.76</td>
    <td align="right">12.52</td>
    <td align="right">15.04</td>
    <td align="right">15.63</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.87</td>
    <td align="right">12.70</td>
    <td align="right">14.51</td>
    <td align="right">15.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.62</td>
    <td align="right">10.85</td>
    <td align="right">6.73</td>
    <td align="right">15.94</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.92</td>
    <td align="right">16.56</td>
    <td align="right">15.14</td>
    <td align="right">18.96</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.65</td>
    <td align="right">18.04</td>
    <td align="right">15.83</td>
    <td align="right">19.83</td>
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
    <td align="right">2.03</td>
    <td align="right">2.60</td>
    <td align="right">2.65</td>
    <td align="right">2.64</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.30</td>
    <td align="right">2.38</td>
    <td align="right">2.44</td>
    <td align="right">2.43</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.40</td>
    <td align="right">2.50</td>
    <td align="right">2.53</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.63</td>
    <td align="right">3.20</td>
    <td align="right">3.17</td>
    <td align="right">3.18</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.47</td>
    <td align="right">3.81</td>
    <td align="right">3.80</td>
    <td align="right">3.81</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.11</td>
    <td align="right">4.75</td>
    <td align="right">4.63</td>
    <td align="right">4.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.36</td>
    <td align="right">8.02</td>
    <td align="right">8.01</td>
    <td align="right">7.92</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.78</td>
    <td align="right">8.94</td>
    <td align="right">8.93</td>
    <td align="right">8.92</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.85</td>
    <td align="right">8.92</td>
    <td align="right">8.97</td>
    <td align="right">8.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.63</td>
    <td align="right">10.93</td>
    <td align="right">10.92</td>
    <td align="right">10.94</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.77</td>
    <td align="right">12.13</td>
    <td align="right">12.19</td>
    <td align="right">12.20</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.64</td>
    <td align="right">12.73</td>
    <td align="right">12.72</td>
    <td align="right">12.73</td>
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
    <td align="right">4.61</td>
    <td align="right">4.27</td>
    <td align="right">11.24</td>
    <td align="right">9.90</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.82</td>
    <td align="right">4.92</td>
    <td align="right">13.66</td>
    <td align="right">10.66</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">9.01</td>
    <td align="right">6.84</td>
    <td align="right">14.70</td>
    <td align="right">11.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">7.88</td>
    <td align="right">7.10</td>
    <td align="right">11.90</td>
    <td align="right">12.59</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.09</td>
    <td align="right">7.45</td>
    <td align="right">12.39</td>
    <td align="right">13.45</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.00</td>
    <td align="right">11.28</td>
    <td align="right">17.31</td>
    <td align="right">14.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.24</td>
    <td align="right">12.22</td>
    <td align="right">13.38</td>
    <td align="right">16.14</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">20.81</td>
    <td align="right">14.27</td>
    <td align="right">15.82</td>
    <td align="right">18.59</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">23.55</td>
    <td align="right">18.99</td>
    <td align="right">18.29</td>
    <td align="right">19.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.48</td>
    <td align="right">16.26</td>
    <td align="right">15.00</td>
    <td align="right">19.87</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.28</td>
    <td align="right">18.99</td>
    <td align="right">16.42</td>
    <td align="right">22.76</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.75</td>
    <td align="right">34.35</td>
    <td align="right">26.62</td>
    <td align="right">31.63</td>
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
    <td align="right">4.60</td>
    <td align="right">4.22</td>
    <td align="right">4.42</td>
    <td align="right">4.38</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.85</td>
    <td align="right">5.19</td>
    <td align="right">5.36</td>
    <td align="right">5.34</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">9.02</td>
    <td align="right">6.95</td>
    <td align="right">6.95</td>
    <td align="right">6.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">7.90</td>
    <td align="right">7.47</td>
    <td align="right">7.46</td>
    <td align="right">7.48</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.07</td>
    <td align="right">7.83</td>
    <td align="right">7.79</td>
    <td align="right">7.77</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.00</td>
    <td align="right">11.71</td>
    <td align="right">11.65</td>
    <td align="right">11.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.17</td>
    <td align="right">13.11</td>
    <td align="right">13.15</td>
    <td align="right">13.06</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">20.70</td>
    <td align="right">15.10</td>
    <td align="right">15.02</td>
    <td align="right">15.09</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">23.58</td>
    <td align="right">20.34</td>
    <td align="right">20.30</td>
    <td align="right">20.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.50</td>
    <td align="right">17.75</td>
    <td align="right">17.77</td>
    <td align="right">17.81</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.25</td>
    <td align="right">20.65</td>
    <td align="right">20.64</td>
    <td align="right">20.65</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.69</td>
    <td align="right">35.55</td>
    <td align="right">35.58</td>
    <td align="right">35.57</td>
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
    <td align="right">4.67</td>
    <td align="right">4.25</td>
    <td align="right">11.33</td>
    <td align="right">9.74</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.70</td>
    <td align="right">4.80</td>
    <td align="right">13.64</td>
    <td align="right">10.63</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">8.01</td>
    <td align="right">6.59</td>
    <td align="right">14.81</td>
    <td align="right">11.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.24</td>
    <td align="right">7.14</td>
    <td align="right">11.93</td>
    <td align="right">12.55</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">13.80</td>
    <td align="right">7.56</td>
    <td align="right">12.24</td>
    <td align="right">13.46</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">12.66</td>
    <td align="right">11.22</td>
    <td align="right">16.47</td>
    <td align="right">14.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.78</td>
    <td align="right">12.21</td>
    <td align="right">13.35</td>
    <td align="right">16.23</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">21.14</td>
    <td align="right">14.51</td>
    <td align="right">15.61</td>
    <td align="right">18.79</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">22.18</td>
    <td align="right">19.14</td>
    <td align="right">15.51</td>
    <td align="right">19.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.65</td>
    <td align="right">16.27</td>
    <td align="right">14.97</td>
    <td align="right">19.77</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.90</td>
    <td align="right">19.50</td>
    <td align="right">16.28</td>
    <td align="right">23.12</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.39</td>
    <td align="right">35.26</td>
    <td align="right">17.53</td>
    <td align="right">30.76</td>
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
    <td align="right">4.66</td>
    <td align="right">4.22</td>
    <td align="right">4.42</td>
    <td align="right">4.39</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.70</td>
    <td align="right">5.09</td>
    <td align="right">5.29</td>
    <td align="right">5.26</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">8.01</td>
    <td align="right">6.60</td>
    <td align="right">6.61</td>
    <td align="right">6.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.18</td>
    <td align="right">7.46</td>
    <td align="right">7.49</td>
    <td align="right">7.44</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.22</td>
    <td align="right">7.95</td>
    <td align="right">7.90</td>
    <td align="right">7.95</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">12.68</td>
    <td align="right">11.73</td>
    <td align="right">11.66</td>
    <td align="right">11.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.69</td>
    <td align="right">13.10</td>
    <td align="right">13.12</td>
    <td align="right">13.09</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">21.19</td>
    <td align="right">15.54</td>
    <td align="right">15.47</td>
    <td align="right">15.45</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">22.06</td>
    <td align="right">20.65</td>
    <td align="right">20.64</td>
    <td align="right">20.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.77</td>
    <td align="right">17.78</td>
    <td align="right">17.76</td>
    <td align="right">17.77</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.94</td>
    <td align="right">21.14</td>
    <td align="right">21.11</td>
    <td align="right">21.19</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.39</td>
    <td align="right">36.79</td>
    <td align="right">36.84</td>
    <td align="right">36.83</td>
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
    <td align="right">26.00</td>
    <td align="right">5.20</td>
    <td align="right">3.59</td>
    <td align="right">9.94</td>
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
    <td align="right">10.31</td>
    <td align="right">10.01</td>
    <td align="right">14.57</td>
    <td align="right">13.89</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.82</td>
    <td align="right">3.74</td>
    <td align="right">4.10</td>
    <td align="right">8.44</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.34</td>
    <td align="right">4.45</td>
    <td align="right">4.55</td>
    <td align="right">9.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.01</td>
    <td align="right">14.33</td>
    <td align="right">14.85</td>
    <td align="right">15.37</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.39</td>
    <td align="right">4.05</td>
    <td align="right">4.20</td>
    <td align="right">8.97</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.03</td>
    <td align="right">4.76</td>
    <td align="right">4.76</td>
    <td align="right">9.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.25</td>
    <td align="right">17.34</td>
    <td align="right">14.59</td>
    <td align="right">17.77</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.03</td>
    <td align="right">4.43</td>
    <td align="right">4.42</td>
    <td align="right">9.56</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.67</td>
    <td align="right">5.30</td>
    <td align="right">5.23</td>
    <td align="right">10.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.94</td>
    <td align="right">22.24</td>
    <td align="right">15.09</td>
    <td align="right">20.59</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.72</td>
    <td align="right">4.82</td>
    <td align="right">4.82</td>
    <td align="right">9.93</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.27</td>
    <td align="right">5.92</td>
    <td align="right">5.67</td>
    <td align="right">10.36</td>
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
    <td align="right">10.24</td>
    <td align="right">12.52</td>
    <td align="right">12.47</td>
    <td align="right">12.48</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.79</td>
    <td align="right">3.72</td>
    <td align="right">4.06</td>
    <td align="right">8.55</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.35</td>
    <td align="right">4.46</td>
    <td align="right">4.54</td>
    <td align="right">8.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.17</td>
    <td align="right">18.56</td>
    <td align="right">18.40</td>
    <td align="right">18.27</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.42</td>
    <td align="right">4.04</td>
    <td align="right">4.21</td>
    <td align="right">9.01</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.02</td>
    <td align="right">4.88</td>
    <td align="right">4.92</td>
    <td align="right">9.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.15</td>
    <td align="right">22.63</td>
    <td align="right">22.53</td>
    <td align="right">22.39</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.04</td>
    <td align="right">4.43</td>
    <td align="right">4.46</td>
    <td align="right">9.53</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.66</td>
    <td align="right">5.27</td>
    <td align="right">5.21</td>
    <td align="right">9.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.92</td>
    <td align="right">27.66</td>
    <td align="right">27.56</td>
    <td align="right">27.54</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.72</td>
    <td align="right">4.86</td>
    <td align="right">4.86</td>
    <td align="right">9.83</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.30</td>
    <td align="right">5.97</td>
    <td align="right">5.70</td>
    <td align="right">10.39</td>
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
    <td align="right">10.16</td>
    <td align="right">10.06</td>
    <td align="right">14.41</td>
    <td align="right">12.77</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.85</td>
    <td align="right">3.71</td>
    <td align="right">4.03</td>
    <td align="right">8.53</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.38</td>
    <td align="right">4.41</td>
    <td align="right">4.62</td>
    <td align="right">8.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">14.99</td>
    <td align="right">14.39</td>
    <td align="right">15.21</td>
    <td align="right">15.74</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.48</td>
    <td align="right">4.06</td>
    <td align="right">4.17</td>
    <td align="right">9.17</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.01</td>
    <td align="right">4.82</td>
    <td align="right">4.89</td>
    <td align="right">9.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.02</td>
    <td align="right">17.20</td>
    <td align="right">14.54</td>
    <td align="right">17.60</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.11</td>
    <td align="right">4.42</td>
    <td align="right">4.41</td>
    <td align="right">9.52</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.62</td>
    <td align="right">5.23</td>
    <td align="right">5.27</td>
    <td align="right">9.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.54</td>
    <td align="right">22.04</td>
    <td align="right">14.92</td>
    <td align="right">20.50</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.76</td>
    <td align="right">4.84</td>
    <td align="right">4.82</td>
    <td align="right">10.01</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.24</td>
    <td align="right">5.82</td>
    <td align="right">5.68</td>
    <td align="right">10.39</td>
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
    <td align="right">10.13</td>
    <td align="right">12.67</td>
    <td align="right">12.69</td>
    <td align="right">12.68</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.86</td>
    <td align="right">3.70</td>
    <td align="right">4.02</td>
    <td align="right">8.48</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.37</td>
    <td align="right">4.40</td>
    <td align="right">4.64</td>
    <td align="right">8.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">14.99</td>
    <td align="right">18.63</td>
    <td align="right">18.27</td>
    <td align="right">18.29</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.49</td>
    <td align="right">3.99</td>
    <td align="right">4.11</td>
    <td align="right">9.06</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.02</td>
    <td align="right">4.82</td>
    <td align="right">4.91</td>
    <td align="right">9.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.02</td>
    <td align="right">22.67</td>
    <td align="right">22.65</td>
    <td align="right">22.69</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.11</td>
    <td align="right">4.42</td>
    <td align="right">4.43</td>
    <td align="right">9.38</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.63</td>
    <td align="right">5.28</td>
    <td align="right">5.31</td>
    <td align="right">9.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.69</td>
    <td align="right">28.57</td>
    <td align="right">28.18</td>
    <td align="right">28.25</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.78</td>
    <td align="right">4.86</td>
    <td align="right">4.86</td>
    <td align="right">9.85</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.27</td>
    <td align="right">5.86</td>
    <td align="right">5.71</td>
    <td align="right">10.21</td>
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
    <td align="right">5.36</td>
    <td align="right">7.00</td>
    <td align="right">11.42</td>
    <td align="right">10.92</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.46</td>
    <td align="right">7.53</td>
    <td align="right">12.21</td>
    <td align="right">11.55</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.84</td>
    <td align="right">2.74</td>
    <td align="right">2.98</td>
    <td align="right">8.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.23</td>
    <td align="right">9.50</td>
    <td align="right">11.80</td>
    <td align="right">12.10</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.76</td>
    <td align="right">11.27</td>
    <td align="right">13.09</td>
    <td align="right">13.83</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.81</td>
    <td align="right">3.59</td>
    <td align="right">2.97</td>
    <td align="right">9.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.52</td>
    <td align="right">12.93</td>
    <td align="right">14.22</td>
    <td align="right">15.70</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.36</td>
    <td align="right">13.88</td>
    <td align="right">15.78</td>
    <td align="right">16.32</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.27</td>
    <td align="right">4.89</td>
    <td align="right">3.63</td>
    <td align="right">11.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.56</td>
    <td align="right">14.33</td>
    <td align="right">13.38</td>
    <td align="right">16.76</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.77</td>
    <td align="right">19.46</td>
    <td align="right">15.56</td>
    <td align="right">20.54</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.32</td>
    <td align="right">4.93</td>
    <td align="right">3.61</td>
    <td align="right">11.52</td>
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
    <td align="right">5.41</td>
    <td align="right">4.78</td>
    <td align="right">4.89</td>
    <td align="right">9.60</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.46</td>
    <td align="right">5.26</td>
    <td align="right">5.45</td>
    <td align="right">10.99</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.84</td>
    <td align="right">2.74</td>
    <td align="right">2.97</td>
    <td align="right">8.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.22</td>
    <td align="right">7.09</td>
    <td align="right">6.93</td>
    <td align="right">11.47</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.72</td>
    <td align="right">7.83</td>
    <td align="right">7.66</td>
    <td align="right">13.22</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.82</td>
    <td align="right">3.02</td>
    <td align="right">2.94</td>
    <td align="right">9.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.49</td>
    <td align="right">9.23</td>
    <td align="right">9.14</td>
    <td align="right">14.03</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.36</td>
    <td align="right">10.61</td>
    <td align="right">10.24</td>
    <td align="right">15.61</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.29</td>
    <td align="right">4.13</td>
    <td align="right">4.05</td>
    <td align="right">10.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.55</td>
    <td align="right">10.24</td>
    <td align="right">10.07</td>
    <td align="right">15.17</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.85</td>
    <td align="right">12.16</td>
    <td align="right">12.08</td>
    <td align="right">17.10</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.32</td>
    <td align="right">4.11</td>
    <td align="right">3.90</td>
    <td align="right">10.90</td>
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
    <td align="right">5.37</td>
    <td align="right">7.04</td>
    <td align="right">11.60</td>
    <td align="right">11.00</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.53</td>
    <td align="right">7.51</td>
    <td align="right">12.00</td>
    <td align="right">11.73</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.84</td>
    <td align="right">2.67</td>
    <td align="right">2.96</td>
    <td align="right">8.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.12</td>
    <td align="right">9.71</td>
    <td align="right">12.01</td>
    <td align="right">12.63</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.61</td>
    <td align="right">11.15</td>
    <td align="right">13.14</td>
    <td align="right">13.78</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.74</td>
    <td align="right">3.51</td>
    <td align="right">2.76</td>
    <td align="right">9.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.46</td>
    <td align="right">12.99</td>
    <td align="right">14.31</td>
    <td align="right">16.00</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.39</td>
    <td align="right">13.72</td>
    <td align="right">15.41</td>
    <td align="right">16.52</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.32</td>
    <td align="right">4.95</td>
    <td align="right">3.66</td>
    <td align="right">11.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.64</td>
    <td align="right">14.84</td>
    <td align="right">13.81</td>
    <td align="right">17.39</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.85</td>
    <td align="right">19.28</td>
    <td align="right">15.73</td>
    <td align="right">20.19</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.36</td>
    <td align="right">4.98</td>
    <td align="right">3.68</td>
    <td align="right">11.58</td>
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
    <td align="right">5.39</td>
    <td align="right">4.68</td>
    <td align="right">4.84</td>
    <td align="right">9.45</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.53</td>
    <td align="right">5.26</td>
    <td align="right">5.52</td>
    <td align="right">10.92</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.82</td>
    <td align="right">2.70</td>
    <td align="right">2.98</td>
    <td align="right">8.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.12</td>
    <td align="right">6.89</td>
    <td align="right">6.69</td>
    <td align="right">11.18</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.50</td>
    <td align="right">7.59</td>
    <td align="right">7.33</td>
    <td align="right">12.91</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">3.03</td>
    <td align="right">2.95</td>
    <td align="right">9.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.41</td>
    <td align="right">9.04</td>
    <td align="right">8.88</td>
    <td align="right">13.91</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.35</td>
    <td align="right">10.62</td>
    <td align="right">10.14</td>
    <td align="right">15.54</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.31</td>
    <td align="right">4.02</td>
    <td align="right">3.94</td>
    <td align="right">10.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.57</td>
    <td align="right">10.18</td>
    <td align="right">10.06</td>
    <td align="right">15.08</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.88</td>
    <td align="right">12.18</td>
    <td align="right">12.07</td>
    <td align="right">16.81</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.33</td>
    <td align="right">4.02</td>
    <td align="right">3.93</td>
    <td align="right">10.80</td>
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
    <td align="right">2.79</td>
    <td align="right">2.59</td>
    <td align="right">2.82</td>
    <td align="right">8.70</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.71</td>
    <td align="right">3.99</td>
    <td align="right">4.08</td>
    <td align="right">10.67</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.77</td>
    <td align="right">3.70</td>
    <td align="right">3.93</td>
    <td align="right">10.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.25</td>
    <td align="right">3.95</td>
    <td align="right">3.10</td>
    <td align="right">9.83</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.16</td>
    <td align="right">4.45</td>
    <td align="right">3.70</td>
    <td align="right">10.84</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.70</td>
    <td align="right">5.38</td>
    <td align="right">4.44</td>
    <td align="right">11.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.36</td>
    <td align="right">4.74</td>
    <td align="right">3.46</td>
    <td align="right">10.99</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.93</td>
    <td align="right">6.74</td>
    <td align="right">5.40</td>
    <td align="right">13.38</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.66</td>
    <td align="right">6.69</td>
    <td align="right">5.37</td>
    <td align="right">13.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.41</td>
    <td align="right">4.75</td>
    <td align="right">3.46</td>
    <td align="right">10.97</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.82</td>
    <td align="right">7.64</td>
    <td align="right">5.39</td>
    <td align="right">13.84</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.03</td>
    <td align="right">7.57</td>
    <td align="right">5.42</td>
    <td align="right">13.70</td>
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
    <td align="right">2.81</td>
    <td align="right">2.59</td>
    <td align="right">2.82</td>
    <td align="right">8.69</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.71</td>
    <td align="right">4.00</td>
    <td align="right">4.08</td>
    <td align="right">10.57</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.76</td>
    <td align="right">3.70</td>
    <td align="right">3.93</td>
    <td align="right">10.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.22</td>
    <td align="right">3.07</td>
    <td align="right">3.02</td>
    <td align="right">9.18</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.14</td>
    <td align="right">5.28</td>
    <td align="right">5.23</td>
    <td align="right">11.45</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.65</td>
    <td align="right">5.95</td>
    <td align="right">5.92</td>
    <td align="right">12.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.35</td>
    <td align="right">3.90</td>
    <td align="right">3.80</td>
    <td align="right">10.56</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.91</td>
    <td align="right">7.50</td>
    <td align="right">7.38</td>
    <td align="right">13.88</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.66</td>
    <td align="right">7.36</td>
    <td align="right">7.09</td>
    <td align="right">13.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.41</td>
    <td align="right">3.92</td>
    <td align="right">3.83</td>
    <td align="right">10.54</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.81</td>
    <td align="right">8.39</td>
    <td align="right">8.35</td>
    <td align="right">14.95</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.00</td>
    <td align="right">8.29</td>
    <td align="right">8.09</td>
    <td align="right">14.79</td>
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
    <td align="right">2.70</td>
    <td align="right">2.57</td>
    <td align="right">2.78</td>
    <td align="right">8.85</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.64</td>
    <td align="right">3.81</td>
    <td align="right">4.02</td>
    <td align="right">10.75</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.75</td>
    <td align="right">3.69</td>
    <td align="right">3.88</td>
    <td align="right">10.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.15</td>
    <td align="right">4.00</td>
    <td align="right">3.25</td>
    <td align="right">9.89</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.18</td>
    <td align="right">4.39</td>
    <td align="right">3.67</td>
    <td align="right">10.62</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.65</td>
    <td align="right">5.25</td>
    <td align="right">4.45</td>
    <td align="right">11.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.33</td>
    <td align="right">4.80</td>
    <td align="right">3.54</td>
    <td align="right">11.00</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.87</td>
    <td align="right">6.79</td>
    <td align="right">5.41</td>
    <td align="right">13.48</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.58</td>
    <td align="right">6.54</td>
    <td align="right">5.27</td>
    <td align="right">12.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.39</td>
    <td align="right">4.87</td>
    <td align="right">3.57</td>
    <td align="right">11.19</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.46</td>
    <td align="right">7.67</td>
    <td align="right">5.38</td>
    <td align="right">14.02</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.93</td>
    <td align="right">7.43</td>
    <td align="right">5.34</td>
    <td align="right">13.39</td>
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
    <td align="right">2.71</td>
    <td align="right">2.56</td>
    <td align="right">2.78</td>
    <td align="right">8.90</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.64</td>
    <td align="right">3.82</td>
    <td align="right">4.01</td>
    <td align="right">10.65</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.75</td>
    <td align="right">3.70</td>
    <td align="right">3.88</td>
    <td align="right">10.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.16</td>
    <td align="right">3.03</td>
    <td align="right">2.94</td>
    <td align="right">9.13</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.20</td>
    <td align="right">5.30</td>
    <td align="right">5.10</td>
    <td align="right">11.36</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.68</td>
    <td align="right">6.00</td>
    <td align="right">5.87</td>
    <td align="right">12.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.36</td>
    <td align="right">3.81</td>
    <td align="right">3.76</td>
    <td align="right">10.54</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.87</td>
    <td align="right">7.51</td>
    <td align="right">7.24</td>
    <td align="right">13.78</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.58</td>
    <td align="right">7.38</td>
    <td align="right">7.13</td>
    <td align="right">13.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.40</td>
    <td align="right">3.87</td>
    <td align="right">3.81</td>
    <td align="right">10.51</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.46</td>
    <td align="right">8.43</td>
    <td align="right">8.38</td>
    <td align="right">15.02</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.95</td>
    <td align="right">8.25</td>
    <td align="right">8.13</td>
    <td align="right">14.64</td>
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
    <td align="right">7.07</td>
    <td align="right">6.75</td>
    <td align="right">11.01</td>
    <td align="right">10.76</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.46</td>
    <td align="right">9.45</td>
    <td align="right">14.06</td>
    <td align="right">12.88</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.01</td>
    <td align="right">12.27</td>
    <td align="right">16.40</td>
    <td align="right">14.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.36</td>
    <td align="right">10.29</td>
    <td align="right">12.04</td>
    <td align="right">12.97</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.75</td>
    <td align="right">11.26</td>
    <td align="right">13.13</td>
    <td align="right">14.42</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.69</td>
    <td align="right">15.99</td>
    <td align="right">16.21</td>
    <td align="right">17.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.37</td>
    <td align="right">11.54</td>
    <td align="right">11.94</td>
    <td align="right">14.31</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.24</td>
    <td align="right">13.33</td>
    <td align="right">14.22</td>
    <td align="right">16.15</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.53</td>
    <td align="right">18.06</td>
    <td align="right">17.67</td>
    <td align="right">19.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.64</td>
    <td align="right">14.13</td>
    <td align="right">12.57</td>
    <td align="right">16.72</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.37</td>
    <td align="right">15.22</td>
    <td align="right">12.45</td>
    <td align="right">16.89</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.40</td>
    <td align="right">23.82</td>
    <td align="right">19.55</td>
    <td align="right">22.44</td>
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
    <td align="right">7.08</td>
    <td align="right">6.11</td>
    <td align="right">6.18</td>
    <td align="right">10.78</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.49</td>
    <td align="right">7.90</td>
    <td align="right">8.13</td>
    <td align="right">13.09</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.12</td>
    <td align="right">9.00</td>
    <td align="right">9.25</td>
    <td align="right">14.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.38</td>
    <td align="right">8.01</td>
    <td align="right">7.91</td>
    <td align="right">12.95</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.76</td>
    <td align="right">9.54</td>
    <td align="right">9.29</td>
    <td align="right">14.69</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.71</td>
    <td align="right">13.01</td>
    <td align="right">12.91</td>
    <td align="right">17.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.36</td>
    <td align="right">10.46</td>
    <td align="right">10.45</td>
    <td align="right">15.02</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.23</td>
    <td align="right">13.30</td>
    <td align="right">13.14</td>
    <td align="right">17.14</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.39</td>
    <td align="right">15.12</td>
    <td align="right">15.09</td>
    <td align="right">20.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.69</td>
    <td align="right">12.97</td>
    <td align="right">12.97</td>
    <td align="right">16.92</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.43</td>
    <td align="right">14.69</td>
    <td align="right">14.59</td>
    <td align="right">18.20</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.36</td>
    <td align="right">23.06</td>
    <td align="right">22.94</td>
    <td align="right">26.29</td>
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
    <td align="right">7.32</td>
    <td align="right">7.11</td>
    <td align="right">11.76</td>
    <td align="right">11.07</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.49</td>
    <td align="right">9.32</td>
    <td align="right">14.27</td>
    <td align="right">12.83</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.11</td>
    <td align="right">12.21</td>
    <td align="right">16.99</td>
    <td align="right">15.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.66</td>
    <td align="right">10.16</td>
    <td align="right">12.15</td>
    <td align="right">13.50</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.79</td>
    <td align="right">11.27</td>
    <td align="right">13.11</td>
    <td align="right">14.52</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.85</td>
    <td align="right">16.40</td>
    <td align="right">16.70</td>
    <td align="right">17.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.78</td>
    <td align="right">11.62</td>
    <td align="right">12.41</td>
    <td align="right">14.58</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.21</td>
    <td align="right">13.31</td>
    <td align="right">14.06</td>
    <td align="right">15.81</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.23</td>
    <td align="right">17.81</td>
    <td align="right">14.65</td>
    <td align="right">18.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">15.03</td>
    <td align="right">14.50</td>
    <td align="right">12.95</td>
    <td align="right">17.34</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.43</td>
    <td align="right">15.07</td>
    <td align="right">12.37</td>
    <td align="right">16.99</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.48</td>
    <td align="right">23.87</td>
    <td align="right">15.43</td>
    <td align="right">22.37</td>
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
    <td align="right">7.32</td>
    <td align="right">6.28</td>
    <td align="right">6.34</td>
    <td align="right">11.24</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.49</td>
    <td align="right">7.86</td>
    <td align="right">8.07</td>
    <td align="right">13.09</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.15</td>
    <td align="right">9.28</td>
    <td align="right">9.49</td>
    <td align="right">14.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.65</td>
    <td align="right">8.40</td>
    <td align="right">8.33</td>
    <td align="right">13.09</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.75</td>
    <td align="right">9.28</td>
    <td align="right">9.04</td>
    <td align="right">14.42</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.80</td>
    <td align="right">13.50</td>
    <td align="right">13.62</td>
    <td align="right">18.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.83</td>
    <td align="right">11.20</td>
    <td align="right">11.08</td>
    <td align="right">15.84</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.21</td>
    <td align="right">13.30</td>
    <td align="right">13.09</td>
    <td align="right">17.10</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.23</td>
    <td align="right">15.17</td>
    <td align="right">15.13</td>
    <td align="right">19.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">15.11</td>
    <td align="right">13.43</td>
    <td align="right">13.32</td>
    <td align="right">17.23</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.40</td>
    <td align="right">14.61</td>
    <td align="right">14.46</td>
    <td align="right">18.15</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.48</td>
    <td align="right">22.37</td>
    <td align="right">22.07</td>
    <td align="right">26.55</td>
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
    <td align="right">23.47</td>
    <td align="right">12.12</td>
    <td align="right">27.92</td>
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
    <td align="right">11.94</td>
    <td align="right">10.62</td>
    <td align="right">16.25</td>
    <td align="right">13.88</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.35</td>
    <td align="right">3.96</td>
    <td align="right">4.50</td>
    <td align="right">9.47</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.65</td>
    <td align="right">4.86</td>
    <td align="right">5.03</td>
    <td align="right">9.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">24.56</td>
    <td align="right">16.19</td>
    <td align="right">16.99</td>
    <td align="right">17.66</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.12</td>
    <td align="right">5.52</td>
    <td align="right">5.64</td>
    <td align="right">11.04</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.88</td>
    <td align="right">6.65</td>
    <td align="right">6.55</td>
    <td align="right">11.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">72.35</td>
    <td align="right">72.88</td>
    <td align="right">25.49</td>
    <td align="right">50.45</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.56</td>
    <td align="right">14.97</td>
    <td align="right">14.74</td>
    <td align="right">19.12</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.68</td>
    <td align="right">17.65</td>
    <td align="right">16.16</td>
    <td align="right">20.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">105.10</td>
    <td align="right">113.79</td>
    <td align="right">33.11</td>
    <td align="right">75.21</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.80</td>
    <td align="right">18.78</td>
    <td align="right">18.86</td>
    <td align="right">22.98</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.99</td>
    <td align="right">23.18</td>
    <td align="right">22.87</td>
    <td align="right">26.57</td>
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
    <td align="right">11.44</td>
    <td align="right">13.02</td>
    <td align="right">13.00</td>
    <td align="right">13.01</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.22</td>
    <td align="right">3.97</td>
    <td align="right">4.47</td>
    <td align="right">9.58</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.89</td>
    <td align="right">4.87</td>
    <td align="right">5.00</td>
    <td align="right">9.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">26.81</td>
    <td align="right">20.69</td>
    <td align="right">20.63</td>
    <td align="right">20.56</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.10</td>
    <td align="right">5.70</td>
    <td align="right">6.02</td>
    <td align="right">11.21</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.81</td>
    <td align="right">6.77</td>
    <td align="right">6.76</td>
    <td align="right">11.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">72.29</td>
    <td align="right">87.58</td>
    <td align="right">87.88</td>
    <td align="right">87.84</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.50</td>
    <td align="right">15.04</td>
    <td align="right">14.78</td>
    <td align="right">19.12</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.59</td>
    <td align="right">17.65</td>
    <td align="right">16.17</td>
    <td align="right">20.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">104.26</td>
    <td align="right">131.26</td>
    <td align="right">131.29</td>
    <td align="right">131.33</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.71</td>
    <td align="right">18.82</td>
    <td align="right">18.90</td>
    <td align="right">22.92</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.80</td>
    <td align="right">23.20</td>
    <td align="right">22.85</td>
    <td align="right">26.52</td>
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
    <td align="right">12.06</td>
    <td align="right">27.98</td>
    <td align="right">20.43</td>
    <td align="right">24.31</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.28</td>
    <td align="right">7.91</td>
    <td align="right">7.96</td>
    <td align="right">12.57</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.06</td>
    <td align="right">4.79</td>
    <td align="right">5.16</td>
    <td align="right">9.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">30.58</td>
    <td align="right">16.01</td>
    <td align="right">17.09</td>
    <td align="right">17.78</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.11</td>
    <td align="right">5.80</td>
    <td align="right">5.91</td>
    <td align="right">11.43</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.71</td>
    <td align="right">6.40</td>
    <td align="right">6.64</td>
    <td align="right">11.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">72.04</td>
    <td align="right">75.47</td>
    <td align="right">26.29</td>
    <td align="right">52.04</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.69</td>
    <td align="right">15.52</td>
    <td align="right">15.33</td>
    <td align="right">19.61</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.58</td>
    <td align="right">17.38</td>
    <td align="right">15.99</td>
    <td align="right">20.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">105.63</td>
    <td align="right">115.34</td>
    <td align="right">33.33</td>
    <td align="right">76.05</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.74</td>
    <td align="right">21.58</td>
    <td align="right">18.85</td>
    <td align="right">23.74</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.62</td>
    <td align="right">23.23</td>
    <td align="right">22.94</td>
    <td align="right">26.52</td>
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
    <td align="right">11.31</td>
    <td align="right">34.86</td>
    <td align="right">34.77</td>
    <td align="right">34.88</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.43</td>
    <td align="right">3.96</td>
    <td align="right">4.45</td>
    <td align="right">9.47</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.74</td>
    <td align="right">4.79</td>
    <td align="right">5.19</td>
    <td align="right">9.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">27.77</td>
    <td align="right">20.83</td>
    <td align="right">20.74</td>
    <td align="right">20.62</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.19</td>
    <td align="right">5.79</td>
    <td align="right">5.93</td>
    <td align="right">11.27</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.73</td>
    <td align="right">6.62</td>
    <td align="right">6.86</td>
    <td align="right">11.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">70.91</td>
    <td align="right">98.88</td>
    <td align="right">98.83</td>
    <td align="right">99.00</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.68</td>
    <td align="right">15.52</td>
    <td align="right">15.37</td>
    <td align="right">19.54</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.44</td>
    <td align="right">17.92</td>
    <td align="right">16.47</td>
    <td align="right">20.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">105.07</td>
    <td align="right">147.80</td>
    <td align="right">147.88</td>
    <td align="right">147.80</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.70</td>
    <td align="right">21.51</td>
    <td align="right">18.81</td>
    <td align="right">23.86</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.79</td>
    <td align="right">23.24</td>
    <td align="right">22.90</td>
    <td align="right">26.42</td>
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
    <td align="right">6.25</td>
    <td align="right">7.47</td>
    <td align="right">12.07</td>
    <td align="right">11.72</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.75</td>
    <td align="right">8.17</td>
    <td align="right">13.17</td>
    <td align="right">12.46</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.08</td>
    <td align="right">2.89</td>
    <td align="right">3.34</td>
    <td align="right">9.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">11.28</td>
    <td align="right">11.99</td>
    <td align="right">13.80</td>
    <td align="right">14.68</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">14.86</td>
    <td align="right">31.27</td>
    <td align="right">22.09</td>
    <td align="right">31.36</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.93</td>
    <td align="right">5.26</td>
    <td align="right">4.91</td>
    <td align="right">11.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.80</td>
    <td align="right">30.41</td>
    <td align="right">22.43</td>
    <td align="right">30.05</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">30.38</td>
    <td align="right">32.08</td>
    <td align="right">26.54</td>
    <td align="right">33.47</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.09</td>
    <td align="right">17.52</td>
    <td align="right">13.26</td>
    <td align="right">19.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.86</td>
    <td align="right">41.52</td>
    <td align="right">25.55</td>
    <td align="right">40.99</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.16</td>
    <td align="right">57.65</td>
    <td align="right">30.71</td>
    <td align="right">53.80</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.48</td>
    <td align="right">20.52</td>
    <td align="right">15.05</td>
    <td align="right">22.02</td>
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
    <td align="right">6.34</td>
    <td align="right">5.24</td>
    <td align="right">5.32</td>
    <td align="right">10.47</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.82</td>
    <td align="right">5.61</td>
    <td align="right">5.83</td>
    <td align="right">11.76</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.08</td>
    <td align="right">2.89</td>
    <td align="right">3.34</td>
    <td align="right">9.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.99</td>
    <td align="right">8.59</td>
    <td align="right">8.53</td>
    <td align="right">13.54</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.31</td>
    <td align="right">24.65</td>
    <td align="right">24.44</td>
    <td align="right">29.27</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.69</td>
    <td align="right">5.00</td>
    <td align="right">5.02</td>
    <td align="right">10.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">27.16</td>
    <td align="right">26.39</td>
    <td align="right">26.43</td>
    <td align="right">30.60</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">30.49</td>
    <td align="right">33.22</td>
    <td align="right">33.04</td>
    <td align="right">37.74</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.10</td>
    <td align="right">15.19</td>
    <td align="right">14.99</td>
    <td align="right">19.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.66</td>
    <td align="right">35.60</td>
    <td align="right">35.44</td>
    <td align="right">40.06</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.53</td>
    <td align="right">39.17</td>
    <td align="right">39.18</td>
    <td align="right">43.46</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.43</td>
    <td align="right">17.64</td>
    <td align="right">17.31</td>
    <td align="right">22.41</td>
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
    <td align="right">5.97</td>
    <td align="right">7.65</td>
    <td align="right">12.24</td>
    <td align="right">11.85</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.83</td>
    <td align="right">9.62</td>
    <td align="right">13.63</td>
    <td align="right">13.88</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.13</td>
    <td align="right">7.16</td>
    <td align="right">7.06</td>
    <td align="right">12.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">9.99</td>
    <td align="right">11.86</td>
    <td align="right">13.80</td>
    <td align="right">15.00</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">14.70</td>
    <td align="right">14.09</td>
    <td align="right">14.31</td>
    <td align="right">16.91</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.67</td>
    <td align="right">5.22</td>
    <td align="right">4.73</td>
    <td align="right">10.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">27.31</td>
    <td align="right">33.19</td>
    <td align="right">24.67</td>
    <td align="right">34.55</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">30.60</td>
    <td align="right">34.13</td>
    <td align="right">27.68</td>
    <td align="right">35.90</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.21</td>
    <td align="right">17.56</td>
    <td align="right">13.26</td>
    <td align="right">19.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.96</td>
    <td align="right">48.67</td>
    <td align="right">26.62</td>
    <td align="right">47.65</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.65</td>
    <td align="right">57.66</td>
    <td align="right">30.80</td>
    <td align="right">53.67</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">18.08</td>
    <td align="right">20.71</td>
    <td align="right">15.19</td>
    <td align="right">22.17</td>
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
    <td align="right">6.01</td>
    <td align="right">5.13</td>
    <td align="right">5.26</td>
    <td align="right">10.33</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.68</td>
    <td align="right">5.61</td>
    <td align="right">5.87</td>
    <td align="right">11.78</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.50</td>
    <td align="right">2.83</td>
    <td align="right">3.33</td>
    <td align="right">9.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.73</td>
    <td align="right">19.50</td>
    <td align="right">19.40</td>
    <td align="right">23.43</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.14</td>
    <td align="right">22.56</td>
    <td align="right">22.22</td>
    <td align="right">26.96</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.87</td>
    <td align="right">4.83</td>
    <td align="right">4.85</td>
    <td align="right">10.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">27.09</td>
    <td align="right">27.59</td>
    <td align="right">27.42</td>
    <td align="right">32.29</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">31.03</td>
    <td align="right">28.65</td>
    <td align="right">28.63</td>
    <td align="right">33.18</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.23</td>
    <td align="right">16.89</td>
    <td align="right">16.70</td>
    <td align="right">21.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.83</td>
    <td align="right">35.80</td>
    <td align="right">35.54</td>
    <td align="right">40.10</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.83</td>
    <td align="right">40.61</td>
    <td align="right">40.50</td>
    <td align="right">44.78</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">18.08</td>
    <td align="right">17.90</td>
    <td align="right">17.69</td>
    <td align="right">22.82</td>
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
    <td align="right">3.34</td>
    <td align="right">2.73</td>
    <td align="right">3.15</td>
    <td align="right">9.65</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.30</td>
    <td align="right">4.21</td>
    <td align="right">4.41</td>
    <td align="right">11.70</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.10</td>
    <td align="right">3.90</td>
    <td align="right">4.27</td>
    <td align="right">11.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.31</td>
    <td align="right">5.81</td>
    <td align="right">5.03</td>
    <td align="right">11.31</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">5.99</td>
    <td align="right">6.05</td>
    <td align="right">5.53</td>
    <td align="right">12.30</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">8.01</td>
    <td align="right">8.73</td>
    <td align="right">6.33</td>
    <td align="right">12.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.11</td>
    <td align="right">15.86</td>
    <td align="right">12.18</td>
    <td align="right">18.56</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.23</td>
    <td align="right">21.45</td>
    <td align="right">17.66</td>
    <td align="right">23.68</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.97</td>
    <td align="right">21.87</td>
    <td align="right">18.08</td>
    <td align="right">23.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.84</td>
    <td align="right">18.40</td>
    <td align="right">13.90</td>
    <td align="right">21.20</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.93</td>
    <td align="right">28.90</td>
    <td align="right">20.45</td>
    <td align="right">29.39</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.00</td>
    <td align="right">27.85</td>
    <td align="right">19.49</td>
    <td align="right">27.87</td>
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
    <td align="right">3.06</td>
    <td align="right">2.74</td>
    <td align="right">3.15</td>
    <td align="right">9.64</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.01</td>
    <td align="right">4.21</td>
    <td align="right">4.42</td>
    <td align="right">11.62</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.13</td>
    <td align="right">3.93</td>
    <td align="right">4.30</td>
    <td align="right">11.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.13</td>
    <td align="right">4.95</td>
    <td align="right">4.81</td>
    <td align="right">10.56</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">5.99</td>
    <td align="right">16.14</td>
    <td align="right">16.04</td>
    <td align="right">21.68</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.54</td>
    <td align="right">8.11</td>
    <td align="right">8.05</td>
    <td align="right">13.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.37</td>
    <td align="right">15.09</td>
    <td align="right">14.95</td>
    <td align="right">19.17</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.15</td>
    <td align="right">25.26</td>
    <td align="right">25.17</td>
    <td align="right">30.17</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.95</td>
    <td align="right">22.44</td>
    <td align="right">22.24</td>
    <td align="right">27.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.87</td>
    <td align="right">17.53</td>
    <td align="right">17.30</td>
    <td align="right">22.05</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">29.17</td>
    <td align="right">28.35</td>
    <td align="right">28.22</td>
    <td align="right">33.39</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.01</td>
    <td align="right">29.43</td>
    <td align="right">29.34</td>
    <td align="right">34.17</td>
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
    <td align="right">2.96</td>
    <td align="right">2.72</td>
    <td align="right">3.09</td>
    <td align="right">9.80</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">3.96</td>
    <td align="right">4.04</td>
    <td align="right">4.38</td>
    <td align="right">11.63</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.15</td>
    <td align="right">3.91</td>
    <td align="right">4.24</td>
    <td align="right">11.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">4.76</td>
    <td align="right">6.06</td>
    <td align="right">5.23</td>
    <td align="right">11.49</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">6.07</td>
    <td align="right">5.83</td>
    <td align="right">5.31</td>
    <td align="right">12.07</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.21</td>
    <td align="right">7.02</td>
    <td align="right">6.10</td>
    <td align="right">12.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.23</td>
    <td align="right">17.56</td>
    <td align="right">13.25</td>
    <td align="right">19.10</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.43</td>
    <td align="right">24.52</td>
    <td align="right">20.12</td>
    <td align="right">25.91</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.93</td>
    <td align="right">19.36</td>
    <td align="right">16.32</td>
    <td align="right">22.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.95</td>
    <td align="right">20.68</td>
    <td align="right">15.21</td>
    <td align="right">21.92</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">29.76</td>
    <td align="right">28.64</td>
    <td align="right">19.85</td>
    <td align="right">29.37</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.28</td>
    <td align="right">27.88</td>
    <td align="right">19.56</td>
    <td align="right">28.05</td>
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
    <td align="right">2.96</td>
    <td align="right">2.72</td>
    <td align="right">3.10</td>
    <td align="right">9.88</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">3.97</td>
    <td align="right">4.05</td>
    <td align="right">4.35</td>
    <td align="right">11.52</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.12</td>
    <td align="right">3.89</td>
    <td align="right">4.22</td>
    <td align="right">11.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">4.82</td>
    <td align="right">5.18</td>
    <td align="right">5.02</td>
    <td align="right">10.49</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">5.87</td>
    <td align="right">16.59</td>
    <td align="right">16.49</td>
    <td align="right">22.06</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.75</td>
    <td align="right">8.55</td>
    <td align="right">7.98</td>
    <td align="right">13.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.16</td>
    <td align="right">15.03</td>
    <td align="right">13.60</td>
    <td align="right">18.80</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.25</td>
    <td align="right">24.30</td>
    <td align="right">24.00</td>
    <td align="right">29.21</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">21.02</td>
    <td align="right">22.49</td>
    <td align="right">22.31</td>
    <td align="right">27.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">18.00</td>
    <td align="right">17.86</td>
    <td align="right">16.02</td>
    <td align="right">22.37</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">29.57</td>
    <td align="right">28.68</td>
    <td align="right">28.60</td>
    <td align="right">33.71</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.15</td>
    <td align="right">29.35</td>
    <td align="right">29.08</td>
    <td align="right">33.91</td>
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
    <td align="right">7.89</td>
    <td align="right">7.23</td>
    <td align="right">11.80</td>
    <td align="right">11.64</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">11.23</td>
    <td align="right">10.33</td>
    <td align="right">14.89</td>
    <td align="right">14.00</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.44</td>
    <td align="right">13.79</td>
    <td align="right">17.43</td>
    <td align="right">16.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">12.42</td>
    <td align="right">12.11</td>
    <td align="right">13.57</td>
    <td align="right">15.11</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">15.65</td>
    <td align="right">14.47</td>
    <td align="right">14.56</td>
    <td align="right">17.40</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">16.70</td>
    <td align="right">17.71</td>
    <td align="right">17.36</td>
    <td align="right">19.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.69</td>
    <td align="right">28.55</td>
    <td align="right">21.22</td>
    <td align="right">29.95</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.50</td>
    <td align="right">37.48</td>
    <td align="right">27.06</td>
    <td align="right">38.89</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">42.18</td>
    <td align="right">42.11</td>
    <td align="right">29.29</td>
    <td align="right">38.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">36.29</td>
    <td align="right">36.58</td>
    <td align="right">23.96</td>
    <td align="right">38.49</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">43.29</td>
    <td align="right">42.43</td>
    <td align="right">23.63</td>
    <td align="right">42.86</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">69.67</td>
    <td align="right">66.82</td>
    <td align="right">40.95</td>
    <td align="right">58.33</td>
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
    <td align="right">7.83</td>
    <td align="right">6.56</td>
    <td align="right">6.53</td>
    <td align="right">11.51</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">11.92</td>
    <td align="right">14.62</td>
    <td align="right">14.72</td>
    <td align="right">19.33</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.96</td>
    <td align="right">9.95</td>
    <td align="right">10.18</td>
    <td align="right">15.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.30</td>
    <td align="right">9.65</td>
    <td align="right">9.71</td>
    <td align="right">15.23</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.42</td>
    <td align="right">15.64</td>
    <td align="right">15.66</td>
    <td align="right">21.39</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">17.15</td>
    <td align="right">14.22</td>
    <td align="right">14.36</td>
    <td align="right">18.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">26.50</td>
    <td align="right">23.94</td>
    <td align="right">23.88</td>
    <td align="right">28.44</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.92</td>
    <td align="right">31.78</td>
    <td align="right">31.61</td>
    <td align="right">35.40</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.99</td>
    <td align="right">37.60</td>
    <td align="right">37.65</td>
    <td align="right">41.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">36.21</td>
    <td align="right">33.90</td>
    <td align="right">33.90</td>
    <td align="right">37.62</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">43.30</td>
    <td align="right">41.03</td>
    <td align="right">40.99</td>
    <td align="right">44.35</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">69.87</td>
    <td align="right">65.08</td>
    <td align="right">64.94</td>
    <td align="right">68.02</td>
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
    <td align="right">7.88</td>
    <td align="right">10.17</td>
    <td align="right">14.11</td>
    <td align="right">14.22</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">11.48</td>
    <td align="right">14.98</td>
    <td align="right">17.36</td>
    <td align="right">17.99</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.99</td>
    <td align="right">13.84</td>
    <td align="right">18.01</td>
    <td align="right">16.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">12.40</td>
    <td align="right">12.25</td>
    <td align="right">13.85</td>
    <td align="right">15.77</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">15.84</td>
    <td align="right">14.50</td>
    <td align="right">14.53</td>
    <td align="right">17.72</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">17.50</td>
    <td align="right">18.19</td>
    <td align="right">17.83</td>
    <td align="right">20.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">26.85</td>
    <td align="right">25.71</td>
    <td align="right">20.51</td>
    <td align="right">27.60</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.25</td>
    <td align="right">35.45</td>
    <td align="right">25.64</td>
    <td align="right">36.63</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.76</td>
    <td align="right">40.94</td>
    <td align="right">20.96</td>
    <td align="right">36.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">36.64</td>
    <td align="right">46.38</td>
    <td align="right">24.80</td>
    <td align="right">48.40</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">44.37</td>
    <td align="right">43.00</td>
    <td align="right">23.65</td>
    <td align="right">43.42</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">73.02</td>
    <td align="right">67.82</td>
    <td align="right">22.76</td>
    <td align="right">54.74</td>
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
    <td align="right">8.31</td>
    <td align="right">6.82</td>
    <td align="right">6.79</td>
    <td align="right">11.95</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.87</td>
    <td align="right">8.39</td>
    <td align="right">8.65</td>
    <td align="right">13.89</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.24</td>
    <td align="right">10.34</td>
    <td align="right">10.61</td>
    <td align="right">15.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.57</td>
    <td align="right">21.93</td>
    <td align="right">21.98</td>
    <td align="right">26.50</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.20</td>
    <td align="right">14.57</td>
    <td align="right">14.49</td>
    <td align="right">20.41</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">15.93</td>
    <td align="right">39.09</td>
    <td align="right">39.11</td>
    <td align="right">43.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">26.47</td>
    <td align="right">25.01</td>
    <td align="right">24.87</td>
    <td align="right">29.53</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.07</td>
    <td align="right">35.44</td>
    <td align="right">35.60</td>
    <td align="right">39.08</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.05</td>
    <td align="right">41.53</td>
    <td align="right">41.05</td>
    <td align="right">45.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">36.75</td>
    <td align="right">34.45</td>
    <td align="right">34.40</td>
    <td align="right">38.02</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">43.46</td>
    <td align="right">41.16</td>
    <td align="right">41.19</td>
    <td align="right">45.46</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">72.82</td>
    <td align="right">68.01</td>
    <td align="right">67.66</td>
    <td align="right">71.31</td>
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
    <td align="right">74.04</td>
    <td align="right">34.56</td>
    <td align="right">14.31</td>
    <td align="right">28.65</td>
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
    <td align="right">31.01</td>
    <td align="right">44.47</td>
    <td align="right">36.18</td>
    <td align="right">39.82</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.30</td>
    <td align="right">16.26</td>
    <td align="right">16.29</td>
    <td align="right">16.10</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.59</td>
    <td align="right">17.50</td>
    <td align="right">18.07</td>
    <td align="right">18.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.68</td>
    <td align="right">68.44</td>
    <td align="right">36.62</td>
    <td align="right">51.91</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.37</td>
    <td align="right">18.29</td>
    <td align="right">18.22</td>
    <td align="right">18.37</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.07</td>
    <td align="right">19.02</td>
    <td align="right">19.58</td>
    <td align="right">19.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.46</td>
    <td align="right">82.40</td>
    <td align="right">35.65</td>
    <td align="right">60.35</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.39</td>
    <td align="right">20.48</td>
    <td align="right">20.48</td>
    <td align="right">20.48</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">16.97</td>
    <td align="right">21.61</td>
    <td align="right">21.14</td>
    <td align="right">21.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.62</td>
    <td align="right">95.73</td>
    <td align="right">35.46</td>
    <td align="right">63.42</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.67</td>
    <td align="right">22.19</td>
    <td align="right">22.20</td>
    <td align="right">22.20</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.63</td>
    <td align="right">22.29</td>
    <td align="right">22.26</td>
    <td align="right">23.09</td>
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
    <td align="right">30.81</td>
    <td align="right">41.38</td>
    <td align="right">41.36</td>
    <td align="right">41.43</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.31</td>
    <td align="right">16.12</td>
    <td align="right">16.32</td>
    <td align="right">16.25</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.61</td>
    <td align="right">17.69</td>
    <td align="right">17.56</td>
    <td align="right">17.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.80</td>
    <td align="right">60.92</td>
    <td align="right">60.95</td>
    <td align="right">61.07</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.32</td>
    <td align="right">18.31</td>
    <td align="right">18.43</td>
    <td align="right">18.31</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.09</td>
    <td align="right">19.65</td>
    <td align="right">19.09</td>
    <td align="right">19.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.17</td>
    <td align="right">70.49</td>
    <td align="right">71.48</td>
    <td align="right">70.37</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.40</td>
    <td align="right">20.48</td>
    <td align="right">20.57</td>
    <td align="right">20.52</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.09</td>
    <td align="right">21.13</td>
    <td align="right">20.99</td>
    <td align="right">21.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">73.33</td>
    <td align="right">113.06</td>
    <td align="right">112.92</td>
    <td align="right">112.51</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.68</td>
    <td align="right">22.22</td>
    <td align="right">22.21</td>
    <td align="right">22.22</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.26</td>
    <td align="right">21.99</td>
    <td align="right">23.09</td>
    <td align="right">22.09</td>
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
    <td align="right">30.95</td>
    <td align="right">46.47</td>
    <td align="right">35.17</td>
    <td align="right">41.17</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.34</td>
    <td align="right">18.97</td>
    <td align="right">19.02</td>
    <td align="right">18.98</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.60</td>
    <td align="right">21.83</td>
    <td align="right">21.83</td>
    <td align="right">21.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.17</td>
    <td align="right">68.98</td>
    <td align="right">37.73</td>
    <td align="right">53.41</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.44</td>
    <td align="right">22.83</td>
    <td align="right">22.79</td>
    <td align="right">22.89</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.10</td>
    <td align="right">20.90</td>
    <td align="right">20.88</td>
    <td align="right">21.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.37</td>
    <td align="right">84.42</td>
    <td align="right">37.08</td>
    <td align="right">61.34</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.51</td>
    <td align="right">21.27</td>
    <td align="right">21.27</td>
    <td align="right">21.31</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.14</td>
    <td align="right">23.11</td>
    <td align="right">23.14</td>
    <td align="right">23.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.27</td>
    <td align="right">109.61</td>
    <td align="right">36.92</td>
    <td align="right">71.80</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.79</td>
    <td align="right">23.58</td>
    <td align="right">23.53</td>
    <td align="right">23.54</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.51</td>
    <td align="right">24.67</td>
    <td align="right">24.58</td>
    <td align="right">24.57</td>
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
    <td align="right">47.53</td>
    <td align="right">47.67</td>
    <td align="right">47.75</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.32</td>
    <td align="right">18.90</td>
    <td align="right">18.97</td>
    <td align="right">18.91</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.62</td>
    <td align="right">21.83</td>
    <td align="right">21.83</td>
    <td align="right">21.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.11</td>
    <td align="right">71.28</td>
    <td align="right">71.42</td>
    <td align="right">71.31</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.50</td>
    <td align="right">22.84</td>
    <td align="right">22.86</td>
    <td align="right">22.86</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.10</td>
    <td align="right">20.90</td>
    <td align="right">20.88</td>
    <td align="right">20.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.59</td>
    <td align="right">87.78</td>
    <td align="right">87.72</td>
    <td align="right">87.92</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.56</td>
    <td align="right">21.31</td>
    <td align="right">21.30</td>
    <td align="right">21.30</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.12</td>
    <td align="right">23.09</td>
    <td align="right">23.13</td>
    <td align="right">23.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.15</td>
    <td align="right">114.12</td>
    <td align="right">116.79</td>
    <td align="right">117.70</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.80</td>
    <td align="right">23.55</td>
    <td align="right">23.54</td>
    <td align="right">23.26</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.43</td>
    <td align="right">24.68</td>
    <td align="right">24.65</td>
    <td align="right">24.55</td>
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
    <td align="right">19.87</td>
    <td align="right">23.98</td>
    <td align="right">26.88</td>
    <td align="right">27.74</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.29</td>
    <td align="right">27.91</td>
    <td align="right">29.30</td>
    <td align="right">30.93</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.87</td>
    <td align="right">14.97</td>
    <td align="right">23.97</td>
    <td align="right">21.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">27.14</td>
    <td align="right">30.76</td>
    <td align="right">28.62</td>
    <td align="right">32.06</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.06</td>
    <td align="right">34.60</td>
    <td align="right">34.21</td>
    <td align="right">35.62</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.01</td>
    <td align="right">17.59</td>
    <td align="right">25.41</td>
    <td align="right">22.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.29</td>
    <td align="right">44.35</td>
    <td align="right">31.07</td>
    <td align="right">40.07</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.89</td>
    <td align="right">49.32</td>
    <td align="right">39.99</td>
    <td align="right">44.71</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.27</td>
    <td align="right">20.15</td>
    <td align="right">26.51</td>
    <td align="right">25.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.38</td>
    <td align="right">47.45</td>
    <td align="right">29.65</td>
    <td align="right">43.07</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.56</td>
    <td align="right">57.05</td>
    <td align="right">41.95</td>
    <td align="right">49.57</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.03</td>
    <td align="right">27.93</td>
    <td align="right">25.90</td>
    <td align="right">30.41</td>
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
    <td align="right">19.92</td>
    <td align="right">23.78</td>
    <td align="right">23.78</td>
    <td align="right">23.83</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.24</td>
    <td align="right">26.52</td>
    <td align="right">26.55</td>
    <td align="right">26.55</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.77</td>
    <td align="right">15.97</td>
    <td align="right">15.56</td>
    <td align="right">15.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.69</td>
    <td align="right">30.12</td>
    <td align="right">30.08</td>
    <td align="right">30.01</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.08</td>
    <td align="right">34.60</td>
    <td align="right">34.59</td>
    <td align="right">34.61</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.90</td>
    <td align="right">18.39</td>
    <td align="right">17.87</td>
    <td align="right">18.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.82</td>
    <td align="right">36.93</td>
    <td align="right">37.12</td>
    <td align="right">37.02</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.89</td>
    <td align="right">49.09</td>
    <td align="right">49.21</td>
    <td align="right">49.07</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.02</td>
    <td align="right">20.93</td>
    <td align="right">20.93</td>
    <td align="right">20.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">38.20</td>
    <td align="right">41.60</td>
    <td align="right">41.70</td>
    <td align="right">41.68</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.55</td>
    <td align="right">58.51</td>
    <td align="right">58.59</td>
    <td align="right">58.57</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.99</td>
    <td align="right">26.05</td>
    <td align="right">26.02</td>
    <td align="right">26.03</td>
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
    <td align="right">19.85</td>
    <td align="right">23.84</td>
    <td align="right">26.80</td>
    <td align="right">27.71</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.21</td>
    <td align="right">27.30</td>
    <td align="right">29.20</td>
    <td align="right">30.57</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">13.02</td>
    <td align="right">15.64</td>
    <td align="right">23.95</td>
    <td align="right">21.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">27.04</td>
    <td align="right">31.03</td>
    <td align="right">28.24</td>
    <td align="right">32.07</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.00</td>
    <td align="right">34.51</td>
    <td align="right">34.00</td>
    <td align="right">35.49</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.06</td>
    <td align="right">17.60</td>
    <td align="right">25.34</td>
    <td align="right">23.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.24</td>
    <td align="right">43.28</td>
    <td align="right">30.55</td>
    <td align="right">39.37</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.50</td>
    <td align="right">49.30</td>
    <td align="right">39.99</td>
    <td align="right">44.72</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.26</td>
    <td align="right">20.16</td>
    <td align="right">26.37</td>
    <td align="right">25.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.65</td>
    <td align="right">48.59</td>
    <td align="right">29.71</td>
    <td align="right">42.13</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.47</td>
    <td align="right">56.98</td>
    <td align="right">41.89</td>
    <td align="right">49.25</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.89</td>
    <td align="right">27.93</td>
    <td align="right">26.02</td>
    <td align="right">30.53</td>
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
    <td align="right">19.97</td>
    <td align="right">23.80</td>
    <td align="right">23.75</td>
    <td align="right">23.73</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.22</td>
    <td align="right">26.59</td>
    <td align="right">26.68</td>
    <td align="right">26.65</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.82</td>
    <td align="right">15.65</td>
    <td align="right">15.56</td>
    <td align="right">15.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.81</td>
    <td align="right">30.12</td>
    <td align="right">30.09</td>
    <td align="right">30.04</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.04</td>
    <td align="right">34.72</td>
    <td align="right">34.59</td>
    <td align="right">34.72</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.85</td>
    <td align="right">17.79</td>
    <td align="right">18.40</td>
    <td align="right">17.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.45</td>
    <td align="right">36.88</td>
    <td align="right">37.07</td>
    <td align="right">36.92</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.82</td>
    <td align="right">49.01</td>
    <td align="right">48.99</td>
    <td align="right">49.09</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.21</td>
    <td align="right">20.91</td>
    <td align="right">20.90</td>
    <td align="right">20.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.77</td>
    <td align="right">41.59</td>
    <td align="right">41.65</td>
    <td align="right">41.72</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.55</td>
    <td align="right">58.52</td>
    <td align="right">58.53</td>
    <td align="right">58.50</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.21</td>
    <td align="right">26.14</td>
    <td align="right">26.05</td>
    <td align="right">26.04</td>
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
    <td align="right">14.45</td>
    <td align="right">16.50</td>
    <td align="right">24.38</td>
    <td align="right">22.48</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.98</td>
    <td align="right">23.81</td>
    <td align="right">26.81</td>
    <td align="right">27.72</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.27</td>
    <td align="right">27.32</td>
    <td align="right">29.28</td>
    <td align="right">30.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.03</td>
    <td align="right">19.87</td>
    <td align="right">26.63</td>
    <td align="right">25.71</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.69</td>
    <td align="right">30.75</td>
    <td align="right">28.18</td>
    <td align="right">32.19</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.10</td>
    <td align="right">34.63</td>
    <td align="right">34.24</td>
    <td align="right">35.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.50</td>
    <td align="right">23.03</td>
    <td align="right">28.23</td>
    <td align="right">28.52</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.47</td>
    <td align="right">43.25</td>
    <td align="right">30.51</td>
    <td align="right">39.47</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.91</td>
    <td align="right">49.21</td>
    <td align="right">39.97</td>
    <td align="right">44.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.80</td>
    <td align="right">30.64</td>
    <td align="right">28.86</td>
    <td align="right">32.68</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.86</td>
    <td align="right">47.06</td>
    <td align="right">29.62</td>
    <td align="right">42.22</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.56</td>
    <td align="right">56.95</td>
    <td align="right">41.87</td>
    <td align="right">49.60</td>
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
    <td align="right">14.47</td>
    <td align="right">16.85</td>
    <td align="right">16.84</td>
    <td align="right">16.83</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.88</td>
    <td align="right">23.78</td>
    <td align="right">23.74</td>
    <td align="right">23.76</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.23</td>
    <td align="right">26.50</td>
    <td align="right">26.50</td>
    <td align="right">26.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.03</td>
    <td align="right">21.05</td>
    <td align="right">21.08</td>
    <td align="right">21.30</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">27.27</td>
    <td align="right">30.06</td>
    <td align="right">30.09</td>
    <td align="right">30.12</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.05</td>
    <td align="right">34.57</td>
    <td align="right">34.58</td>
    <td align="right">34.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.45</td>
    <td align="right">25.11</td>
    <td align="right">25.11</td>
    <td align="right">25.10</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.16</td>
    <td align="right">37.01</td>
    <td align="right">37.09</td>
    <td align="right">37.01</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.94</td>
    <td align="right">49.02</td>
    <td align="right">49.14</td>
    <td align="right">49.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.67</td>
    <td align="right">33.09</td>
    <td align="right">33.10</td>
    <td align="right">33.11</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.37</td>
    <td align="right">41.42</td>
    <td align="right">41.64</td>
    <td align="right">41.55</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.48</td>
    <td align="right">58.48</td>
    <td align="right">58.48</td>
    <td align="right">58.44</td>
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
    <td align="right">14.49</td>
    <td align="right">16.51</td>
    <td align="right">24.38</td>
    <td align="right">22.46</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.91</td>
    <td align="right">23.88</td>
    <td align="right">26.87</td>
    <td align="right">27.68</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.21</td>
    <td align="right">27.70</td>
    <td align="right">29.18</td>
    <td align="right">30.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.02</td>
    <td align="right">19.81</td>
    <td align="right">26.81</td>
    <td align="right">25.53</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">27.16</td>
    <td align="right">31.14</td>
    <td align="right">28.47</td>
    <td align="right">32.23</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">36.95</td>
    <td align="right">34.50</td>
    <td align="right">33.99</td>
    <td align="right">35.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.57</td>
    <td align="right">22.93</td>
    <td align="right">28.29</td>
    <td align="right">28.09</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.22</td>
    <td align="right">42.68</td>
    <td align="right">30.55</td>
    <td align="right">40.64</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.55</td>
    <td align="right">49.24</td>
    <td align="right">39.92</td>
    <td align="right">44.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.66</td>
    <td align="right">30.63</td>
    <td align="right">29.00</td>
    <td align="right">32.86</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.45</td>
    <td align="right">47.68</td>
    <td align="right">29.55</td>
    <td align="right">42.00</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.46</td>
    <td align="right">56.96</td>
    <td align="right">41.95</td>
    <td align="right">49.27</td>
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
    <td align="right">14.52</td>
    <td align="right">16.84</td>
    <td align="right">16.83</td>
    <td align="right">17.11</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.82</td>
    <td align="right">23.73</td>
    <td align="right">23.76</td>
    <td align="right">23.73</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.21</td>
    <td align="right">26.59</td>
    <td align="right">26.63</td>
    <td align="right">26.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.00</td>
    <td align="right">21.04</td>
    <td align="right">21.06</td>
    <td align="right">21.07</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.80</td>
    <td align="right">30.02</td>
    <td align="right">30.00</td>
    <td align="right">30.11</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">36.96</td>
    <td align="right">34.70</td>
    <td align="right">34.57</td>
    <td align="right">34.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.45</td>
    <td align="right">25.18</td>
    <td align="right">25.08</td>
    <td align="right">25.09</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.95</td>
    <td align="right">37.00</td>
    <td align="right">36.96</td>
    <td align="right">36.90</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.75</td>
    <td align="right">48.97</td>
    <td align="right">48.97</td>
    <td align="right">49.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.80</td>
    <td align="right">33.07</td>
    <td align="right">33.08</td>
    <td align="right">33.06</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.45</td>
    <td align="right">41.54</td>
    <td align="right">41.59</td>
    <td align="right">41.66</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.52</td>
    <td align="right">58.51</td>
    <td align="right">58.52</td>
    <td align="right">58.56</td>
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
    <td align="right">24.51</td>
    <td align="right">28.04</td>
    <td align="right">28.10</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.72</td>
    <td align="right">31.47</td>
    <td align="right">36.17</td>
    <td align="right">33.72</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.05</td>
    <td align="right">36.44</td>
    <td align="right">33.54</td>
    <td align="right">35.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.40</td>
    <td align="right">36.80</td>
    <td align="right">28.57</td>
    <td align="right">36.00</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">44.96</td>
    <td align="right">40.80</td>
    <td align="right">34.21</td>
    <td align="right">39.59</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.25</td>
    <td align="right">47.56</td>
    <td align="right">38.01</td>
    <td align="right">42.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.04</td>
    <td align="right">44.00</td>
    <td align="right">28.17</td>
    <td align="right">40.38</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.46</td>
    <td align="right">49.85</td>
    <td align="right">35.85</td>
    <td align="right">44.31</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.81</td>
    <td align="right">51.97</td>
    <td align="right">32.53</td>
    <td align="right">44.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.26</td>
    <td align="right">49.39</td>
    <td align="right">29.68</td>
    <td align="right">44.44</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.36</td>
    <td align="right">52.64</td>
    <td align="right">36.21</td>
    <td align="right">46.01</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">61.67</td>
    <td align="right">65.10</td>
    <td align="right">35.10</td>
    <td align="right">52.82</td>
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
    <td align="right">24.29</td>
    <td align="right">24.25</td>
    <td align="right">24.20</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.73</td>
    <td align="right">32.64</td>
    <td align="right">32.64</td>
    <td align="right">32.56</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.39</td>
    <td align="right">35.00</td>
    <td align="right">34.80</td>
    <td align="right">34.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.38</td>
    <td align="right">33.65</td>
    <td align="right">33.65</td>
    <td align="right">33.66</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.30</td>
    <td align="right">39.33</td>
    <td align="right">39.33</td>
    <td align="right">39.35</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.65</td>
    <td align="right">44.93</td>
    <td align="right">44.80</td>
    <td align="right">44.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.05</td>
    <td align="right">41.13</td>
    <td align="right">41.14</td>
    <td align="right">41.17</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.46</td>
    <td align="right">48.22</td>
    <td align="right">48.19</td>
    <td align="right">48.28</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.17</td>
    <td align="right">47.33</td>
    <td align="right">47.17</td>
    <td align="right">47.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.27</td>
    <td align="right">46.78</td>
    <td align="right">46.76</td>
    <td align="right">46.70</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.45</td>
    <td align="right">52.41</td>
    <td align="right">52.42</td>
    <td align="right">52.41</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">61.11</td>
    <td align="right">65.43</td>
    <td align="right">65.90</td>
    <td align="right">65.32</td>
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
    <td align="right">18.27</td>
    <td align="right">24.31</td>
    <td align="right">27.89</td>
    <td align="right">28.13</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.18</td>
    <td align="right">31.48</td>
    <td align="right">36.13</td>
    <td align="right">33.77</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.32</td>
    <td align="right">36.94</td>
    <td align="right">35.56</td>
    <td align="right">37.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.31</td>
    <td align="right">36.84</td>
    <td align="right">28.57</td>
    <td align="right">36.69</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.22</td>
    <td align="right">40.68</td>
    <td align="right">34.71</td>
    <td align="right">39.23</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">40.86</td>
    <td align="right">47.63</td>
    <td align="right">35.29</td>
    <td align="right">41.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.07</td>
    <td align="right">43.83</td>
    <td align="right">27.93</td>
    <td align="right">39.79</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.45</td>
    <td align="right">49.80</td>
    <td align="right">36.28</td>
    <td align="right">44.32</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">43.84</td>
    <td align="right">50.69</td>
    <td align="right">32.13</td>
    <td align="right">43.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.26</td>
    <td align="right">49.40</td>
    <td align="right">30.65</td>
    <td align="right">42.70</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.30</td>
    <td align="right">52.58</td>
    <td align="right">35.99</td>
    <td align="right">45.95</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">60.95</td>
    <td align="right">65.27</td>
    <td align="right">35.66</td>
    <td align="right">53.50</td>
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
    <td align="right">18.30</td>
    <td align="right">24.18</td>
    <td align="right">24.20</td>
    <td align="right">24.26</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.18</td>
    <td align="right">32.61</td>
    <td align="right">32.66</td>
    <td align="right">32.60</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.26</td>
    <td align="right">34.71</td>
    <td align="right">34.53</td>
    <td align="right">34.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.27</td>
    <td align="right">33.64</td>
    <td align="right">33.64</td>
    <td align="right">33.63</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">44.94</td>
    <td align="right">39.35</td>
    <td align="right">39.35</td>
    <td align="right">39.40</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.19</td>
    <td align="right">44.85</td>
    <td align="right">44.97</td>
    <td align="right">44.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.08</td>
    <td align="right">41.34</td>
    <td align="right">41.12</td>
    <td align="right">41.17</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.40</td>
    <td align="right">48.22</td>
    <td align="right">48.22</td>
    <td align="right">48.21</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">43.67</td>
    <td align="right">47.32</td>
    <td align="right">47.44</td>
    <td align="right">47.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.25</td>
    <td align="right">47.02</td>
    <td align="right">46.78</td>
    <td align="right">46.81</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.32</td>
    <td align="right">52.41</td>
    <td align="right">52.45</td>
    <td align="right">52.44</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">60.94</td>
    <td align="right">64.58</td>
    <td align="right">65.18</td>
    <td align="right">65.21</td>
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
    <td align="right">108.09</td>
    <td align="right">125.90</td>
    <td align="right">27.13</td>
    <td align="right">82.75</td>
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
    <td align="right">38.05</td>
    <td align="right">53.56</td>
    <td align="right">40.67</td>
    <td align="right">47.78</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.64</td>
    <td align="right">18.89</td>
    <td align="right">18.75</td>
    <td align="right">19.06</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.40</td>
    <td align="right">20.72</td>
    <td align="right">22.30</td>
    <td align="right">20.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">101.48</td>
    <td align="right">131.76</td>
    <td align="right">54.61</td>
    <td align="right">94.03</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.72</td>
    <td align="right">27.85</td>
    <td align="right">27.33</td>
    <td align="right">27.88</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.47</td>
    <td align="right">28.49</td>
    <td align="right">28.49</td>
    <td align="right">28.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">187.93</td>
    <td align="right">244.96</td>
    <td align="right">69.87</td>
    <td align="right">159.34</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.33</td>
    <td align="right">46.89</td>
    <td align="right">46.78</td>
    <td align="right">46.73</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.98</td>
    <td align="right">49.88</td>
    <td align="right">49.85</td>
    <td align="right">50.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.30</td>
    <td align="right">352.49</td>
    <td align="right">83.53</td>
    <td align="right">238.55</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">46.85</td>
    <td align="right">63.43</td>
    <td align="right">63.23</td>
    <td align="right">63.20</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">62.87</td>
    <td align="right">65.23</td>
    <td align="right">65.16</td>
    <td align="right">65.17</td>
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
    <td align="right">37.57</td>
    <td align="right">47.18</td>
    <td align="right">47.42</td>
    <td align="right">47.62</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.68</td>
    <td align="right">19.60</td>
    <td align="right">19.54</td>
    <td align="right">19.39</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.27</td>
    <td align="right">20.41</td>
    <td align="right">20.33</td>
    <td align="right">20.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">92.51</td>
    <td align="right">109.65</td>
    <td align="right">109.51</td>
    <td align="right">109.58</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.47</td>
    <td align="right">28.42</td>
    <td align="right">27.88</td>
    <td align="right">28.09</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.75</td>
    <td align="right">32.73</td>
    <td align="right">31.55</td>
    <td align="right">31.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">190.73</td>
    <td align="right">180.56</td>
    <td align="right">181.65</td>
    <td align="right">180.72</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.32</td>
    <td align="right">46.59</td>
    <td align="right">46.46</td>
    <td align="right">46.52</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.04</td>
    <td align="right">48.46</td>
    <td align="right">48.16</td>
    <td align="right">48.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">300.29</td>
    <td align="right">420.04</td>
    <td align="right">454.53</td>
    <td align="right">453.11</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.04</td>
    <td align="right">64.15</td>
    <td align="right">64.16</td>
    <td align="right">69.32</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.39</td>
    <td align="right">65.03</td>
    <td align="right">66.26</td>
    <td align="right">70.70</td>
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
    <td align="right">38.15</td>
    <td align="right">55.49</td>
    <td align="right">41.01</td>
    <td align="right">49.03</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.91</td>
    <td align="right">21.71</td>
    <td align="right">21.69</td>
    <td align="right">21.75</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.38</td>
    <td align="right">27.17</td>
    <td align="right">27.17</td>
    <td align="right">26.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">90.16</td>
    <td align="right">116.83</td>
    <td align="right">51.38</td>
    <td align="right">86.37</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.94</td>
    <td align="right">36.28</td>
    <td align="right">36.10</td>
    <td align="right">36.27</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.32</td>
    <td align="right">33.88</td>
    <td align="right">33.85</td>
    <td align="right">33.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">191.58</td>
    <td align="right">256.16</td>
    <td align="right">74.73</td>
    <td align="right">166.95</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">38.12</td>
    <td align="right">47.79</td>
    <td align="right">47.72</td>
    <td align="right">47.75</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.12</td>
    <td align="right">52.61</td>
    <td align="right">52.32</td>
    <td align="right">52.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.20</td>
    <td align="right">369.57</td>
    <td align="right">85.00</td>
    <td align="right">228.39</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.35</td>
    <td align="right">63.98</td>
    <td align="right">64.01</td>
    <td align="right">64.00</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">62.80</td>
    <td align="right">68.48</td>
    <td align="right">68.24</td>
    <td align="right">68.19</td>
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
    <td align="right">41.42</td>
    <td align="right">58.13</td>
    <td align="right">58.04</td>
    <td align="right">58.02</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.05</td>
    <td align="right">22.00</td>
    <td align="right">21.96</td>
    <td align="right">22.03</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.92</td>
    <td align="right">26.75</td>
    <td align="right">26.76</td>
    <td align="right">26.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">93.72</td>
    <td align="right">118.95</td>
    <td align="right">118.61</td>
    <td align="right">118.49</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.00</td>
    <td align="right">32.87</td>
    <td align="right">32.84</td>
    <td align="right">32.86</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.37</td>
    <td align="right">34.15</td>
    <td align="right">34.15</td>
    <td align="right">34.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">190.33</td>
    <td align="right">206.90</td>
    <td align="right">207.72</td>
    <td align="right">206.17</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.63</td>
    <td align="right">48.10</td>
    <td align="right">48.10</td>
    <td align="right">48.03</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.99</td>
    <td align="right">51.65</td>
    <td align="right">51.44</td>
    <td align="right">51.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">296.81</td>
    <td align="right">414.97</td>
    <td align="right">415.39</td>
    <td align="right">415.26</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">46.99</td>
    <td align="right">64.62</td>
    <td align="right">64.59</td>
    <td align="right">63.99</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">62.88</td>
    <td align="right">67.89</td>
    <td align="right">68.08</td>
    <td align="right">68.03</td>
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
    <td align="right">24.35</td>
    <td align="right">28.72</td>
    <td align="right">30.40</td>
    <td align="right">33.45</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.01</td>
    <td align="right">34.15</td>
    <td align="right">32.26</td>
    <td align="right">36.87</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.24</td>
    <td align="right">18.58</td>
    <td align="right">26.54</td>
    <td align="right">25.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.11</td>
    <td align="right">45.10</td>
    <td align="right">38.24</td>
    <td align="right">46.15</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">55.06</td>
    <td align="right">55.46</td>
    <td align="right">47.46</td>
    <td align="right">54.33</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">24.99</td>
    <td align="right">28.14</td>
    <td align="right">34.11</td>
    <td align="right">33.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.28</td>
    <td align="right">76.87</td>
    <td align="right">49.37</td>
    <td align="right">70.77</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.17</td>
    <td align="right">82.39</td>
    <td align="right">66.37</td>
    <td align="right">76.66</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.40</td>
    <td align="right">44.37</td>
    <td align="right">44.04</td>
    <td align="right">46.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.82</td>
    <td align="right">98.60</td>
    <td align="right">56.65</td>
    <td align="right">89.76</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.65</td>
    <td align="right">109.72</td>
    <td align="right">88.53</td>
    <td align="right">99.94</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.66</td>
    <td align="right">73.90</td>
    <td align="right">49.02</td>
    <td align="right">71.58</td>
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
    <td align="right">24.39</td>
    <td align="right">28.65</td>
    <td align="right">28.64</td>
    <td align="right">28.47</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">31.13</td>
    <td align="right">32.66</td>
    <td align="right">32.69</td>
    <td align="right">32.64</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">16.19</td>
    <td align="right">19.88</td>
    <td align="right">20.29</td>
    <td align="right">19.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.85</td>
    <td align="right">44.89</td>
    <td align="right">44.84</td>
    <td align="right">44.84</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.96</td>
    <td align="right">49.25</td>
    <td align="right">49.21</td>
    <td align="right">49.20</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">26.31</td>
    <td align="right">26.46</td>
    <td align="right">27.32</td>
    <td align="right">26.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.84</td>
    <td align="right">72.73</td>
    <td align="right">72.85</td>
    <td align="right">72.83</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.31</td>
    <td align="right">81.72</td>
    <td align="right">81.75</td>
    <td align="right">81.71</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.38</td>
    <td align="right">48.24</td>
    <td align="right">47.31</td>
    <td align="right">47.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.23</td>
    <td align="right">94.76</td>
    <td align="right">94.93</td>
    <td align="right">94.69</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.44</td>
    <td align="right">110.26</td>
    <td align="right">110.31</td>
    <td align="right">110.29</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.94</td>
    <td align="right">75.34</td>
    <td align="right">75.28</td>
    <td align="right">75.51</td>
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
    <td align="right">22.73</td>
    <td align="right">27.15</td>
    <td align="right">29.63</td>
    <td align="right">31.80</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.02</td>
    <td align="right">32.38</td>
    <td align="right">32.07</td>
    <td align="right">36.01</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">14.59</td>
    <td align="right">16.87</td>
    <td align="right">26.59</td>
    <td align="right">24.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">42.23</td>
    <td align="right">46.37</td>
    <td align="right">39.40</td>
    <td align="right">47.48</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.93</td>
    <td align="right">53.52</td>
    <td align="right">46.35</td>
    <td align="right">53.58</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">26.87</td>
    <td align="right">28.78</td>
    <td align="right">35.14</td>
    <td align="right">34.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">69.39</td>
    <td align="right">78.07</td>
    <td align="right">50.17</td>
    <td align="right">71.13</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.30</td>
    <td align="right">82.56</td>
    <td align="right">66.44</td>
    <td align="right">76.77</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.73</td>
    <td align="right">44.68</td>
    <td align="right">44.52</td>
    <td align="right">47.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.56</td>
    <td align="right">96.65</td>
    <td align="right">56.09</td>
    <td align="right">86.42</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.45</td>
    <td align="right">109.71</td>
    <td align="right">91.61</td>
    <td align="right">101.07</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.38</td>
    <td align="right">74.26</td>
    <td align="right">49.29</td>
    <td align="right">72.14</td>
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
    <td align="right">23.99</td>
    <td align="right">28.22</td>
    <td align="right">28.03</td>
    <td align="right">28.03</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.38</td>
    <td align="right">31.91</td>
    <td align="right">31.85</td>
    <td align="right">31.86</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">16.03</td>
    <td align="right">19.37</td>
    <td align="right">21.11</td>
    <td align="right">20.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.57</td>
    <td align="right">44.76</td>
    <td align="right">44.59</td>
    <td align="right">44.76</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.76</td>
    <td align="right">52.16</td>
    <td align="right">50.63</td>
    <td align="right">52.17</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">23.83</td>
    <td align="right">26.50</td>
    <td align="right">27.03</td>
    <td align="right">27.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.93</td>
    <td align="right">72.18</td>
    <td align="right">72.24</td>
    <td align="right">72.29</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.72</td>
    <td align="right">83.23</td>
    <td align="right">83.28</td>
    <td align="right">83.34</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.55</td>
    <td align="right">46.54</td>
    <td align="right">46.59</td>
    <td align="right">46.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.99</td>
    <td align="right">94.43</td>
    <td align="right">94.43</td>
    <td align="right">94.33</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.49</td>
    <td align="right">110.25</td>
    <td align="right">110.37</td>
    <td align="right">110.30</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.80</td>
    <td align="right">76.42</td>
    <td align="right">76.41</td>
    <td align="right">76.39</td>
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
    <td align="right">17.03</td>
    <td align="right">19.53</td>
    <td align="right">29.22</td>
    <td align="right">28.80</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.20</td>
    <td align="right">27.85</td>
    <td align="right">30.09</td>
    <td align="right">32.47</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.62</td>
    <td align="right">34.99</td>
    <td align="right">33.03</td>
    <td align="right">38.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">29.87</td>
    <td align="right">31.41</td>
    <td align="right">36.72</td>
    <td align="right">36.68</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.30</td>
    <td align="right">44.60</td>
    <td align="right">36.93</td>
    <td align="right">45.99</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.14</td>
    <td align="right">54.70</td>
    <td align="right">47.06</td>
    <td align="right">53.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.59</td>
    <td align="right">47.71</td>
    <td align="right">51.25</td>
    <td align="right">51.67</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.46</td>
    <td align="right">78.61</td>
    <td align="right">50.52</td>
    <td align="right">72.08</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.12</td>
    <td align="right">84.15</td>
    <td align="right">67.69</td>
    <td align="right">78.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.16</td>
    <td align="right">81.71</td>
    <td align="right">60.63</td>
    <td align="right">79.62</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.16</td>
    <td align="right">98.51</td>
    <td align="right">55.86</td>
    <td align="right">87.24</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.89</td>
    <td align="right">109.53</td>
    <td align="right">88.30</td>
    <td align="right">99.89</td>
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
    <td align="right">16.69</td>
    <td align="right">19.59</td>
    <td align="right">19.71</td>
    <td align="right">19.68</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.64</td>
    <td align="right">27.75</td>
    <td align="right">27.82</td>
    <td align="right">27.76</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.57</td>
    <td align="right">32.07</td>
    <td align="right">31.99</td>
    <td align="right">32.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.25</td>
    <td align="right">32.91</td>
    <td align="right">34.20</td>
    <td align="right">33.68</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.44</td>
    <td align="right">44.54</td>
    <td align="right">44.63</td>
    <td align="right">44.54</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.15</td>
    <td align="right">51.07</td>
    <td align="right">51.02</td>
    <td align="right">50.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.43</td>
    <td align="right">56.71</td>
    <td align="right">56.67</td>
    <td align="right">56.73</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.65</td>
    <td align="right">73.75</td>
    <td align="right">72.92</td>
    <td align="right">73.19</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.26</td>
    <td align="right">82.54</td>
    <td align="right">82.82</td>
    <td align="right">82.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.13</td>
    <td align="right">84.90</td>
    <td align="right">84.97</td>
    <td align="right">85.16</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.53</td>
    <td align="right">93.79</td>
    <td align="right">94.05</td>
    <td align="right">93.79</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">133.63</td>
    <td align="right">108.00</td>
    <td align="right">107.99</td>
    <td align="right">107.97</td>
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
    <td align="right">16.40</td>
    <td align="right">18.92</td>
    <td align="right">28.91</td>
    <td align="right">26.85</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.23</td>
    <td align="right">28.54</td>
    <td align="right">30.41</td>
    <td align="right">33.26</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.70</td>
    <td align="right">32.59</td>
    <td align="right">31.06</td>
    <td align="right">35.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">29.86</td>
    <td align="right">30.51</td>
    <td align="right">36.73</td>
    <td align="right">37.33</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.11</td>
    <td align="right">42.40</td>
    <td align="right">37.04</td>
    <td align="right">43.84</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.23</td>
    <td align="right">53.29</td>
    <td align="right">47.15</td>
    <td align="right">53.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.58</td>
    <td align="right">46.25</td>
    <td align="right">49.76</td>
    <td align="right">50.13</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.93</td>
    <td align="right">78.67</td>
    <td align="right">49.75</td>
    <td align="right">71.45</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.02</td>
    <td align="right">84.41</td>
    <td align="right">67.65</td>
    <td align="right">78.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">81.13</td>
    <td align="right">79.01</td>
    <td align="right">58.36</td>
    <td align="right">76.80</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.69</td>
    <td align="right">100.03</td>
    <td align="right">56.28</td>
    <td align="right">87.90</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">133.94</td>
    <td align="right">109.13</td>
    <td align="right">87.97</td>
    <td align="right">99.39</td>
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
    <td align="right">16.85</td>
    <td align="right">20.66</td>
    <td align="right">20.32</td>
    <td align="right">19.61</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.49</td>
    <td align="right">28.37</td>
    <td align="right">28.42</td>
    <td align="right">28.36</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.44</td>
    <td align="right">31.97</td>
    <td align="right">32.29</td>
    <td align="right">32.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">29.49</td>
    <td align="right">31.76</td>
    <td align="right">31.74</td>
    <td align="right">31.93</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.20</td>
    <td align="right">44.68</td>
    <td align="right">44.75</td>
    <td align="right">44.71</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.78</td>
    <td align="right">53.26</td>
    <td align="right">51.80</td>
    <td align="right">53.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.75</td>
    <td align="right">56.85</td>
    <td align="right">55.85</td>
    <td align="right">55.85</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.64</td>
    <td align="right">73.04</td>
    <td align="right">72.75</td>
    <td align="right">72.56</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.38</td>
    <td align="right">82.24</td>
    <td align="right">82.33</td>
    <td align="right">82.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.84</td>
    <td align="right">84.28</td>
    <td align="right">84.26</td>
    <td align="right">84.37</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.24</td>
    <td align="right">94.41</td>
    <td align="right">97.13</td>
    <td align="right">95.51</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.67</td>
    <td align="right">110.35</td>
    <td align="right">110.37</td>
    <td align="right">110.29</td>
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
    <td align="right">21.75</td>
    <td align="right">29.28</td>
    <td align="right">31.98</td>
    <td align="right">33.49</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.26</td>
    <td align="right">36.09</td>
    <td align="right">41.23</td>
    <td align="right">39.70</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">33.92</td>
    <td align="right">42.18</td>
    <td align="right">38.44</td>
    <td align="right">41.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.31</td>
    <td align="right">52.24</td>
    <td align="right">39.08</td>
    <td align="right">51.40</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">60.44</td>
    <td align="right">60.57</td>
    <td align="right">47.69</td>
    <td align="right">59.69</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">63.63</td>
    <td align="right">72.22</td>
    <td align="right">46.31</td>
    <td align="right">61.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.80</td>
    <td align="right">73.43</td>
    <td align="right">47.51</td>
    <td align="right">69.30</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.71</td>
    <td align="right">88.40</td>
    <td align="right">59.77</td>
    <td align="right">80.09</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">91.32</td>
    <td align="right">94.56</td>
    <td align="right">44.58</td>
    <td align="right">77.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">84.23</td>
    <td align="right">90.59</td>
    <td align="right">56.65</td>
    <td align="right">86.06</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">105.61</td>
    <td align="right">105.01</td>
    <td align="right">68.14</td>
    <td align="right">94.23</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.17</td>
    <td align="right">138.23</td>
    <td align="right">51.56</td>
    <td align="right">107.57</td>
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
    <td align="right">20.70</td>
    <td align="right">28.23</td>
    <td align="right">27.94</td>
    <td align="right">27.92</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">37.06</td>
    <td align="right">39.51</td>
    <td align="right">39.53</td>
    <td align="right">37.99</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">35.81</td>
    <td align="right">40.10</td>
    <td align="right">40.01</td>
    <td align="right">40.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.52</td>
    <td align="right">46.90</td>
    <td align="right">46.84</td>
    <td align="right">46.78</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">59.46</td>
    <td align="right">58.16</td>
    <td align="right">58.19</td>
    <td align="right">58.16</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">66.88</td>
    <td align="right">62.90</td>
    <td align="right">62.85</td>
    <td align="right">62.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.81</td>
    <td align="right">68.41</td>
    <td align="right">68.47</td>
    <td align="right">68.61</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">86.89</td>
    <td align="right">85.60</td>
    <td align="right">85.69</td>
    <td align="right">85.71</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">90.31</td>
    <td align="right">95.35</td>
    <td align="right">95.40</td>
    <td align="right">97.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.64</td>
    <td align="right">88.02</td>
    <td align="right">87.95</td>
    <td align="right">87.82</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">105.22</td>
    <td align="right">105.67</td>
    <td align="right">105.64</td>
    <td align="right">105.65</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.46</td>
    <td align="right">143.61</td>
    <td align="right">144.38</td>
    <td align="right">142.85</td>
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
    <td align="right">21.58</td>
    <td align="right">29.24</td>
    <td align="right">31.15</td>
    <td align="right">33.23</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">34.98</td>
    <td align="right">35.87</td>
    <td align="right">39.76</td>
    <td align="right">39.43</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">35.60</td>
    <td align="right">45.58</td>
    <td align="right">40.38</td>
    <td align="right">43.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.87</td>
    <td align="right">47.50</td>
    <td align="right">36.66</td>
    <td align="right">47.17</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">58.69</td>
    <td align="right">58.15</td>
    <td align="right">45.88</td>
    <td align="right">55.90</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">63.74</td>
    <td align="right">71.76</td>
    <td align="right">46.80</td>
    <td align="right">63.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.32</td>
    <td align="right">75.16</td>
    <td align="right">49.47</td>
    <td align="right">70.61</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">85.80</td>
    <td align="right">87.95</td>
    <td align="right">60.01</td>
    <td align="right">79.96</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">89.10</td>
    <td align="right">94.02</td>
    <td align="right">45.24</td>
    <td align="right">78.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.00</td>
    <td align="right">90.27</td>
    <td align="right">57.27</td>
    <td align="right">89.03</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">103.75</td>
    <td align="right">104.13</td>
    <td align="right">67.64</td>
    <td align="right">93.94</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.93</td>
    <td align="right">142.47</td>
    <td align="right">51.56</td>
    <td align="right">111.06</td>
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
    <td align="right">20.68</td>
    <td align="right">27.70</td>
    <td align="right">27.55</td>
    <td align="right">27.82</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.93</td>
    <td align="right">38.04</td>
    <td align="right">39.50</td>
    <td align="right">37.93</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">36.35</td>
    <td align="right">41.10</td>
    <td align="right">40.86</td>
    <td align="right">40.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.22</td>
    <td align="right">47.12</td>
    <td align="right">47.06</td>
    <td align="right">47.11</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">60.36</td>
    <td align="right">59.00</td>
    <td align="right">58.93</td>
    <td align="right">58.92</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">65.52</td>
    <td align="right">67.83</td>
    <td align="right">67.90</td>
    <td align="right">67.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.49</td>
    <td align="right">69.86</td>
    <td align="right">69.84</td>
    <td align="right">69.79</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.20</td>
    <td align="right">85.78</td>
    <td align="right">85.77</td>
    <td align="right">85.78</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">89.96</td>
    <td align="right">94.99</td>
    <td align="right">94.99</td>
    <td align="right">95.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.82</td>
    <td align="right">87.66</td>
    <td align="right">87.57</td>
    <td align="right">87.50</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.86</td>
    <td align="right">104.92</td>
    <td align="right">104.95</td>
    <td align="right">104.94</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.51</td>
    <td align="right">142.71</td>
    <td align="right">143.02</td>
    <td align="right">142.66</td>
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
    <td align="right">78.97</td>
    <td align="right">14.04</td>
    <td align="right">8.55</td>
    <td align="right">17.97</td>
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
    <td align="right">21.42</td>
    <td align="right">32.13</td>
    <td align="right">29.18</td>
    <td align="right">31.02</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.44</td>
    <td align="right">14.06</td>
    <td align="right">13.93</td>
    <td align="right">14.03</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.81</td>
    <td align="right">18.00</td>
    <td align="right">18.01</td>
    <td align="right">18.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.69</td>
    <td align="right">48.92</td>
    <td align="right">30.74</td>
    <td align="right">40.51</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.14</td>
    <td align="right">18.41</td>
    <td align="right">18.40</td>
    <td align="right">18.45</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.21</td>
    <td align="right">20.75</td>
    <td align="right">20.74</td>
    <td align="right">20.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.48</td>
    <td align="right">65.65</td>
    <td align="right">31.36</td>
    <td align="right">49.82</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.62</td>
    <td align="right">21.15</td>
    <td align="right">21.16</td>
    <td align="right">21.26</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.08</td>
    <td align="right">22.94</td>
    <td align="right">22.96</td>
    <td align="right">22.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">59.41</td>
    <td align="right">81.84</td>
    <td align="right">32.07</td>
    <td align="right">62.65</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.20</td>
    <td align="right">23.25</td>
    <td align="right">23.18</td>
    <td align="right">23.29</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.07</td>
    <td align="right">25.71</td>
    <td align="right">25.76</td>
    <td align="right">25.80</td>
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
    <td align="right">21.66</td>
    <td align="right">30.25</td>
    <td align="right">30.51</td>
    <td align="right">29.97</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.45</td>
    <td align="right">13.92</td>
    <td align="right">13.95</td>
    <td align="right">14.06</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.86</td>
    <td align="right">18.03</td>
    <td align="right">18.03</td>
    <td align="right">18.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.59</td>
    <td align="right">46.13</td>
    <td align="right">46.87</td>
    <td align="right">46.14</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.15</td>
    <td align="right">18.42</td>
    <td align="right">18.42</td>
    <td align="right">18.47</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.20</td>
    <td align="right">20.73</td>
    <td align="right">20.81</td>
    <td align="right">20.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.39</td>
    <td align="right">56.97</td>
    <td align="right">57.27</td>
    <td align="right">56.72</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.70</td>
    <td align="right">21.19</td>
    <td align="right">21.15</td>
    <td align="right">21.16</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.08</td>
    <td align="right">22.96</td>
    <td align="right">22.93</td>
    <td align="right">22.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">63.98</td>
    <td align="right">72.56</td>
    <td align="right">74.14</td>
    <td align="right">73.30</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.19</td>
    <td align="right">23.17</td>
    <td align="right">23.24</td>
    <td align="right">23.18</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.08</td>
    <td align="right">25.76</td>
    <td align="right">25.71</td>
    <td align="right">25.73</td>
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
    <td align="right">21.49</td>
    <td align="right">32.28</td>
    <td align="right">29.26</td>
    <td align="right">30.89</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.47</td>
    <td align="right">13.92</td>
    <td align="right">13.92</td>
    <td align="right">13.99</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.82</td>
    <td align="right">18.05</td>
    <td align="right">18.03</td>
    <td align="right">18.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.74</td>
    <td align="right">48.83</td>
    <td align="right">31.09</td>
    <td align="right">40.64</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.13</td>
    <td align="right">18.42</td>
    <td align="right">18.42</td>
    <td align="right">18.41</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.20</td>
    <td align="right">20.71</td>
    <td align="right">20.72</td>
    <td align="right">20.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.31</td>
    <td align="right">64.77</td>
    <td align="right">31.09</td>
    <td align="right">49.77</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.57</td>
    <td align="right">21.17</td>
    <td align="right">21.23</td>
    <td align="right">21.31</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.09</td>
    <td align="right">22.96</td>
    <td align="right">22.96</td>
    <td align="right">22.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">63.72</td>
    <td align="right">81.83</td>
    <td align="right">31.95</td>
    <td align="right">58.55</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.25</td>
    <td align="right">23.28</td>
    <td align="right">23.29</td>
    <td align="right">23.28</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.09</td>
    <td align="right">25.72</td>
    <td align="right">25.72</td>
    <td align="right">25.77</td>
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
    <td align="right">21.52</td>
    <td align="right">30.10</td>
    <td align="right">30.10</td>
    <td align="right">30.10</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.46</td>
    <td align="right">14.00</td>
    <td align="right">13.92</td>
    <td align="right">14.04</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.84</td>
    <td align="right">18.00</td>
    <td align="right">18.01</td>
    <td align="right">18.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.71</td>
    <td align="right">46.11</td>
    <td align="right">46.19</td>
    <td align="right">46.19</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.15</td>
    <td align="right">18.41</td>
    <td align="right">18.41</td>
    <td align="right">18.41</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.18</td>
    <td align="right">20.72</td>
    <td align="right">20.74</td>
    <td align="right">20.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.27</td>
    <td align="right">57.22</td>
    <td align="right">57.01</td>
    <td align="right">57.21</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.58</td>
    <td align="right">21.16</td>
    <td align="right">21.29</td>
    <td align="right">21.33</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.09</td>
    <td align="right">22.93</td>
    <td align="right">22.96</td>
    <td align="right">22.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">64.51</td>
    <td align="right">71.88</td>
    <td align="right">70.24</td>
    <td align="right">69.58</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.18</td>
    <td align="right">23.17</td>
    <td align="right">23.25</td>
    <td align="right">23.17</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.07</td>
    <td align="right">25.87</td>
    <td align="right">25.72</td>
    <td align="right">25.71</td>
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
    <td align="right">17.05</td>
    <td align="right">20.08</td>
    <td align="right">23.48</td>
    <td align="right">24.08</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.04</td>
    <td align="right">20.08</td>
    <td align="right">23.56</td>
    <td align="right">23.60</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.99</td>
    <td align="right">9.38</td>
    <td align="right">18.39</td>
    <td align="right">15.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.94</td>
    <td align="right">25.36</td>
    <td align="right">28.29</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.61</td>
    <td align="right">27.44</td>
    <td align="right">25.35</td>
    <td align="right">28.17</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.93</td>
    <td align="right">13.94</td>
    <td align="right">21.45</td>
    <td align="right">19.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.05</td>
    <td align="right">37.09</td>
    <td align="right">26.28</td>
    <td align="right">34.30</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.43</td>
    <td align="right">38.31</td>
    <td align="right">26.30</td>
    <td align="right">34.51</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.85</td>
    <td align="right">16.87</td>
    <td align="right">22.22</td>
    <td align="right">21.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.71</td>
    <td align="right">41.34</td>
    <td align="right">26.33</td>
    <td align="right">36.73</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.35</td>
    <td align="right">46.48</td>
    <td align="right">26.39</td>
    <td align="right">38.84</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.15</td>
    <td align="right">21.05</td>
    <td align="right">22.03</td>
    <td align="right">25.65</td>
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
    <td align="right">17.04</td>
    <td align="right">18.45</td>
    <td align="right">18.34</td>
    <td align="right">18.32</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.06</td>
    <td align="right">19.01</td>
    <td align="right">18.85</td>
    <td align="right">18.85</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.98</td>
    <td align="right">8.91</td>
    <td align="right">8.72</td>
    <td align="right">8.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">26.60</td>
    <td align="right">26.53</td>
    <td align="right">26.54</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.61</td>
    <td align="right">26.97</td>
    <td align="right">26.98</td>
    <td align="right">26.98</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.91</td>
    <td align="right">13.73</td>
    <td align="right">13.75</td>
    <td align="right">13.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.09</td>
    <td align="right">35.83</td>
    <td align="right">35.79</td>
    <td align="right">35.77</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.43</td>
    <td align="right">34.34</td>
    <td align="right">34.30</td>
    <td align="right">34.31</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.86</td>
    <td align="right">17.83</td>
    <td align="right">17.83</td>
    <td align="right">17.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.75</td>
    <td align="right">38.42</td>
    <td align="right">38.51</td>
    <td align="right">38.51</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.35</td>
    <td align="right">40.88</td>
    <td align="right">41.12</td>
    <td align="right">40.93</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.15</td>
    <td align="right">19.70</td>
    <td align="right">19.70</td>
    <td align="right">19.70</td>
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
    <td align="right">17.05</td>
    <td align="right">20.04</td>
    <td align="right">23.61</td>
    <td align="right">24.23</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.13</td>
    <td align="right">19.62</td>
    <td align="right">23.54</td>
    <td align="right">23.43</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.58</td>
    <td align="right">9.19</td>
    <td align="right">18.53</td>
    <td align="right">15.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.82</td>
    <td align="right">25.35</td>
    <td align="right">28.49</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.08</td>
    <td align="right">27.51</td>
    <td align="right">25.23</td>
    <td align="right">28.47</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.95</td>
    <td align="right">14.10</td>
    <td align="right">21.50</td>
    <td align="right">20.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">34.10</td>
    <td align="right">38.36</td>
    <td align="right">26.99</td>
    <td align="right">34.90</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.46</td>
    <td align="right">38.06</td>
    <td align="right">25.92</td>
    <td align="right">34.36</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.84</td>
    <td align="right">17.38</td>
    <td align="right">21.78</td>
    <td align="right">22.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.53</td>
    <td align="right">44.14</td>
    <td align="right">26.17</td>
    <td align="right">38.41</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.36</td>
    <td align="right">45.88</td>
    <td align="right">26.33</td>
    <td align="right">38.29</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.07</td>
    <td align="right">20.86</td>
    <td align="right">21.70</td>
    <td align="right">25.49</td>
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
    <td align="right">17.08</td>
    <td align="right">18.30</td>
    <td align="right">18.29</td>
    <td align="right">18.32</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.21</td>
    <td align="right">18.86</td>
    <td align="right">18.87</td>
    <td align="right">18.86</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.56</td>
    <td align="right">8.70</td>
    <td align="right">8.71</td>
    <td align="right">8.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">26.60</td>
    <td align="right">26.53</td>
    <td align="right">26.56</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.08</td>
    <td align="right">27.02</td>
    <td align="right">27.00</td>
    <td align="right">27.01</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.92</td>
    <td align="right">13.74</td>
    <td align="right">13.74</td>
    <td align="right">13.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">34.09</td>
    <td align="right">36.26</td>
    <td align="right">36.24</td>
    <td align="right">36.27</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.49</td>
    <td align="right">34.56</td>
    <td align="right">34.68</td>
    <td align="right">34.35</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.86</td>
    <td align="right">17.19</td>
    <td align="right">17.22</td>
    <td align="right">17.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.54</td>
    <td align="right">39.01</td>
    <td align="right">39.01</td>
    <td align="right">38.99</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.20</td>
    <td align="right">40.76</td>
    <td align="right">40.85</td>
    <td align="right">40.91</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.09</td>
    <td align="right">19.80</td>
    <td align="right">19.80</td>
    <td align="right">19.80</td>
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
    <td align="right">9.06</td>
    <td align="right">17.77</td>
    <td align="right">15.24</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.04</td>
    <td align="right">20.12</td>
    <td align="right">23.50</td>
    <td align="right">24.09</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.06</td>
    <td align="right">20.06</td>
    <td align="right">23.55</td>
    <td align="right">23.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.89</td>
    <td align="right">15.22</td>
    <td align="right">21.70</td>
    <td align="right">20.96</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">26.64</td>
    <td align="right">25.33</td>
    <td align="right">28.28</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.61</td>
    <td align="right">27.42</td>
    <td align="right">25.37</td>
    <td align="right">28.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.27</td>
    <td align="right">17.06</td>
    <td align="right">21.82</td>
    <td align="right">22.64</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.06</td>
    <td align="right">37.11</td>
    <td align="right">26.29</td>
    <td align="right">34.29</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.41</td>
    <td align="right">38.11</td>
    <td align="right">26.24</td>
    <td align="right">34.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.77</td>
    <td align="right">20.42</td>
    <td align="right">20.70</td>
    <td align="right">25.14</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.75</td>
    <td align="right">41.57</td>
    <td align="right">26.35</td>
    <td align="right">36.82</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.38</td>
    <td align="right">46.47</td>
    <td align="right">26.40</td>
    <td align="right">38.96</td>
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
    <td align="right">7.50</td>
    <td align="right">8.89</td>
    <td align="right">8.52</td>
    <td align="right">8.50</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.05</td>
    <td align="right">18.32</td>
    <td align="right">18.32</td>
    <td align="right">18.45</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.02</td>
    <td align="right">18.84</td>
    <td align="right">18.84</td>
    <td align="right">18.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.95</td>
    <td align="right">14.13</td>
    <td align="right">14.12</td>
    <td align="right">14.12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.60</td>
    <td align="right">26.55</td>
    <td align="right">26.54</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.62</td>
    <td align="right">26.98</td>
    <td align="right">27.00</td>
    <td align="right">26.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.29</td>
    <td align="right">17.24</td>
    <td align="right">17.25</td>
    <td align="right">17.24</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.01</td>
    <td align="right">35.84</td>
    <td align="right">35.83</td>
    <td align="right">35.81</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.37</td>
    <td align="right">34.58</td>
    <td align="right">34.25</td>
    <td align="right">34.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.80</td>
    <td align="right">20.24</td>
    <td align="right">20.24</td>
    <td align="right">20.24</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.70</td>
    <td align="right">38.50</td>
    <td align="right">38.53</td>
    <td align="right">38.54</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.37</td>
    <td align="right">40.90</td>
    <td align="right">41.12</td>
    <td align="right">40.95</td>
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
    <td align="right">7.11</td>
    <td align="right">9.04</td>
    <td align="right">17.78</td>
    <td align="right">15.03</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.04</td>
    <td align="right">20.10</td>
    <td align="right">23.56</td>
    <td align="right">24.19</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.16</td>
    <td align="right">19.86</td>
    <td align="right">23.67</td>
    <td align="right">23.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.80</td>
    <td align="right">14.73</td>
    <td align="right">21.58</td>
    <td align="right">20.69</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.66</td>
    <td align="right">26.82</td>
    <td align="right">25.32</td>
    <td align="right">28.46</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.07</td>
    <td align="right">26.96</td>
    <td align="right">25.33</td>
    <td align="right">28.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.19</td>
    <td align="right">17.08</td>
    <td align="right">21.68</td>
    <td align="right">22.74</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">34.12</td>
    <td align="right">38.49</td>
    <td align="right">27.00</td>
    <td align="right">34.94</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.50</td>
    <td align="right">38.19</td>
    <td align="right">25.98</td>
    <td align="right">34.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.79</td>
    <td align="right">20.23</td>
    <td align="right">20.69</td>
    <td align="right">24.92</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.42</td>
    <td align="right">43.50</td>
    <td align="right">26.16</td>
    <td align="right">38.24</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.15</td>
    <td align="right">45.79</td>
    <td align="right">26.33</td>
    <td align="right">38.30</td>
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
    <td align="right">7.39</td>
    <td align="right">8.48</td>
    <td align="right">8.48</td>
    <td align="right">8.48</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.10</td>
    <td align="right">18.34</td>
    <td align="right">18.34</td>
    <td align="right">18.34</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.08</td>
    <td align="right">18.87</td>
    <td align="right">18.86</td>
    <td align="right">18.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.93</td>
    <td align="right">14.12</td>
    <td align="right">14.11</td>
    <td align="right">14.12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">26.57</td>
    <td align="right">26.54</td>
    <td align="right">26.54</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.08</td>
    <td align="right">27.06</td>
    <td align="right">26.98</td>
    <td align="right">27.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.18</td>
    <td align="right">17.24</td>
    <td align="right">17.23</td>
    <td align="right">17.23</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">34.09</td>
    <td align="right">36.26</td>
    <td align="right">36.26</td>
    <td align="right">36.26</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.44</td>
    <td align="right">34.31</td>
    <td align="right">34.32</td>
    <td align="right">34.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.81</td>
    <td align="right">20.22</td>
    <td align="right">20.21</td>
    <td align="right">20.21</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.50</td>
    <td align="right">39.00</td>
    <td align="right">38.98</td>
    <td align="right">39.00</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.22</td>
    <td align="right">40.84</td>
    <td align="right">40.89</td>
    <td align="right">40.87</td>
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
    <td align="right">18.21</td>
    <td align="right">20.93</td>
    <td align="right">24.54</td>
    <td align="right">24.71</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.61</td>
    <td align="right">41.64</td>
    <td align="right">41.44</td>
    <td align="right">42.20</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">27.19</td>
    <td align="right">30.04</td>
    <td align="right">29.35</td>
    <td align="right">30.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.00</td>
    <td align="right">29.83</td>
    <td align="right">24.61</td>
    <td align="right">30.20</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.35</td>
    <td align="right">44.78</td>
    <td align="right">38.88</td>
    <td align="right">42.54</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.55</td>
    <td align="right">38.90</td>
    <td align="right">29.82</td>
    <td align="right">35.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.20</td>
    <td align="right">36.66</td>
    <td align="right">24.29</td>
    <td align="right">33.95</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">59.30</td>
    <td align="right">52.12</td>
    <td align="right">40.05</td>
    <td align="right">46.51</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.62</td>
    <td align="right">45.36</td>
    <td align="right">31.20</td>
    <td align="right">40.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.73</td>
    <td align="right">46.83</td>
    <td align="right">29.64</td>
    <td align="right">41.88</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">63.38</td>
    <td align="right">58.59</td>
    <td align="right">43.72</td>
    <td align="right">51.60</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.50</td>
    <td align="right">57.98</td>
    <td align="right">32.63</td>
    <td align="right">47.69</td>
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
    <td align="right">18.24</td>
    <td align="right">20.07</td>
    <td align="right">20.04</td>
    <td align="right">20.05</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">48.36</td>
    <td align="right">37.90</td>
    <td align="right">38.06</td>
    <td align="right">37.91</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.92</td>
    <td align="right">27.05</td>
    <td align="right">27.12</td>
    <td align="right">27.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">26.99</td>
    <td align="right">27.28</td>
    <td align="right">27.26</td>
    <td align="right">27.33</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.52</td>
    <td align="right">42.28</td>
    <td align="right">42.36</td>
    <td align="right">42.12</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.74</td>
    <td align="right">36.23</td>
    <td align="right">36.01</td>
    <td align="right">35.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.11</td>
    <td align="right">34.39</td>
    <td align="right">34.39</td>
    <td align="right">34.58</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.32</td>
    <td align="right">48.44</td>
    <td align="right">48.55</td>
    <td align="right">48.66</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.75</td>
    <td align="right">38.62</td>
    <td align="right">38.54</td>
    <td align="right">38.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.71</td>
    <td align="right">39.51</td>
    <td align="right">39.75</td>
    <td align="right">39.45</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.81</td>
    <td align="right">52.44</td>
    <td align="right">52.42</td>
    <td align="right">52.59</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.49</td>
    <td align="right">50.42</td>
    <td align="right">50.61</td>
    <td align="right">50.26</td>
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
    <td align="right">20.93</td>
    <td align="right">24.61</td>
    <td align="right">24.72</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.60</td>
    <td align="right">42.79</td>
    <td align="right">41.92</td>
    <td align="right">42.16</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">27.01</td>
    <td align="right">29.56</td>
    <td align="right">29.40</td>
    <td align="right">29.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">26.99</td>
    <td align="right">29.93</td>
    <td align="right">24.58</td>
    <td align="right">30.16</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">51.75</td>
    <td align="right">46.08</td>
    <td align="right">39.43</td>
    <td align="right">42.78</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.61</td>
    <td align="right">38.82</td>
    <td align="right">29.98</td>
    <td align="right">35.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.09</td>
    <td align="right">36.70</td>
    <td align="right">24.45</td>
    <td align="right">33.85</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">59.04</td>
    <td align="right">52.23</td>
    <td align="right">40.29</td>
    <td align="right">46.61</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.73</td>
    <td align="right">45.67</td>
    <td align="right">31.65</td>
    <td align="right">40.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.71</td>
    <td align="right">46.85</td>
    <td align="right">30.05</td>
    <td align="right">41.47</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.59</td>
    <td align="right">59.47</td>
    <td align="right">44.28</td>
    <td align="right">52.05</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">53.16</td>
    <td align="right">58.11</td>
    <td align="right">33.26</td>
    <td align="right">47.36</td>
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
    <td align="right">18.25</td>
    <td align="right">20.05</td>
    <td align="right">20.06</td>
    <td align="right">20.03</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.84</td>
    <td align="right">38.29</td>
    <td align="right">37.93</td>
    <td align="right">38.05</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">27.11</td>
    <td align="right">27.92</td>
    <td align="right">27.99</td>
    <td align="right">28.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">26.99</td>
    <td align="right">27.25</td>
    <td align="right">27.29</td>
    <td align="right">27.26</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.06</td>
    <td align="right">42.53</td>
    <td align="right">42.22</td>
    <td align="right">42.30</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.61</td>
    <td align="right">35.76</td>
    <td align="right">35.76</td>
    <td align="right">35.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.11</td>
    <td align="right">34.41</td>
    <td align="right">34.38</td>
    <td align="right">34.39</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.47</td>
    <td align="right">50.35</td>
    <td align="right">48.52</td>
    <td align="right">48.90</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.72</td>
    <td align="right">38.75</td>
    <td align="right">38.57</td>
    <td align="right">38.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.72</td>
    <td align="right">39.54</td>
    <td align="right">39.46</td>
    <td align="right">39.52</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.10</td>
    <td align="right">52.71</td>
    <td align="right">52.63</td>
    <td align="right">52.49</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.24</td>
    <td align="right">50.46</td>
    <td align="right">50.32</td>
    <td align="right">50.41</td>
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
    <td align="right">123.81</td>
    <td align="right">62.15</td>
    <td align="right">23.26</td>
    <td align="right">53.48</td>
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
    <td align="right">31.89</td>
    <td align="right">45.08</td>
    <td align="right">35.53</td>
    <td align="right">41.45</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.63</td>
    <td align="right">17.14</td>
    <td align="right">17.20</td>
    <td align="right">17.15</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">19.17</td>
    <td align="right">21.21</td>
    <td align="right">21.11</td>
    <td align="right">21.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">72.66</td>
    <td align="right">93.69</td>
    <td align="right">42.19</td>
    <td align="right">68.99</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.76</td>
    <td align="right">27.88</td>
    <td align="right">28.02</td>
    <td align="right">27.98</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.07</td>
    <td align="right">30.17</td>
    <td align="right">29.83</td>
    <td align="right">29.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">142.64</td>
    <td align="right">207.11</td>
    <td align="right">60.41</td>
    <td align="right">135.78</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">41.01</td>
    <td align="right">49.11</td>
    <td align="right">49.18</td>
    <td align="right">49.09</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">52.03</td>
    <td align="right">52.56</td>
    <td align="right">52.37</td>
    <td align="right">52.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">249.67</td>
    <td align="right">331.87</td>
    <td align="right">75.18</td>
    <td align="right">208.98</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.26</td>
    <td align="right">63.51</td>
    <td align="right">63.44</td>
    <td align="right">63.54</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.57</td>
    <td align="right">67.28</td>
    <td align="right">67.33</td>
    <td align="right">67.28</td>
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
    <td align="right">29.67</td>
    <td align="right">40.44</td>
    <td align="right">40.47</td>
    <td align="right">39.99</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.93</td>
    <td align="right">16.54</td>
    <td align="right">16.49</td>
    <td align="right">16.40</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">19.01</td>
    <td align="right">21.00</td>
    <td align="right">20.99</td>
    <td align="right">21.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">82.66</td>
    <td align="right">108.95</td>
    <td align="right">108.61</td>
    <td align="right">108.54</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.55</td>
    <td align="right">29.10</td>
    <td align="right">29.13</td>
    <td align="right">29.41</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">27.86</td>
    <td align="right">33.69</td>
    <td align="right">33.79</td>
    <td align="right">33.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">142.56</td>
    <td align="right">190.03</td>
    <td align="right">190.74</td>
    <td align="right">189.79</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.33</td>
    <td align="right">48.58</td>
    <td align="right">48.51</td>
    <td align="right">48.48</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.88</td>
    <td align="right">50.83</td>
    <td align="right">50.71</td>
    <td align="right">50.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">248.32</td>
    <td align="right">298.46</td>
    <td align="right">300.23</td>
    <td align="right">297.98</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.33</td>
    <td align="right">64.07</td>
    <td align="right">64.25</td>
    <td align="right">64.04</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.24</td>
    <td align="right">69.31</td>
    <td align="right">69.35</td>
    <td align="right">69.17</td>
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
    <td align="right">28.67</td>
    <td align="right">41.84</td>
    <td align="right">34.61</td>
    <td align="right">39.63</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.27</td>
    <td align="right">16.74</td>
    <td align="right">16.78</td>
    <td align="right">16.73</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.05</td>
    <td align="right">20.10</td>
    <td align="right">20.09</td>
    <td align="right">20.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">78.40</td>
    <td align="right">104.31</td>
    <td align="right">45.00</td>
    <td align="right">75.32</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.06</td>
    <td align="right">27.90</td>
    <td align="right">27.97</td>
    <td align="right">27.90</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">29.54</td>
    <td align="right">34.55</td>
    <td align="right">34.73</td>
    <td align="right">34.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">146.35</td>
    <td align="right">213.71</td>
    <td align="right">61.80</td>
    <td align="right">140.03</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">41.14</td>
    <td align="right">49.33</td>
    <td align="right">49.25</td>
    <td align="right">49.28</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">52.59</td>
    <td align="right">52.77</td>
    <td align="right">52.70</td>
    <td align="right">52.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">256.48</td>
    <td align="right">331.10</td>
    <td align="right">75.05</td>
    <td align="right">205.54</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">63.93</td>
    <td align="right">65.04</td>
    <td align="right">64.98</td>
    <td align="right">64.97</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">68.46</td>
    <td align="right">67.91</td>
    <td align="right">67.91</td>
    <td align="right">67.94</td>
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
    <td align="right">26.96</td>
    <td align="right">38.00</td>
    <td align="right">37.34</td>
    <td align="right">37.64</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.46</td>
    <td align="right">17.09</td>
    <td align="right">17.00</td>
    <td align="right">16.96</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">19.25</td>
    <td align="right">21.33</td>
    <td align="right">21.22</td>
    <td align="right">21.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">77.23</td>
    <td align="right">100.67</td>
    <td align="right">101.15</td>
    <td align="right">101.09</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.02</td>
    <td align="right">28.47</td>
    <td align="right">28.66</td>
    <td align="right">28.49</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.77</td>
    <td align="right">29.71</td>
    <td align="right">29.83</td>
    <td align="right">29.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">144.97</td>
    <td align="right">195.72</td>
    <td align="right">198.79</td>
    <td align="right">197.19</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.76</td>
    <td align="right">49.96</td>
    <td align="right">49.95</td>
    <td align="right">49.74</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">52.40</td>
    <td align="right">52.78</td>
    <td align="right">52.75</td>
    <td align="right">52.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">271.21</td>
    <td align="right">293.17</td>
    <td align="right">294.38</td>
    <td align="right">291.70</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.49</td>
    <td align="right">65.55</td>
    <td align="right">65.76</td>
    <td align="right">65.66</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.49</td>
    <td align="right">69.18</td>
    <td align="right">69.08</td>
    <td align="right">69.10</td>
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
    <td align="right">18.69</td>
    <td align="right">22.20</td>
    <td align="right">25.00</td>
    <td align="right">27.49</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.88</td>
    <td align="right">24.01</td>
    <td align="right">25.86</td>
    <td align="right">29.12</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">10.56</td>
    <td align="right">12.09</td>
    <td align="right">20.60</td>
    <td align="right">18.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.55</td>
    <td align="right">35.57</td>
    <td align="right">31.96</td>
    <td align="right">38.05</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.78</td>
    <td align="right">43.46</td>
    <td align="right">33.54</td>
    <td align="right">43.54</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">22.20</td>
    <td align="right">23.75</td>
    <td align="right">28.32</td>
    <td align="right">29.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.50</td>
    <td align="right">70.56</td>
    <td align="right">42.50</td>
    <td align="right">64.47</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.96</td>
    <td align="right">73.04</td>
    <td align="right">43.90</td>
    <td align="right">68.40</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.31</td>
    <td align="right">41.63</td>
    <td align="right">35.85</td>
    <td align="right">43.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.52</td>
    <td align="right">88.79</td>
    <td align="right">47.07</td>
    <td align="right">78.89</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">97.05</td>
    <td align="right">99.37</td>
    <td align="right">51.07</td>
    <td align="right">86.75</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.20</td>
    <td align="right">53.04</td>
    <td align="right">39.52</td>
    <td align="right">53.01</td>
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
    <td align="right">18.64</td>
    <td align="right">20.35</td>
    <td align="right">20.50</td>
    <td align="right">20.20</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.08</td>
    <td align="right">22.62</td>
    <td align="right">22.62</td>
    <td align="right">22.62</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">9.79</td>
    <td align="right">10.55</td>
    <td align="right">10.53</td>
    <td align="right">10.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.68</td>
    <td align="right">41.76</td>
    <td align="right">41.64</td>
    <td align="right">41.56</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.24</td>
    <td align="right">45.04</td>
    <td align="right">44.99</td>
    <td align="right">44.98</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">20.50</td>
    <td align="right">20.24</td>
    <td align="right">20.53</td>
    <td align="right">20.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.59</td>
    <td align="right">73.41</td>
    <td align="right">73.23</td>
    <td align="right">73.19</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.31</td>
    <td align="right">69.07</td>
    <td align="right">68.62</td>
    <td align="right">68.64</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">37.74</td>
    <td align="right">41.89</td>
    <td align="right">40.75</td>
    <td align="right">40.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.86</td>
    <td align="right">88.66</td>
    <td align="right">88.67</td>
    <td align="right">89.61</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.87</td>
    <td align="right">90.93</td>
    <td align="right">91.11</td>
    <td align="right">90.99</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.26</td>
    <td align="right">52.16</td>
    <td align="right">52.24</td>
    <td align="right">52.04</td>
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
    <td align="right">18.47</td>
    <td align="right">21.92</td>
    <td align="right">24.99</td>
    <td align="right">27.29</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.23</td>
    <td align="right">22.22</td>
    <td align="right">25.37</td>
    <td align="right">27.47</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">8.67</td>
    <td align="right">10.25</td>
    <td align="right">19.63</td>
    <td align="right">17.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.89</td>
    <td align="right">38.25</td>
    <td align="right">32.84</td>
    <td align="right">40.41</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">41.05</td>
    <td align="right">42.89</td>
    <td align="right">33.47</td>
    <td align="right">43.53</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">20.75</td>
    <td align="right">22.66</td>
    <td align="right">27.38</td>
    <td align="right">28.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.55</td>
    <td align="right">72.12</td>
    <td align="right">43.21</td>
    <td align="right">65.31</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.82</td>
    <td align="right">75.56</td>
    <td align="right">46.09</td>
    <td align="right">70.39</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.58</td>
    <td align="right">41.19</td>
    <td align="right">35.21</td>
    <td align="right">42.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.28</td>
    <td align="right">93.64</td>
    <td align="right">47.68</td>
    <td align="right">82.16</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.54</td>
    <td align="right">99.00</td>
    <td align="right">51.10</td>
    <td align="right">86.38</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.00</td>
    <td align="right">53.78</td>
    <td align="right">39.00</td>
    <td align="right">53.81</td>
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
    <td align="right">20.64</td>
    <td align="right">22.29</td>
    <td align="right">22.11</td>
    <td align="right">22.33</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">18.96</td>
    <td align="right">21.59</td>
    <td align="right">21.62</td>
    <td align="right">21.71</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">8.46</td>
    <td align="right">9.53</td>
    <td align="right">9.53</td>
    <td align="right">9.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.50</td>
    <td align="right">40.49</td>
    <td align="right">40.40</td>
    <td align="right">40.37</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.22</td>
    <td align="right">45.65</td>
    <td align="right">45.72</td>
    <td align="right">45.67</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">22.30</td>
    <td align="right">24.47</td>
    <td align="right">24.04</td>
    <td align="right">24.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.09</td>
    <td align="right">70.59</td>
    <td align="right">70.50</td>
    <td align="right">70.55</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">69.99</td>
    <td align="right">69.20</td>
    <td align="right">68.72</td>
    <td align="right">68.98</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.09</td>
    <td align="right">40.59</td>
    <td align="right">40.50</td>
    <td align="right">43.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.93</td>
    <td align="right">89.89</td>
    <td align="right">89.87</td>
    <td align="right">89.94</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.76</td>
    <td align="right">93.39</td>
    <td align="right">93.35</td>
    <td align="right">93.29</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.05</td>
    <td align="right">52.63</td>
    <td align="right">52.61</td>
    <td align="right">52.72</td>
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
    <td align="right">9.29</td>
    <td align="right">11.28</td>
    <td align="right">19.59</td>
    <td align="right">17.52</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.89</td>
    <td align="right">25.00</td>
    <td align="right">26.42</td>
    <td align="right">30.08</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.66</td>
    <td align="right">24.78</td>
    <td align="right">26.37</td>
    <td align="right">29.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">22.45</td>
    <td align="right">26.33</td>
    <td align="right">28.61</td>
    <td align="right">30.52</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.65</td>
    <td align="right">40.36</td>
    <td align="right">33.64</td>
    <td align="right">42.44</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.67</td>
    <td align="right">41.69</td>
    <td align="right">32.96</td>
    <td align="right">41.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.97</td>
    <td align="right">40.44</td>
    <td align="right">34.68</td>
    <td align="right">41.98</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.22</td>
    <td align="right">69.78</td>
    <td align="right">42.31</td>
    <td align="right">63.87</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.07</td>
    <td align="right">72.38</td>
    <td align="right">43.64</td>
    <td align="right">65.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.26</td>
    <td align="right">53.61</td>
    <td align="right">38.19</td>
    <td align="right">53.80</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.42</td>
    <td align="right">92.23</td>
    <td align="right">48.26</td>
    <td align="right">82.32</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.92</td>
    <td align="right">97.28</td>
    <td align="right">50.37</td>
    <td align="right">84.87</td>
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
    <td align="right">8.36</td>
    <td align="right">9.37</td>
    <td align="right">9.43</td>
    <td align="right">9.43</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.93</td>
    <td align="right">22.29</td>
    <td align="right">22.60</td>
    <td align="right">22.46</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.01</td>
    <td align="right">22.60</td>
    <td align="right">22.59</td>
    <td align="right">22.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.31</td>
    <td align="right">25.46</td>
    <td align="right">25.51</td>
    <td align="right">25.44</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.13</td>
    <td align="right">40.34</td>
    <td align="right">40.21</td>
    <td align="right">40.22</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.29</td>
    <td align="right">45.01</td>
    <td align="right">45.10</td>
    <td align="right">45.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.32</td>
    <td align="right">41.28</td>
    <td align="right">41.12</td>
    <td align="right">41.14</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.79</td>
    <td align="right">69.51</td>
    <td align="right">70.87</td>
    <td align="right">73.11</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.91</td>
    <td align="right">68.15</td>
    <td align="right">68.21</td>
    <td align="right">68.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.11</td>
    <td align="right">53.61</td>
    <td align="right">53.66</td>
    <td align="right">53.56</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.92</td>
    <td align="right">86.70</td>
    <td align="right">86.77</td>
    <td align="right">86.72</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.20</td>
    <td align="right">90.57</td>
    <td align="right">90.71</td>
    <td align="right">90.53</td>
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
    <td align="right">9.66</td>
    <td align="right">11.81</td>
    <td align="right">20.27</td>
    <td align="right">18.26</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.92</td>
    <td align="right">24.64</td>
    <td align="right">26.55</td>
    <td align="right">29.84</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.34</td>
    <td align="right">23.52</td>
    <td align="right">26.10</td>
    <td align="right">27.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.79</td>
    <td align="right">26.94</td>
    <td align="right">29.04</td>
    <td align="right">31.00</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.42</td>
    <td align="right">41.15</td>
    <td align="right">34.10</td>
    <td align="right">43.20</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">40.88</td>
    <td align="right">43.64</td>
    <td align="right">33.32</td>
    <td align="right">43.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.55</td>
    <td align="right">40.72</td>
    <td align="right">34.57</td>
    <td align="right">42.30</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.74</td>
    <td align="right">73.06</td>
    <td align="right">43.48</td>
    <td align="right">66.06</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.74</td>
    <td align="right">73.70</td>
    <td align="right">44.03</td>
    <td align="right">67.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.15</td>
    <td align="right">54.23</td>
    <td align="right">38.34</td>
    <td align="right">54.26</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.63</td>
    <td align="right">95.11</td>
    <td align="right">48.18</td>
    <td align="right">83.42</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.53</td>
    <td align="right">96.66</td>
    <td align="right">50.32</td>
    <td align="right">84.26</td>
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
    <td align="right">9.44</td>
    <td align="right">11.54</td>
    <td align="right">11.21</td>
    <td align="right">11.21</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">18.98</td>
    <td align="right">20.52</td>
    <td align="right">20.57</td>
    <td align="right">20.68</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.96</td>
    <td align="right">23.23</td>
    <td align="right">23.24</td>
    <td align="right">23.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.23</td>
    <td align="right">25.14</td>
    <td align="right">25.16</td>
    <td align="right">24.98</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.58</td>
    <td align="right">41.68</td>
    <td align="right">41.40</td>
    <td align="right">41.38</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">41.95</td>
    <td align="right">44.07</td>
    <td align="right">44.03</td>
    <td align="right">44.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.08</td>
    <td align="right">40.58</td>
    <td align="right">40.52</td>
    <td align="right">40.56</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">69.02</td>
    <td align="right">70.73</td>
    <td align="right">70.63</td>
    <td align="right">70.53</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.71</td>
    <td align="right">69.61</td>
    <td align="right">69.39</td>
    <td align="right">69.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.36</td>
    <td align="right">53.95</td>
    <td align="right">53.81</td>
    <td align="right">53.77</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.50</td>
    <td align="right">88.63</td>
    <td align="right">88.61</td>
    <td align="right">88.65</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.74</td>
    <td align="right">93.53</td>
    <td align="right">93.54</td>
    <td align="right">93.48</td>
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
    <td align="right">21.10</td>
    <td align="right">24.60</td>
    <td align="right">26.80</td>
    <td align="right">29.71</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">48.36</td>
    <td align="right">42.47</td>
    <td align="right">43.49</td>
    <td align="right">42.85</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">33.98</td>
    <td align="right">37.08</td>
    <td align="right">33.71</td>
    <td align="right">37.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.03</td>
    <td align="right">44.47</td>
    <td align="right">33.06</td>
    <td align="right">44.85</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">64.57</td>
    <td align="right">59.36</td>
    <td align="right">50.25</td>
    <td align="right">58.32</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">58.58</td>
    <td align="right">61.67</td>
    <td align="right">38.99</td>
    <td align="right">53.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.67</td>
    <td align="right">66.21</td>
    <td align="right">41.16</td>
    <td align="right">63.24</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">90.57</td>
    <td align="right">86.34</td>
    <td align="right">63.25</td>
    <td align="right">79.07</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.12</td>
    <td align="right">90.53</td>
    <td align="right">43.03</td>
    <td align="right">76.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.90</td>
    <td align="right">89.09</td>
    <td align="right">56.88</td>
    <td align="right">84.06</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.42</td>
    <td align="right">106.69</td>
    <td align="right">78.35</td>
    <td align="right">99.29</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.77</td>
    <td align="right">134.75</td>
    <td align="right">50.05</td>
    <td align="right">106.26</td>
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
    <td align="right">21.71</td>
    <td align="right">24.02</td>
    <td align="right">24.00</td>
    <td align="right">23.91</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">50.83</td>
    <td align="right">40.19</td>
    <td align="right">40.29</td>
    <td align="right">40.17</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">32.99</td>
    <td align="right">31.83</td>
    <td align="right">31.79</td>
    <td align="right">31.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.84</td>
    <td align="right">41.66</td>
    <td align="right">41.21</td>
    <td align="right">41.18</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">64.94</td>
    <td align="right">56.18</td>
    <td align="right">56.16</td>
    <td align="right">56.04</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">57.04</td>
    <td align="right">56.19</td>
    <td align="right">56.23</td>
    <td align="right">56.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.84</td>
    <td align="right">61.62</td>
    <td align="right">61.67</td>
    <td align="right">61.63</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">88.95</td>
    <td align="right">80.88</td>
    <td align="right">80.89</td>
    <td align="right">81.03</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">87.26</td>
    <td align="right">81.55</td>
    <td align="right">81.51</td>
    <td align="right">81.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.94</td>
    <td align="right">79.73</td>
    <td align="right">79.87</td>
    <td align="right">79.74</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">110.56</td>
    <td align="right">98.27</td>
    <td align="right">98.13</td>
    <td align="right">98.24</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.68</td>
    <td align="right">120.35</td>
    <td align="right">120.52</td>
    <td align="right">120.40</td>
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
    <td align="right">21.36</td>
    <td align="right">24.85</td>
    <td align="right">27.04</td>
    <td align="right">29.99</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">49.17</td>
    <td align="right">43.92</td>
    <td align="right">43.64</td>
    <td align="right">43.27</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">35.45</td>
    <td align="right">38.43</td>
    <td align="right">34.34</td>
    <td align="right">38.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.34</td>
    <td align="right">40.88</td>
    <td align="right">31.30</td>
    <td align="right">41.07</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">64.57</td>
    <td align="right">59.74</td>
    <td align="right">50.99</td>
    <td align="right">57.66</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">59.16</td>
    <td align="right">61.82</td>
    <td align="right">38.92</td>
    <td align="right">54.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.29</td>
    <td align="right">64.26</td>
    <td align="right">40.38</td>
    <td align="right">60.98</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">89.24</td>
    <td align="right">85.54</td>
    <td align="right">63.11</td>
    <td align="right">78.40</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">85.72</td>
    <td align="right">87.72</td>
    <td align="right">42.11</td>
    <td align="right">73.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.60</td>
    <td align="right">89.19</td>
    <td align="right">57.30</td>
    <td align="right">83.68</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.96</td>
    <td align="right">106.80</td>
    <td align="right">78.73</td>
    <td align="right">96.72</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">132.16</td>
    <td align="right">130.46</td>
    <td align="right">48.13</td>
    <td align="right">101.63</td>
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
    <td align="right">21.26</td>
    <td align="right">23.87</td>
    <td align="right">23.47</td>
    <td align="right">23.56</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">50.22</td>
    <td align="right">40.26</td>
    <td align="right">39.95</td>
    <td align="right">40.11</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">33.61</td>
    <td align="right">34.19</td>
    <td align="right">34.19</td>
    <td align="right">34.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.86</td>
    <td align="right">42.74</td>
    <td align="right">42.83</td>
    <td align="right">42.80</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">65.60</td>
    <td align="right">57.30</td>
    <td align="right">56.94</td>
    <td align="right">56.99</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">60.20</td>
    <td align="right">57.56</td>
    <td align="right">57.63</td>
    <td align="right">57.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.38</td>
    <td align="right">62.48</td>
    <td align="right">62.49</td>
    <td align="right">62.49</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">89.24</td>
    <td align="right">82.12</td>
    <td align="right">81.27</td>
    <td align="right">81.65</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">87.77</td>
    <td align="right">80.88</td>
    <td align="right">80.82</td>
    <td align="right">81.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.64</td>
    <td align="right">81.67</td>
    <td align="right">81.70</td>
    <td align="right">81.93</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.93</td>
    <td align="right">101.27</td>
    <td align="right">99.88</td>
    <td align="right">99.72</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">132.01</td>
    <td align="right">120.44</td>
    <td align="right">120.34</td>
    <td align="right">120.21</td>
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
    <td align="right">31.91</td>
    <td align="right">6.68</td>
    <td align="right">5.59</td>
    <td align="right">11.93</td>
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
    <td align="right">65.30</td>
    <td align="right">63.02</td>
    <td align="right">38.14</td>
    <td align="right">49.09</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.96</td>
    <td align="right">21.21</td>
    <td align="right">24.00</td>
    <td align="right">25.85</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.20</td>
    <td align="right">25.21</td>
    <td align="right">26.82</td>
    <td align="right">28.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">99.57</td>
    <td align="right">94.38</td>
    <td align="right">39.33</td>
    <td align="right">65.47</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.52</td>
    <td align="right">22.92</td>
    <td align="right">24.31</td>
    <td align="right">27.16</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.74</td>
    <td align="right">28.27</td>
    <td align="right">29.12</td>
    <td align="right">30.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">122.53</td>
    <td align="right">113.80</td>
    <td align="right">38.34</td>
    <td align="right">76.10</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.10</td>
    <td align="right">25.31</td>
    <td align="right">26.09</td>
    <td align="right">29.75</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">28.89</td>
    <td align="right">29.90</td>
    <td align="right">31.12</td>
    <td align="right">33.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">166.17</td>
    <td align="right">148.05</td>
    <td align="right">39.47</td>
    <td align="right">94.20</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.47</td>
    <td align="right">27.16</td>
    <td align="right">27.39</td>
    <td align="right">31.32</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">30.62</td>
    <td align="right">31.83</td>
    <td align="right">32.21</td>
    <td align="right">35.28</td>
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
    <td align="right">68.25</td>
    <td align="right">63.33</td>
    <td align="right">61.21</td>
    <td align="right">61.13</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.95</td>
    <td align="right">21.20</td>
    <td align="right">23.79</td>
    <td align="right">26.05</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.89</td>
    <td align="right">25.23</td>
    <td align="right">26.93</td>
    <td align="right">29.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">101.98</td>
    <td align="right">90.80</td>
    <td align="right">90.38</td>
    <td align="right">89.46</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.39</td>
    <td align="right">22.77</td>
    <td align="right">24.35</td>
    <td align="right">27.17</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.66</td>
    <td align="right">28.22</td>
    <td align="right">29.16</td>
    <td align="right">30.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">128.42</td>
    <td align="right">108.66</td>
    <td align="right">108.52</td>
    <td align="right">107.93</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.18</td>
    <td align="right">25.47</td>
    <td align="right">26.29</td>
    <td align="right">29.83</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.08</td>
    <td align="right">30.05</td>
    <td align="right">30.49</td>
    <td align="right">33.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">162.90</td>
    <td align="right">139.47</td>
    <td align="right">139.34</td>
    <td align="right">140.39</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.54</td>
    <td align="right">27.27</td>
    <td align="right">27.50</td>
    <td align="right">31.30</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">30.75</td>
    <td align="right">32.10</td>
    <td align="right">32.70</td>
    <td align="right">36.25</td>
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
    <td align="right">65.59</td>
    <td align="right">63.73</td>
    <td align="right">38.39</td>
    <td align="right">49.80</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">21.00</td>
    <td align="right">21.24</td>
    <td align="right">24.74</td>
    <td align="right">26.98</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.97</td>
    <td align="right">25.30</td>
    <td align="right">27.00</td>
    <td align="right">28.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">99.63</td>
    <td align="right">92.86</td>
    <td align="right">39.61</td>
    <td align="right">65.49</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.79</td>
    <td align="right">23.01</td>
    <td align="right">24.88</td>
    <td align="right">28.81</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.59</td>
    <td align="right">27.82</td>
    <td align="right">28.52</td>
    <td align="right">31.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">122.51</td>
    <td align="right">115.96</td>
    <td align="right">38.92</td>
    <td align="right">78.68</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.39</td>
    <td align="right">25.51</td>
    <td align="right">26.94</td>
    <td align="right">32.59</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.26</td>
    <td align="right">29.80</td>
    <td align="right">30.13</td>
    <td align="right">33.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">162.06</td>
    <td align="right">147.42</td>
    <td align="right">39.14</td>
    <td align="right">93.78</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.89</td>
    <td align="right">27.19</td>
    <td align="right">27.96</td>
    <td align="right">34.10</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.40</td>
    <td align="right">31.78</td>
    <td align="right">31.36</td>
    <td align="right">35.16</td>
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
    <td align="right">65.27</td>
    <td align="right">66.18</td>
    <td align="right">65.50</td>
    <td align="right">64.47</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">21.09</td>
    <td align="right">21.20</td>
    <td align="right">24.41</td>
    <td align="right">26.70</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.00</td>
    <td align="right">25.33</td>
    <td align="right">26.82</td>
    <td align="right">28.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">101.85</td>
    <td align="right">100.53</td>
    <td align="right">98.48</td>
    <td align="right">97.93</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.86</td>
    <td align="right">22.81</td>
    <td align="right">24.94</td>
    <td align="right">29.41</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.75</td>
    <td align="right">27.78</td>
    <td align="right">28.92</td>
    <td align="right">30.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">125.47</td>
    <td align="right">121.35</td>
    <td align="right">120.96</td>
    <td align="right">120.90</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.46</td>
    <td align="right">25.57</td>
    <td align="right">26.88</td>
    <td align="right">31.64</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.29</td>
    <td align="right">29.85</td>
    <td align="right">29.94</td>
    <td align="right">33.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">159.31</td>
    <td align="right">160.62</td>
    <td align="right">160.09</td>
    <td align="right">160.02</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">27.26</td>
    <td align="right">27.24</td>
    <td align="right">27.95</td>
    <td align="right">34.17</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.44</td>
    <td align="right">31.75</td>
    <td align="right">31.55</td>
    <td align="right">34.75</td>
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
    <td align="right">24.28</td>
    <td align="right">43.85</td>
    <td align="right">33.49</td>
    <td align="right">39.94</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.32</td>
    <td align="right">44.07</td>
    <td align="right">35.41</td>
    <td align="right">41.18</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.62</td>
    <td align="right">17.50</td>
    <td align="right">17.83</td>
    <td align="right">25.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.56</td>
    <td align="right">59.12</td>
    <td align="right">35.31</td>
    <td align="right">47.81</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.48</td>
    <td align="right">59.58</td>
    <td align="right">36.82</td>
    <td align="right">48.70</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.80</td>
    <td align="right">22.60</td>
    <td align="right">18.86</td>
    <td align="right">28.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">37.74</td>
    <td align="right">79.77</td>
    <td align="right">36.09</td>
    <td align="right">58.75</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.67</td>
    <td align="right">79.94</td>
    <td align="right">37.97</td>
    <td align="right">59.13</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.13</td>
    <td align="right">32.24</td>
    <td align="right">21.98</td>
    <td align="right">35.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.35</td>
    <td align="right">89.33</td>
    <td align="right">35.45</td>
    <td align="right">62.96</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.31</td>
    <td align="right">98.50</td>
    <td align="right">38.64</td>
    <td align="right">68.57</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.11</td>
    <td align="right">32.39</td>
    <td align="right">21.88</td>
    <td align="right">35.46</td>
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
    <td align="right">24.31</td>
    <td align="right">41.41</td>
    <td align="right">42.07</td>
    <td align="right">45.39</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.38</td>
    <td align="right">41.14</td>
    <td align="right">41.87</td>
    <td align="right">44.15</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.61</td>
    <td align="right">17.50</td>
    <td align="right">17.83</td>
    <td align="right">25.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.68</td>
    <td align="right">56.27</td>
    <td align="right">56.40</td>
    <td align="right">58.67</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.44</td>
    <td align="right">56.60</td>
    <td align="right">56.52</td>
    <td align="right">59.35</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.85</td>
    <td align="right">17.51</td>
    <td align="right">17.53</td>
    <td align="right">25.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">38.44</td>
    <td align="right">77.69</td>
    <td align="right">77.72</td>
    <td align="right">80.61</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.43</td>
    <td align="right">78.10</td>
    <td align="right">77.99</td>
    <td align="right">80.97</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.19</td>
    <td align="right">29.34</td>
    <td align="right">28.93</td>
    <td align="right">36.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.35</td>
    <td align="right">86.06</td>
    <td align="right">84.47</td>
    <td align="right">87.34</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">46.77</td>
    <td align="right">89.66</td>
    <td align="right">89.02</td>
    <td align="right">92.27</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.08</td>
    <td align="right">29.33</td>
    <td align="right">28.89</td>
    <td align="right">36.38</td>
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
    <td align="right">24.20</td>
    <td align="right">43.92</td>
    <td align="right">33.39</td>
    <td align="right">39.12</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.17</td>
    <td align="right">43.62</td>
    <td align="right">34.43</td>
    <td align="right">39.48</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.35</td>
    <td align="right">17.22</td>
    <td align="right">17.65</td>
    <td align="right">25.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.46</td>
    <td align="right">58.80</td>
    <td align="right">34.67</td>
    <td align="right">47.11</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.24</td>
    <td align="right">58.89</td>
    <td align="right">36.51</td>
    <td align="right">48.04</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.83</td>
    <td align="right">22.79</td>
    <td align="right">18.89</td>
    <td align="right">28.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">38.71</td>
    <td align="right">78.84</td>
    <td align="right">35.20</td>
    <td align="right">57.28</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.23</td>
    <td align="right">79.34</td>
    <td align="right">37.99</td>
    <td align="right">59.27</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.16</td>
    <td align="right">29.79</td>
    <td align="right">19.16</td>
    <td align="right">32.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.79</td>
    <td align="right">90.48</td>
    <td align="right">34.90</td>
    <td align="right">63.23</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.14</td>
    <td align="right">97.69</td>
    <td align="right">37.65</td>
    <td align="right">67.58</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.08</td>
    <td align="right">29.80</td>
    <td align="right">19.10</td>
    <td align="right">32.23</td>
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
    <td align="right">24.19</td>
    <td align="right">41.34</td>
    <td align="right">41.88</td>
    <td align="right">43.74</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.21</td>
    <td align="right">42.42</td>
    <td align="right">41.83</td>
    <td align="right">43.96</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.40</td>
    <td align="right">17.24</td>
    <td align="right">17.61</td>
    <td align="right">25.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.52</td>
    <td align="right">55.92</td>
    <td align="right">56.15</td>
    <td align="right">58.72</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.45</td>
    <td align="right">57.53</td>
    <td align="right">56.43</td>
    <td align="right">58.79</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.90</td>
    <td align="right">17.43</td>
    <td align="right">17.68</td>
    <td align="right">26.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">38.69</td>
    <td align="right">77.73</td>
    <td align="right">77.19</td>
    <td align="right">80.42</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.25</td>
    <td align="right">77.87</td>
    <td align="right">77.79</td>
    <td align="right">81.03</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.05</td>
    <td align="right">29.06</td>
    <td align="right">28.77</td>
    <td align="right">37.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.90</td>
    <td align="right">83.89</td>
    <td align="right">83.65</td>
    <td align="right">87.07</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.85</td>
    <td align="right">89.40</td>
    <td align="right">88.77</td>
    <td align="right">92.09</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.07</td>
    <td align="right">29.05</td>
    <td align="right">28.76</td>
    <td align="right">37.72</td>
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
    <td align="right">17.88</td>
    <td align="right">17.26</td>
    <td align="right">17.71</td>
    <td align="right">25.05</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.79</td>
    <td align="right">19.59</td>
    <td align="right">19.94</td>
    <td align="right">26.92</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.30</td>
    <td align="right">19.50</td>
    <td align="right">19.87</td>
    <td align="right">26.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.00</td>
    <td align="right">29.43</td>
    <td align="right">21.00</td>
    <td align="right">33.19</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.78</td>
    <td align="right">24.39</td>
    <td align="right">20.95</td>
    <td align="right">30.06</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.70</td>
    <td align="right">32.32</td>
    <td align="right">24.34</td>
    <td align="right">37.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.09</td>
    <td align="right">31.78</td>
    <td align="right">21.50</td>
    <td align="right">34.87</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.89</td>
    <td align="right">36.12</td>
    <td align="right">25.04</td>
    <td align="right">38.70</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.70</td>
    <td align="right">35.38</td>
    <td align="right">25.58</td>
    <td align="right">38.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.30</td>
    <td align="right">31.94</td>
    <td align="right">21.71</td>
    <td align="right">35.05</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.62</td>
    <td align="right">39.57</td>
    <td align="right">25.11</td>
    <td align="right">40.44</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.98</td>
    <td align="right">39.70</td>
    <td align="right">26.05</td>
    <td align="right">41.16</td>
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
    <td align="right">17.88</td>
    <td align="right">17.28</td>
    <td align="right">17.74</td>
    <td align="right">25.20</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.76</td>
    <td align="right">19.52</td>
    <td align="right">19.88</td>
    <td align="right">26.70</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.39</td>
    <td align="right">19.48</td>
    <td align="right">19.85</td>
    <td align="right">26.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.02</td>
    <td align="right">17.63</td>
    <td align="right">17.81</td>
    <td align="right">25.29</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.84</td>
    <td align="right">19.36</td>
    <td align="right">19.45</td>
    <td align="right">27.76</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.69</td>
    <td align="right">19.41</td>
    <td align="right">19.52</td>
    <td align="right">26.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.42</td>
    <td align="right">29.33</td>
    <td align="right">29.00</td>
    <td align="right">36.47</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.88</td>
    <td align="right">32.37</td>
    <td align="right">32.30</td>
    <td align="right">39.10</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.74</td>
    <td align="right">32.64</td>
    <td align="right">32.38</td>
    <td align="right">39.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.13</td>
    <td align="right">29.32</td>
    <td align="right">29.00</td>
    <td align="right">36.53</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.64</td>
    <td align="right">34.46</td>
    <td align="right">34.24</td>
    <td align="right">42.31</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.97</td>
    <td align="right">34.50</td>
    <td align="right">34.17</td>
    <td align="right">42.01</td>
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
    <td align="right">17.77</td>
    <td align="right">17.22</td>
    <td align="right">17.63</td>
    <td align="right">25.88</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.74</td>
    <td align="right">19.45</td>
    <td align="right">19.77</td>
    <td align="right">26.96</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.36</td>
    <td align="right">19.46</td>
    <td align="right">19.85</td>
    <td align="right">27.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.90</td>
    <td align="right">28.09</td>
    <td align="right">19.69</td>
    <td align="right">31.65</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.68</td>
    <td align="right">24.28</td>
    <td align="right">20.96</td>
    <td align="right">29.97</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.86</td>
    <td align="right">31.96</td>
    <td align="right">24.33</td>
    <td align="right">36.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.18</td>
    <td align="right">31.61</td>
    <td align="right">21.13</td>
    <td align="right">34.66</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.26</td>
    <td align="right">33.18</td>
    <td align="right">21.71</td>
    <td align="right">34.55</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.29</td>
    <td align="right">35.49</td>
    <td align="right">25.92</td>
    <td align="right">39.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.05</td>
    <td align="right">31.56</td>
    <td align="right">21.07</td>
    <td align="right">34.59</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.67</td>
    <td align="right">34.79</td>
    <td align="right">21.62</td>
    <td align="right">35.30</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.03</td>
    <td align="right">39.40</td>
    <td align="right">25.85</td>
    <td align="right">41.03</td>
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
    <td align="right">17.77</td>
    <td align="right">17.14</td>
    <td align="right">17.55</td>
    <td align="right">25.63</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.73</td>
    <td align="right">19.38</td>
    <td align="right">19.72</td>
    <td align="right">26.95</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.34</td>
    <td align="right">19.38</td>
    <td align="right">19.77</td>
    <td align="right">27.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.87</td>
    <td align="right">17.61</td>
    <td align="right">17.53</td>
    <td align="right">26.33</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.72</td>
    <td align="right">19.35</td>
    <td align="right">19.44</td>
    <td align="right">27.81</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.82</td>
    <td align="right">19.46</td>
    <td align="right">19.50</td>
    <td align="right">28.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.04</td>
    <td align="right">28.91</td>
    <td align="right">28.67</td>
    <td align="right">36.30</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.30</td>
    <td align="right">32.55</td>
    <td align="right">32.25</td>
    <td align="right">40.60</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.32</td>
    <td align="right">32.63</td>
    <td align="right">32.35</td>
    <td align="right">40.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.03</td>
    <td align="right">28.91</td>
    <td align="right">28.64</td>
    <td align="right">36.09</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.70</td>
    <td align="right">34.48</td>
    <td align="right">34.28</td>
    <td align="right">43.48</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.07</td>
    <td align="right">34.51</td>
    <td align="right">34.32</td>
    <td align="right">42.75</td>
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
    <td align="right">27.03</td>
    <td align="right">44.92</td>
    <td align="right">34.70</td>
    <td align="right">40.45</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.81</td>
    <td align="right">55.45</td>
    <td align="right">37.67</td>
    <td align="right">46.53</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.33</td>
    <td align="right">63.36</td>
    <td align="right">39.58</td>
    <td align="right">50.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.70</td>
    <td align="right">63.74</td>
    <td align="right">34.53</td>
    <td align="right">49.46</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.04</td>
    <td align="right">63.18</td>
    <td align="right">36.43</td>
    <td align="right">50.57</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.66</td>
    <td align="right">85.78</td>
    <td align="right">41.33</td>
    <td align="right">62.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.88</td>
    <td align="right">74.05</td>
    <td align="right">33.62</td>
    <td align="right">56.13</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">47.10</td>
    <td align="right">80.81</td>
    <td align="right">36.93</td>
    <td align="right">59.32</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">47.27</td>
    <td align="right">89.34</td>
    <td align="right">37.46</td>
    <td align="right">63.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.35</td>
    <td align="right">99.92</td>
    <td align="right">34.23</td>
    <td align="right">68.90</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.38</td>
    <td align="right">100.66</td>
    <td align="right">36.64</td>
    <td align="right">70.43</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">63.67</td>
    <td align="right">123.17</td>
    <td align="right">40.78</td>
    <td align="right">82.96</td>
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
    <td align="right">26.97</td>
    <td align="right">42.87</td>
    <td align="right">43.04</td>
    <td align="right">45.29</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.77</td>
    <td align="right">48.85</td>
    <td align="right">48.92</td>
    <td align="right">51.14</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.26</td>
    <td align="right">60.20</td>
    <td align="right">60.67</td>
    <td align="right">63.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.78</td>
    <td align="right">57.10</td>
    <td align="right">57.10</td>
    <td align="right">61.78</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.08</td>
    <td align="right">61.43</td>
    <td align="right">60.78</td>
    <td align="right">63.02</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.48</td>
    <td align="right">79.04</td>
    <td align="right">78.90</td>
    <td align="right">81.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.56</td>
    <td align="right">67.88</td>
    <td align="right">67.73</td>
    <td align="right">70.70</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">47.07</td>
    <td align="right">78.03</td>
    <td align="right">78.03</td>
    <td align="right">80.57</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">47.04</td>
    <td align="right">85.31</td>
    <td align="right">84.67</td>
    <td align="right">87.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.07</td>
    <td align="right">92.18</td>
    <td align="right">91.78</td>
    <td align="right">96.50</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.28</td>
    <td align="right">92.68</td>
    <td align="right">92.18</td>
    <td align="right">97.18</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">62.63</td>
    <td align="right">117.89</td>
    <td align="right">117.71</td>
    <td align="right">121.19</td>
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
    <td align="right">28.12</td>
    <td align="right">43.76</td>
    <td align="right">34.05</td>
    <td align="right">40.50</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.67</td>
    <td align="right">55.14</td>
    <td align="right">37.63</td>
    <td align="right">46.39</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">38.36</td>
    <td align="right">62.48</td>
    <td align="right">39.04</td>
    <td align="right">51.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">38.02</td>
    <td align="right">62.95</td>
    <td align="right">35.19</td>
    <td align="right">50.28</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.01</td>
    <td align="right">63.16</td>
    <td align="right">35.86</td>
    <td align="right">50.80</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">46.31</td>
    <td align="right">87.15</td>
    <td align="right">41.45</td>
    <td align="right">64.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">43.23</td>
    <td align="right">73.76</td>
    <td align="right">36.16</td>
    <td align="right">56.02</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.93</td>
    <td align="right">80.69</td>
    <td align="right">36.52</td>
    <td align="right">60.45</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">49.18</td>
    <td align="right">92.61</td>
    <td align="right">37.69</td>
    <td align="right">64.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">54.27</td>
    <td align="right">99.96</td>
    <td align="right">36.26</td>
    <td align="right">69.67</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.64</td>
    <td align="right">101.07</td>
    <td align="right">37.17</td>
    <td align="right">70.43</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">64.50</td>
    <td align="right">127.73</td>
    <td align="right">40.59</td>
    <td align="right">82.97</td>
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
    <td align="right">28.14</td>
    <td align="right">42.52</td>
    <td align="right">42.42</td>
    <td align="right">44.55</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.81</td>
    <td align="right">48.01</td>
    <td align="right">48.24</td>
    <td align="right">52.09</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">38.37</td>
    <td align="right">60.50</td>
    <td align="right">61.09</td>
    <td align="right">63.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">38.01</td>
    <td align="right">57.07</td>
    <td align="right">58.97</td>
    <td align="right">59.73</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.02</td>
    <td align="right">60.03</td>
    <td align="right">60.44</td>
    <td align="right">63.47</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">46.09</td>
    <td align="right">78.31</td>
    <td align="right">78.31</td>
    <td align="right">80.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">43.15</td>
    <td align="right">67.83</td>
    <td align="right">67.84</td>
    <td align="right">70.50</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.93</td>
    <td align="right">77.64</td>
    <td align="right">77.84</td>
    <td align="right">80.33</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">49.23</td>
    <td align="right">83.78</td>
    <td align="right">83.67</td>
    <td align="right">86.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">54.30</td>
    <td align="right">92.16</td>
    <td align="right">92.41</td>
    <td align="right">96.70</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.45</td>
    <td align="right">93.34</td>
    <td align="right">93.02</td>
    <td align="right">97.75</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">64.76</td>
    <td align="right">118.27</td>
    <td align="right">118.50</td>
    <td align="right">122.93</td>
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
    <td align="right">62.12</td>
    <td align="right">33.54</td>
    <td align="right">15.66</td>
    <td align="right">37.11</td>
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
    <td align="right">70.23</td>
    <td align="right">66.89</td>
    <td align="right">42.00</td>
    <td align="right">54.19</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.11</td>
    <td align="right">21.20</td>
    <td align="right">24.34</td>
    <td align="right">26.69</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.75</td>
    <td align="right">26.90</td>
    <td align="right">28.53</td>
    <td align="right">29.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">112.97</td>
    <td align="right">106.63</td>
    <td align="right">45.49</td>
    <td align="right">75.31</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.95</td>
    <td align="right">24.96</td>
    <td align="right">26.65</td>
    <td align="right">29.67</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">31.07</td>
    <td align="right">31.04</td>
    <td align="right">32.02</td>
    <td align="right">33.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">255.64</td>
    <td align="right">249.45</td>
    <td align="right">68.35</td>
    <td align="right">157.96</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">38.75</td>
    <td align="right">38.72</td>
    <td align="right">39.96</td>
    <td align="right">44.16</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.33</td>
    <td align="right">47.37</td>
    <td align="right">48.78</td>
    <td align="right">51.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">446.89</td>
    <td align="right">438.13</td>
    <td align="right">91.95</td>
    <td align="right">263.52</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.03</td>
    <td align="right">45.00</td>
    <td align="right">45.65</td>
    <td align="right">50.52</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">59.85</td>
    <td align="right">62.95</td>
    <td align="right">62.62</td>
    <td align="right">65.77</td>
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
    <td align="right">76.30</td>
    <td align="right">67.36</td>
    <td align="right">66.29</td>
    <td align="right">66.43</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.01</td>
    <td align="right">21.19</td>
    <td align="right">24.10</td>
    <td align="right">26.70</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.56</td>
    <td align="right">26.92</td>
    <td align="right">28.54</td>
    <td align="right">30.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">113.03</td>
    <td align="right">98.39</td>
    <td align="right">98.87</td>
    <td align="right">98.00</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.11</td>
    <td align="right">24.45</td>
    <td align="right">26.00</td>
    <td align="right">29.50</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">30.95</td>
    <td align="right">31.07</td>
    <td align="right">32.07</td>
    <td align="right">33.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">257.96</td>
    <td align="right">223.31</td>
    <td align="right">224.12</td>
    <td align="right">223.86</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.40</td>
    <td align="right">37.38</td>
    <td align="right">38.44</td>
    <td align="right">42.91</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.61</td>
    <td align="right">48.10</td>
    <td align="right">48.71</td>
    <td align="right">51.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">436.22</td>
    <td align="right">360.34</td>
    <td align="right">360.25</td>
    <td align="right">360.10</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.04</td>
    <td align="right">44.84</td>
    <td align="right">45.62</td>
    <td align="right">50.53</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.51</td>
    <td align="right">62.22</td>
    <td align="right">62.58</td>
    <td align="right">66.06</td>
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
    <td align="right">69.90</td>
    <td align="right">70.71</td>
    <td align="right">42.05</td>
    <td align="right">54.23</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.20</td>
    <td align="right">21.28</td>
    <td align="right">25.21</td>
    <td align="right">28.24</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.82</td>
    <td align="right">26.99</td>
    <td align="right">28.47</td>
    <td align="right">29.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">113.04</td>
    <td align="right">106.26</td>
    <td align="right">45.24</td>
    <td align="right">74.78</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.13</td>
    <td align="right">25.22</td>
    <td align="right">27.30</td>
    <td align="right">32.32</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">30.45</td>
    <td align="right">31.09</td>
    <td align="right">31.94</td>
    <td align="right">34.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">268.09</td>
    <td align="right">262.68</td>
    <td align="right">71.16</td>
    <td align="right">165.65</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">41.65</td>
    <td align="right">41.48</td>
    <td align="right">42.74</td>
    <td align="right">49.62</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.96</td>
    <td align="right">47.97</td>
    <td align="right">48.44</td>
    <td align="right">51.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">437.99</td>
    <td align="right">429.12</td>
    <td align="right">90.00</td>
    <td align="right">257.51</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">53.58</td>
    <td align="right">54.02</td>
    <td align="right">55.14</td>
    <td align="right">62.49</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.25</td>
    <td align="right">61.57</td>
    <td align="right">61.29</td>
    <td align="right">64.93</td>
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
    <td align="right">70.37</td>
    <td align="right">71.18</td>
    <td align="right">70.92</td>
    <td align="right">70.91</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.20</td>
    <td align="right">21.36</td>
    <td align="right">25.24</td>
    <td align="right">28.24</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.76</td>
    <td align="right">27.01</td>
    <td align="right">28.20</td>
    <td align="right">30.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">111.65</td>
    <td align="right">109.07</td>
    <td align="right">108.57</td>
    <td align="right">108.40</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.31</td>
    <td align="right">25.10</td>
    <td align="right">27.28</td>
    <td align="right">32.80</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">39.02</td>
    <td align="right">38.67</td>
    <td align="right">39.87</td>
    <td align="right">41.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">256.94</td>
    <td align="right">254.11</td>
    <td align="right">253.98</td>
    <td align="right">253.81</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">41.43</td>
    <td align="right">40.98</td>
    <td align="right">42.81</td>
    <td align="right">48.87</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.29</td>
    <td align="right">47.99</td>
    <td align="right">48.72</td>
    <td align="right">51.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">438.44</td>
    <td align="right">440.72</td>
    <td align="right">441.01</td>
    <td align="right">440.18</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">53.74</td>
    <td align="right">54.25</td>
    <td align="right">55.16</td>
    <td align="right">62.62</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.57</td>
    <td align="right">61.70</td>
    <td align="right">61.13</td>
    <td align="right">64.16</td>
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
    <td align="right">25.99</td>
    <td align="right">44.31</td>
    <td align="right">35.70</td>
    <td align="right">41.70</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.33</td>
    <td align="right">45.66</td>
    <td align="right">37.07</td>
    <td align="right">41.96</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.00</td>
    <td align="right">17.76</td>
    <td align="right">18.03</td>
    <td align="right">26.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">33.50</td>
    <td align="right">61.28</td>
    <td align="right">38.72</td>
    <td align="right">50.62</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">37.07</td>
    <td align="right">61.69</td>
    <td align="right">41.00</td>
    <td align="right">52.26</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">18.94</td>
    <td align="right">25.44</td>
    <td align="right">20.88</td>
    <td align="right">30.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">58.71</td>
    <td align="right">93.25</td>
    <td align="right">52.01</td>
    <td align="right">73.89</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">64.99</td>
    <td align="right">96.76</td>
    <td align="right">58.88</td>
    <td align="right">78.43</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">49.51</td>
    <td align="right">58.46</td>
    <td align="right">48.08</td>
    <td align="right">59.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">75.28</td>
    <td align="right">113.35</td>
    <td align="right">61.69</td>
    <td align="right">88.43</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.27</td>
    <td align="right">128.09</td>
    <td align="right">74.31</td>
    <td align="right">101.54</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">59.01</td>
    <td align="right">69.78</td>
    <td align="right">57.44</td>
    <td align="right">69.01</td>
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
    <td align="right">25.89</td>
    <td align="right">41.61</td>
    <td align="right">42.23</td>
    <td align="right">45.59</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.33</td>
    <td align="right">41.53</td>
    <td align="right">42.32</td>
    <td align="right">44.67</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.05</td>
    <td align="right">17.76</td>
    <td align="right">18.02</td>
    <td align="right">26.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">33.51</td>
    <td align="right">58.43</td>
    <td align="right">58.50</td>
    <td align="right">60.63</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">37.06</td>
    <td align="right">59.43</td>
    <td align="right">59.41</td>
    <td align="right">62.10</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">18.27</td>
    <td align="right">19.03</td>
    <td align="right">18.78</td>
    <td align="right">28.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">58.03</td>
    <td align="right">90.48</td>
    <td align="right">90.54</td>
    <td align="right">93.39</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">64.33</td>
    <td align="right">94.72</td>
    <td align="right">94.59</td>
    <td align="right">97.75</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">46.78</td>
    <td align="right">52.49</td>
    <td align="right">51.41</td>
    <td align="right">58.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">75.24</td>
    <td align="right">108.82</td>
    <td align="right">107.43</td>
    <td align="right">110.57</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">84.79</td>
    <td align="right">118.98</td>
    <td align="right">119.01</td>
    <td align="right">121.62</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.70</td>
    <td align="right">66.24</td>
    <td align="right">64.35</td>
    <td align="right">70.32</td>
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
    <td align="right">26.07</td>
    <td align="right">44.34</td>
    <td align="right">34.71</td>
    <td align="right">40.35</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.70</td>
    <td align="right">43.99</td>
    <td align="right">37.66</td>
    <td align="right">41.25</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">17.63</td>
    <td align="right">17.57</td>
    <td align="right">17.81</td>
    <td align="right">27.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">33.40</td>
    <td align="right">61.13</td>
    <td align="right">37.54</td>
    <td align="right">49.58</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">38.26</td>
    <td align="right">61.34</td>
    <td align="right">41.55</td>
    <td align="right">52.14</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">18.93</td>
    <td align="right">25.32</td>
    <td align="right">20.92</td>
    <td align="right">30.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">62.02</td>
    <td align="right">93.79</td>
    <td align="right">51.35</td>
    <td align="right">72.44</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">65.68</td>
    <td align="right">97.23</td>
    <td align="right">60.23</td>
    <td align="right">79.03</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">48.89</td>
    <td align="right">53.07</td>
    <td align="right">42.75</td>
    <td align="right">55.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">78.29</td>
    <td align="right">115.34</td>
    <td align="right">61.89</td>
    <td align="right">88.31</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.33</td>
    <td align="right">127.68</td>
    <td align="right">73.73</td>
    <td align="right">100.74</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">60.61</td>
    <td align="right">65.73</td>
    <td align="right">55.72</td>
    <td align="right">67.95</td>
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
    <td align="right">26.02</td>
    <td align="right">41.98</td>
    <td align="right">42.29</td>
    <td align="right">44.35</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.72</td>
    <td align="right">42.56</td>
    <td align="right">42.16</td>
    <td align="right">44.37</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">17.61</td>
    <td align="right">17.56</td>
    <td align="right">17.81</td>
    <td align="right">27.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">33.86</td>
    <td align="right">57.53</td>
    <td align="right">58.02</td>
    <td align="right">60.83</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">38.44</td>
    <td align="right">59.96</td>
    <td align="right">59.26</td>
    <td align="right">61.42</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">18.96</td>
    <td align="right">19.64</td>
    <td align="right">19.66</td>
    <td align="right">29.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">61.24</td>
    <td align="right">91.63</td>
    <td align="right">91.29</td>
    <td align="right">94.46</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">66.03</td>
    <td align="right">95.15</td>
    <td align="right">95.12</td>
    <td align="right">98.61</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">48.91</td>
    <td align="right">52.54</td>
    <td align="right">51.53</td>
    <td align="right">60.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">78.40</td>
    <td align="right">107.75</td>
    <td align="right">107.82</td>
    <td align="right">111.16</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.26</td>
    <td align="right">118.51</td>
    <td align="right">118.31</td>
    <td align="right">121.37</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">60.59</td>
    <td align="right">65.77</td>
    <td align="right">64.30</td>
    <td align="right">72.00</td>
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
    <td align="right">18.14</td>
    <td align="right">17.44</td>
    <td align="right">17.92</td>
    <td align="right">26.14</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">19.99</td>
    <td align="right">19.64</td>
    <td align="right">19.95</td>
    <td align="right">27.78</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.50</td>
    <td align="right">19.50</td>
    <td align="right">20.65</td>
    <td align="right">27.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.67</td>
    <td align="right">33.80</td>
    <td align="right">23.54</td>
    <td align="right">36.08</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">21.08</td>
    <td align="right">26.85</td>
    <td align="right">23.18</td>
    <td align="right">32.91</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">23.38</td>
    <td align="right">36.85</td>
    <td align="right">28.44</td>
    <td align="right">41.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.77</td>
    <td align="right">57.20</td>
    <td align="right">45.15</td>
    <td align="right">56.57</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.28</td>
    <td align="right">58.96</td>
    <td align="right">47.68</td>
    <td align="right">61.39</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.57</td>
    <td align="right">58.41</td>
    <td align="right">50.00</td>
    <td align="right">63.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.89</td>
    <td align="right">71.28</td>
    <td align="right">59.18</td>
    <td align="right">70.50</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.42</td>
    <td align="right">77.16</td>
    <td align="right">61.56</td>
    <td align="right">76.48</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">64.69</td>
    <td align="right">78.07</td>
    <td align="right">64.94</td>
    <td align="right">79.81</td>
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
    <td align="right">18.17</td>
    <td align="right">17.42</td>
    <td align="right">17.89</td>
    <td align="right">26.09</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">19.98</td>
    <td align="right">19.65</td>
    <td align="right">20.01</td>
    <td align="right">27.94</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.49</td>
    <td align="right">19.49</td>
    <td align="right">20.63</td>
    <td align="right">27.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.46</td>
    <td align="right">19.34</td>
    <td align="right">19.47</td>
    <td align="right">27.56</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">23.48</td>
    <td align="right">24.25</td>
    <td align="right">24.39</td>
    <td align="right">33.53</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">23.41</td>
    <td align="right">21.84</td>
    <td align="right">22.40</td>
    <td align="right">30.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.59</td>
    <td align="right">53.37</td>
    <td align="right">50.87</td>
    <td align="right">58.90</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.36</td>
    <td align="right">54.26</td>
    <td align="right">52.73</td>
    <td align="right">60.14</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.42</td>
    <td align="right">54.48</td>
    <td align="right">53.30</td>
    <td align="right">60.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">60.54</td>
    <td align="right">67.38</td>
    <td align="right">63.96</td>
    <td align="right">71.49</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.35</td>
    <td align="right">69.77</td>
    <td align="right">69.38</td>
    <td align="right">78.84</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">64.94</td>
    <td align="right">70.19</td>
    <td align="right">69.82</td>
    <td align="right">79.80</td>
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
    <td align="right">18.20</td>
    <td align="right">17.45</td>
    <td align="right">17.72</td>
    <td align="right">27.08</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">19.95</td>
    <td align="right">19.66</td>
    <td align="right">19.96</td>
    <td align="right">27.97</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.57</td>
    <td align="right">19.52</td>
    <td align="right">19.86</td>
    <td align="right">28.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">21.00</td>
    <td align="right">33.75</td>
    <td align="right">23.22</td>
    <td align="right">36.39</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">24.97</td>
    <td align="right">31.64</td>
    <td align="right">27.89</td>
    <td align="right">37.44</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">23.81</td>
    <td align="right">37.84</td>
    <td align="right">29.00</td>
    <td align="right">43.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.67</td>
    <td align="right">57.06</td>
    <td align="right">45.17</td>
    <td align="right">56.76</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">53.13</td>
    <td align="right">54.30</td>
    <td align="right">44.20</td>
    <td align="right">56.61</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.23</td>
    <td align="right">58.68</td>
    <td align="right">49.88</td>
    <td align="right">63.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.84</td>
    <td align="right">70.17</td>
    <td align="right">58.98</td>
    <td align="right">69.90</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">65.95</td>
    <td align="right">71.12</td>
    <td align="right">58.15</td>
    <td align="right">71.70</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">66.53</td>
    <td align="right">78.26</td>
    <td align="right">64.48</td>
    <td align="right">79.65</td>
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
    <td align="right">18.15</td>
    <td align="right">17.56</td>
    <td align="right">18.07</td>
    <td align="right">27.54</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">19.97</td>
    <td align="right">19.65</td>
    <td align="right">19.96</td>
    <td align="right">28.22</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.51</td>
    <td align="right">19.62</td>
    <td align="right">19.93</td>
    <td align="right">28.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.09</td>
    <td align="right">19.71</td>
    <td align="right">19.17</td>
    <td align="right">29.02</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">20.99</td>
    <td align="right">21.68</td>
    <td align="right">21.59</td>
    <td align="right">30.76</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">23.61</td>
    <td align="right">22.25</td>
    <td align="right">22.22</td>
    <td align="right">31.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.38</td>
    <td align="right">51.72</td>
    <td align="right">51.73</td>
    <td align="right">57.12</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">53.62</td>
    <td align="right">57.43</td>
    <td align="right">55.66</td>
    <td align="right">63.16</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.14</td>
    <td align="right">59.81</td>
    <td align="right">59.10</td>
    <td align="right">65.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.53</td>
    <td align="right">65.67</td>
    <td align="right">65.12</td>
    <td align="right">68.53</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">66.74</td>
    <td align="right">70.64</td>
    <td align="right">69.93</td>
    <td align="right">80.58</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">66.65</td>
    <td align="right">70.45</td>
    <td align="right">68.23</td>
    <td align="right">76.93</td>
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
    <td align="right">28.72</td>
    <td align="right">45.19</td>
    <td align="right">35.68</td>
    <td align="right">41.66</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.09</td>
    <td align="right">55.79</td>
    <td align="right">39.48</td>
    <td align="right">47.52</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">38.09</td>
    <td align="right">62.88</td>
    <td align="right">40.77</td>
    <td align="right">51.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">38.94</td>
    <td align="right">65.42</td>
    <td align="right">37.11</td>
    <td align="right">51.87</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">44.79</td>
    <td align="right">66.00</td>
    <td align="right">40.52</td>
    <td align="right">54.34</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">48.25</td>
    <td align="right">87.57</td>
    <td align="right">42.82</td>
    <td align="right">63.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">57.23</td>
    <td align="right">86.52</td>
    <td align="right">49.94</td>
    <td align="right">70.81</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">72.93</td>
    <td align="right">102.96</td>
    <td align="right">63.03</td>
    <td align="right">83.62</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">76.94</td>
    <td align="right">108.14</td>
    <td align="right">50.20</td>
    <td align="right">79.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">78.85</td>
    <td align="right">120.70</td>
    <td align="right">61.50</td>
    <td align="right">92.64</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">92.76</td>
    <td align="right">133.20</td>
    <td align="right">73.38</td>
    <td align="right">105.43</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">110.77</td>
    <td align="right">152.19</td>
    <td align="right">64.91</td>
    <td align="right">110.31</td>
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
    <td align="right">28.73</td>
    <td align="right">43.10</td>
    <td align="right">43.00</td>
    <td align="right">45.38</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.11</td>
    <td align="right">49.23</td>
    <td align="right">49.18</td>
    <td align="right">51.74</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">38.11</td>
    <td align="right">60.53</td>
    <td align="right">60.98</td>
    <td align="right">63.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">39.18</td>
    <td align="right">58.96</td>
    <td align="right">58.89</td>
    <td align="right">63.38</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">44.66</td>
    <td align="right">66.24</td>
    <td align="right">65.58</td>
    <td align="right">68.62</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">48.51</td>
    <td align="right">80.94</td>
    <td align="right">80.85</td>
    <td align="right">83.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">57.51</td>
    <td align="right">76.02</td>
    <td align="right">76.01</td>
    <td align="right">79.06</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">71.17</td>
    <td align="right">103.11</td>
    <td align="right">103.64</td>
    <td align="right">106.02</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">77.49</td>
    <td align="right">104.42</td>
    <td align="right">104.17</td>
    <td align="right">106.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">78.97</td>
    <td align="right">109.91</td>
    <td align="right">109.64</td>
    <td align="right">114.66</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">92.66</td>
    <td align="right">127.34</td>
    <td align="right">126.58</td>
    <td align="right">131.00</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">109.41</td>
    <td align="right">145.86</td>
    <td align="right">145.66</td>
    <td align="right">148.99</td>
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
    <td align="right">30.77</td>
    <td align="right">43.84</td>
    <td align="right">35.71</td>
    <td align="right">41.46</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.37</td>
    <td align="right">55.54</td>
    <td align="right">39.63</td>
    <td align="right">47.34</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">41.53</td>
    <td align="right">64.07</td>
    <td align="right">42.32</td>
    <td align="right">53.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.19</td>
    <td align="right">64.73</td>
    <td align="right">38.44</td>
    <td align="right">53.08</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">45.23</td>
    <td align="right">66.09</td>
    <td align="right">40.72</td>
    <td align="right">55.01</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">50.28</td>
    <td align="right">88.75</td>
    <td align="right">43.86</td>
    <td align="right">66.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">60.89</td>
    <td align="right">86.78</td>
    <td align="right">53.37</td>
    <td align="right">71.11</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">72.32</td>
    <td align="right">100.51</td>
    <td align="right">61.38</td>
    <td align="right">82.99</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">80.40</td>
    <td align="right">113.15</td>
    <td align="right">42.56</td>
    <td align="right">82.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.28</td>
    <td align="right">121.69</td>
    <td align="right">63.79</td>
    <td align="right">95.00</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">94.46</td>
    <td align="right">132.58</td>
    <td align="right">73.55</td>
    <td align="right">105.26</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">118.68</td>
    <td align="right">165.84</td>
    <td align="right">46.56</td>
    <td align="right">112.77</td>
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
    <td align="right">30.78</td>
    <td align="right">42.59</td>
    <td align="right">42.74</td>
    <td align="right">45.19</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.11</td>
    <td align="right">48.40</td>
    <td align="right">48.41</td>
    <td align="right">52.66</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">44.25</td>
    <td align="right">63.43</td>
    <td align="right">64.01</td>
    <td align="right">66.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.21</td>
    <td align="right">58.98</td>
    <td align="right">60.88</td>
    <td align="right">61.67</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">49.64</td>
    <td align="right">69.64</td>
    <td align="right">70.87</td>
    <td align="right">74.65</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">50.40</td>
    <td align="right">79.72</td>
    <td align="right">79.82</td>
    <td align="right">82.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">64.72</td>
    <td align="right">81.14</td>
    <td align="right">81.01</td>
    <td align="right">83.86</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">72.94</td>
    <td align="right">102.59</td>
    <td align="right">103.59</td>
    <td align="right">106.34</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.35</td>
    <td align="right">113.84</td>
    <td align="right">111.06</td>
    <td align="right">116.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.58</td>
    <td align="right">112.80</td>
    <td align="right">112.79</td>
    <td align="right">117.37</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">94.34</td>
    <td align="right">128.08</td>
    <td align="right">127.77</td>
    <td align="right">132.42</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">118.54</td>
    <td align="right">151.77</td>
    <td align="right">152.18</td>
    <td align="right">156.75</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
