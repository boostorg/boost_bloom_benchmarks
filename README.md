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
    <td align="right">38.61</td>
    <td align="right">6.18</td>
    <td align="right">4.28</td>
    <td align="right">13.07</td>
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
    <td align="right">12.21</td>
    <td align="right">18.18</td>
    <td align="right">17.03</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.91</td>
    <td align="right">4.49</td>
    <td align="right">4.50</td>
    <td align="right">4.50</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.46</td>
    <td align="right">5.11</td>
    <td align="right">5.11</td>
    <td align="right">5.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.51</td>
    <td align="right">17.88</td>
    <td align="right">19.15</td>
    <td align="right">20.55</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.38</td>
    <td align="right">5.16</td>
    <td align="right">5.16</td>
    <td align="right">5.16</td>
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
    <td align="right">20.28</td>
    <td align="right">21.49</td>
    <td align="right">18.18</td>
    <td align="right">23.21</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.01</td>
    <td align="right">5.62</td>
    <td align="right">5.62</td>
    <td align="right">5.61</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.53</td>
    <td align="right">6.01</td>
    <td align="right">6.01</td>
    <td align="right">6.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.27</td>
    <td align="right">27.59</td>
    <td align="right">18.50</td>
    <td align="right">27.56</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.40</td>
    <td align="right">5.98</td>
    <td align="right">5.99</td>
    <td align="right">5.99</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.81</td>
    <td align="right">6.30</td>
    <td align="right">6.31</td>
    <td align="right">6.30</td>
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
    <td align="right">11.03</td>
    <td align="right">13.14</td>
    <td align="right">13.15</td>
    <td align="right">13.17</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.48</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.96</td>
    <td align="right">5.08</td>
    <td align="right">5.07</td>
    <td align="right">5.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.72</td>
    <td align="right">20.21</td>
    <td align="right">20.19</td>
    <td align="right">20.18</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.36</td>
    <td align="right">5.14</td>
    <td align="right">5.15</td>
    <td align="right">5.14</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.01</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.36</td>
    <td align="right">24.41</td>
    <td align="right">24.38</td>
    <td align="right">24.33</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.02</td>
    <td align="right">5.63</td>
    <td align="right">5.64</td>
    <td align="right">5.64</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.55</td>
    <td align="right">6.03</td>
    <td align="right">6.04</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.32</td>
    <td align="right">29.24</td>
    <td align="right">29.28</td>
    <td align="right">29.28</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.41</td>
    <td align="right">6.00</td>
    <td align="right">6.00</td>
    <td align="right">6.00</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.83</td>
    <td align="right">6.30</td>
    <td align="right">6.31</td>
    <td align="right">6.30</td>
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
    <td align="right">10.01</td>
    <td align="right">11.95</td>
    <td align="right">19.29</td>
    <td align="right">16.14</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.97</td>
    <td align="right">4.42</td>
    <td align="right">4.42</td>
    <td align="right">4.42</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.93</td>
    <td align="right">4.87</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">14.96</td>
    <td align="right">17.71</td>
    <td align="right">20.70</td>
    <td align="right">21.08</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.36</td>
    <td align="right">4.98</td>
    <td align="right">4.97</td>
    <td align="right">4.97</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.06</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
    <td align="right">5.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">17.64</td>
    <td align="right">21.70</td>
    <td align="right">19.93</td>
    <td align="right">23.02</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.99</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="right">5.30</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.52</td>
    <td align="right">5.91</td>
    <td align="right">5.92</td>
    <td align="right">5.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">21.49</td>
    <td align="right">27.25</td>
    <td align="right">20.36</td>
    <td align="right">27.63</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.37</td>
    <td align="right">5.93</td>
    <td align="right">5.94</td>
    <td align="right">5.94</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.94</td>
    <td align="right">6.19</td>
    <td align="right">6.19</td>
    <td align="right">6.17</td>
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
    <td align="right">9.95</td>
    <td align="right">13.37</td>
    <td align="right">13.35</td>
    <td align="right">13.38</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.98</td>
    <td align="right">4.42</td>
    <td align="right">4.43</td>
    <td align="right">4.41</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.43</td>
    <td align="right">4.85</td>
    <td align="right">4.85</td>
    <td align="right">4.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">14.89</td>
    <td align="right">20.57</td>
    <td align="right">20.56</td>
    <td align="right">20.47</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.35</td>
    <td align="right">4.96</td>
    <td align="right">4.96</td>
    <td align="right">4.96</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.06</td>
    <td align="right">5.25</td>
    <td align="right">5.26</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">17.86</td>
    <td align="right">25.72</td>
    <td align="right">25.69</td>
    <td align="right">25.95</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.99</td>
    <td align="right">5.30</td>
    <td align="right">5.29</td>
    <td align="right">5.30</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.52</td>
    <td align="right">5.90</td>
    <td align="right">5.90</td>
    <td align="right">5.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">21.86</td>
    <td align="right">32.41</td>
    <td align="right">32.31</td>
    <td align="right">32.37</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.38</td>
    <td align="right">5.94</td>
    <td align="right">5.95</td>
    <td align="right">5.95</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.94</td>
    <td align="right">6.19</td>
    <td align="right">6.19</td>
    <td align="right">6.19</td>
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
    <td align="right">5.03</td>
    <td align="right">5.82</td>
    <td align="right">14.07</td>
    <td align="right">11.79</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.50</td>
    <td align="right">7.64</td>
    <td align="right">14.79</td>
    <td align="right">13.22</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.23</td>
    <td align="right">2.95</td>
    <td align="right">2.95</td>
    <td align="right">2.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.86</td>
    <td align="right">8.47</td>
    <td align="right">14.77</td>
    <td align="right">13.62</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.03</td>
    <td align="right">9.64</td>
    <td align="right">16.32</td>
    <td align="right">15.27</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.70</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.15</td>
    <td align="right">12.36</td>
    <td align="right">16.11</td>
    <td align="right">17.61</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.14</td>
    <td align="right">13.08</td>
    <td align="right">17.79</td>
    <td align="right">17.89</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.84</td>
    <td align="right">5.86</td>
    <td align="right">4.19</td>
    <td align="right">14.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.37</td>
    <td align="right">13.54</td>
    <td align="right">15.48</td>
    <td align="right">18.53</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.61</td>
    <td align="right">14.85</td>
    <td align="right">18.65</td>
    <td align="right">19.88</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.84</td>
    <td align="right">5.89</td>
    <td align="right">4.18</td>
    <td align="right">14.75</td>
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
    <td align="right">5.66</td>
    <td align="right">5.66</td>
    <td align="right">5.66</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.49</td>
    <td align="right">6.97</td>
    <td align="right">6.98</td>
    <td align="right">7.00</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.24</td>
    <td align="right">2.96</td>
    <td align="right">2.96</td>
    <td align="right">2.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.88</td>
    <td align="right">9.28</td>
    <td align="right">9.28</td>
    <td align="right">9.28</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.06</td>
    <td align="right">9.70</td>
    <td align="right">9.69</td>
    <td align="right">9.69</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.70</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.30</td>
    <td align="right">11.79</td>
    <td align="right">11.78</td>
    <td align="right">11.79</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.08</td>
    <td align="right">13.67</td>
    <td align="right">13.66</td>
    <td align="right">13.67</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.79</td>
    <td align="right">5.85</td>
    <td align="right">5.85</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.37</td>
    <td align="right">12.71</td>
    <td align="right">12.72</td>
    <td align="right">12.72</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.63</td>
    <td align="right">15.10</td>
    <td align="right">15.12</td>
    <td align="right">15.09</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.82</td>
    <td align="right">5.88</td>
    <td align="right">5.88</td>
    <td align="right">5.89</td>
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
    <td align="right">4.69</td>
    <td align="right">5.76</td>
    <td align="right">13.94</td>
    <td align="right">11.59</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.48</td>
    <td align="right">7.42</td>
    <td align="right">14.48</td>
    <td align="right">14.37</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.93</td>
    <td align="right">3.03</td>
    <td align="right">3.03</td>
    <td align="right">3.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.11</td>
    <td align="right">8.54</td>
    <td align="right">14.77</td>
    <td align="right">13.57</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">6.83</td>
    <td align="right">9.52</td>
    <td align="right">16.25</td>
    <td align="right">15.18</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.56</td>
    <td align="right">2.91</td>
    <td align="right">2.91</td>
    <td align="right">2.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">8.58</td>
    <td align="right">12.21</td>
    <td align="right">15.98</td>
    <td align="right">16.88</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.15</td>
    <td align="right">12.75</td>
    <td align="right">17.16</td>
    <td align="right">17.38</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.25</td>
    <td align="right">5.78</td>
    <td align="right">3.85</td>
    <td align="right">14.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.11</td>
    <td align="right">13.77</td>
    <td align="right">15.46</td>
    <td align="right">18.34</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.49</td>
    <td align="right">14.64</td>
    <td align="right">18.26</td>
    <td align="right">18.99</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.30</td>
    <td align="right">5.82</td>
    <td align="right">3.84</td>
    <td align="right">14.68</td>
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
    <td align="right">4.68</td>
    <td align="right">5.57</td>
    <td align="right">5.57</td>
    <td align="right">5.57</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.48</td>
    <td align="right">6.81</td>
    <td align="right">6.81</td>
    <td align="right">6.81</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.94</td>
    <td align="right">3.04</td>
    <td align="right">3.04</td>
    <td align="right">3.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.10</td>
    <td align="right">9.24</td>
    <td align="right">9.24</td>
    <td align="right">9.23</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">6.81</td>
    <td align="right">9.57</td>
    <td align="right">9.57</td>
    <td align="right">9.57</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.56</td>
    <td align="right">2.91</td>
    <td align="right">2.91</td>
    <td align="right">2.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">8.56</td>
    <td align="right">10.90</td>
    <td align="right">10.90</td>
    <td align="right">10.90</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.16</td>
    <td align="right">11.82</td>
    <td align="right">11.81</td>
    <td align="right">11.82</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.25</td>
    <td align="right">5.60</td>
    <td align="right">5.62</td>
    <td align="right">5.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.08</td>
    <td align="right">12.39</td>
    <td align="right">12.39</td>
    <td align="right">12.39</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.53</td>
    <td align="right">14.63</td>
    <td align="right">14.62</td>
    <td align="right">14.61</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.35</td>
    <td align="right">5.63</td>
    <td align="right">5.63</td>
    <td align="right">5.62</td>
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
    <td align="right">3.18</td>
    <td align="right">2.78</td>
    <td align="right">2.77</td>
    <td align="right">2.78</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.64</td>
    <td align="right">4.80</td>
    <td align="right">4.80</td>
    <td align="right">4.80</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.78</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.35</td>
    <td align="right">2.85</td>
    <td align="right">2.86</td>
    <td align="right">2.84</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.47</td>
    <td align="right">4.17</td>
    <td align="right">4.18</td>
    <td align="right">4.16</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.79</td>
    <td align="right">4.71</td>
    <td align="right">4.72</td>
    <td align="right">4.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.55</td>
    <td align="right">5.66</td>
    <td align="right">3.92</td>
    <td align="right">14.33</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.62</td>
    <td align="right">8.21</td>
    <td align="right">6.19</td>
    <td align="right">17.90</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.78</td>
    <td align="right">7.99</td>
    <td align="right">6.16</td>
    <td align="right">17.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.61</td>
    <td align="right">5.69</td>
    <td align="right">3.89</td>
    <td align="right">14.39</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.49</td>
    <td align="right">9.36</td>
    <td align="right">6.29</td>
    <td align="right">18.61</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.57</td>
    <td align="right">9.16</td>
    <td align="right">6.20</td>
    <td align="right">18.31</td>
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
    <td align="right">2.77</td>
    <td align="right">2.77</td>
    <td align="right">2.78</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.65</td>
    <td align="right">4.58</td>
    <td align="right">4.58</td>
    <td align="right">4.56</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.81</td>
    <td align="right">4.41</td>
    <td align="right">4.41</td>
    <td align="right">4.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.31</td>
    <td align="right">2.84</td>
    <td align="right">2.84</td>
    <td align="right">2.83</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.50</td>
    <td align="right">4.18</td>
    <td align="right">4.19</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.80</td>
    <td align="right">4.50</td>
    <td align="right">4.50</td>
    <td align="right">4.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.55</td>
    <td align="right">5.64</td>
    <td align="right">5.63</td>
    <td align="right">5.63</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.57</td>
    <td align="right">7.81</td>
    <td align="right">7.82</td>
    <td align="right">7.82</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.75</td>
    <td align="right">7.68</td>
    <td align="right">7.69</td>
    <td align="right">7.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.63</td>
    <td align="right">5.68</td>
    <td align="right">5.67</td>
    <td align="right">5.67</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.47</td>
    <td align="right">8.65</td>
    <td align="right">8.69</td>
    <td align="right">8.70</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.63</td>
    <td align="right">8.36</td>
    <td align="right">8.07</td>
    <td align="right">8.28</td>
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
    <td align="right">2.85</td>
    <td align="right">2.85</td>
    <td align="right">2.85</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.44</td>
    <td align="right">4.61</td>
    <td align="right">4.64</td>
    <td align="right">4.64</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.66</td>
    <td align="right">4.45</td>
    <td align="right">4.45</td>
    <td align="right">4.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.03</td>
    <td align="right">2.90</td>
    <td align="right">2.90</td>
    <td align="right">2.90</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.46</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
    <td align="right">4.07</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.60</td>
    <td align="right">4.55</td>
    <td align="right">4.55</td>
    <td align="right">4.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.46</td>
    <td align="right">5.48</td>
    <td align="right">3.68</td>
    <td align="right">14.16</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.30</td>
    <td align="right">7.94</td>
    <td align="right">5.89</td>
    <td align="right">17.77</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.49</td>
    <td align="right">7.83</td>
    <td align="right">5.87</td>
    <td align="right">17.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.51</td>
    <td align="right">5.52</td>
    <td align="right">3.67</td>
    <td align="right">14.22</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.95</td>
    <td align="right">9.18</td>
    <td align="right">5.93</td>
    <td align="right">18.64</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.71</td>
    <td align="right">8.98</td>
    <td align="right">5.93</td>
    <td align="right">18.07</td>
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
    <td align="right">2.94</td>
    <td align="right">2.84</td>
    <td align="right">2.86</td>
    <td align="right">2.86</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.46</td>
    <td align="right">4.43</td>
    <td align="right">4.43</td>
    <td align="right">4.43</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.67</td>
    <td align="right">4.26</td>
    <td align="right">4.26</td>
    <td align="right">4.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.03</td>
    <td align="right">2.90</td>
    <td align="right">2.90</td>
    <td align="right">2.90</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.44</td>
    <td align="right">4.07</td>
    <td align="right">4.08</td>
    <td align="right">4.06</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.58</td>
    <td align="right">4.36</td>
    <td align="right">4.36</td>
    <td align="right">4.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.45</td>
    <td align="right">5.40</td>
    <td align="right">5.41</td>
    <td align="right">5.41</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.36</td>
    <td align="right">7.56</td>
    <td align="right">7.54</td>
    <td align="right">7.56</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.37</td>
    <td align="right">7.26</td>
    <td align="right">7.25</td>
    <td align="right">7.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.52</td>
    <td align="right">5.46</td>
    <td align="right">5.45</td>
    <td align="right">5.43</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.93</td>
    <td align="right">8.35</td>
    <td align="right">8.38</td>
    <td align="right">8.38</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.68</td>
    <td align="right">8.23</td>
    <td align="right">8.22</td>
    <td align="right">8.26</td>
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
    <td align="right">6.44</td>
    <td align="right">7.35</td>
    <td align="right">14.44</td>
    <td align="right">12.70</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.74</td>
    <td align="right">8.79</td>
    <td align="right">18.85</td>
    <td align="right">15.76</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.14</td>
    <td align="right">11.50</td>
    <td align="right">19.42</td>
    <td align="right">16.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.78</td>
    <td align="right">10.40</td>
    <td align="right">14.38</td>
    <td align="right">15.80</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.54</td>
    <td align="right">10.53</td>
    <td align="right">16.20</td>
    <td align="right">17.23</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.96</td>
    <td align="right">14.24</td>
    <td align="right">20.48</td>
    <td align="right">20.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.65</td>
    <td align="right">11.92</td>
    <td align="right">14.01</td>
    <td align="right">16.79</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.98</td>
    <td align="right">12.95</td>
    <td align="right">17.34</td>
    <td align="right">19.76</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.26</td>
    <td align="right">14.74</td>
    <td align="right">19.04</td>
    <td align="right">20.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.87</td>
    <td align="right">14.38</td>
    <td align="right">14.81</td>
    <td align="right">18.51</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.65</td>
    <td align="right">15.19</td>
    <td align="right">16.96</td>
    <td align="right">20.10</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.95</td>
    <td align="right">20.82</td>
    <td align="right">21.25</td>
    <td align="right">23.26</td>
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
    <td align="right">6.44</td>
    <td align="right">6.93</td>
    <td align="right">6.93</td>
    <td align="right">6.92</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.77</td>
    <td align="right">8.40</td>
    <td align="right">8.41</td>
    <td align="right">8.41</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.27</td>
    <td align="right">11.22</td>
    <td align="right">11.22</td>
    <td align="right">11.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.79</td>
    <td align="right">9.92</td>
    <td align="right">9.92</td>
    <td align="right">9.92</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.53</td>
    <td align="right">10.92</td>
    <td align="right">10.92</td>
    <td align="right">10.92</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.04</td>
    <td align="right">14.32</td>
    <td align="right">14.33</td>
    <td align="right">14.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.65</td>
    <td align="right">11.05</td>
    <td align="right">11.04</td>
    <td align="right">11.05</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.98</td>
    <td align="right">13.14</td>
    <td align="right">13.15</td>
    <td align="right">13.14</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.32</td>
    <td align="right">16.35</td>
    <td align="right">16.32</td>
    <td align="right">16.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.87</td>
    <td align="right">14.18</td>
    <td align="right">14.19</td>
    <td align="right">14.18</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.65</td>
    <td align="right">16.01</td>
    <td align="right">16.01</td>
    <td align="right">16.01</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.76</td>
    <td align="right">21.13</td>
    <td align="right">21.23</td>
    <td align="right">21.18</td>
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
    <td align="right">6.41</td>
    <td align="right">7.34</td>
    <td align="right">14.51</td>
    <td align="right">13.05</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.24</td>
    <td align="right">8.76</td>
    <td align="right">18.55</td>
    <td align="right">15.69</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.15</td>
    <td align="right">10.83</td>
    <td align="right">18.93</td>
    <td align="right">15.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.10</td>
    <td align="right">10.48</td>
    <td align="right">14.32</td>
    <td align="right">15.65</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.62</td>
    <td align="right">10.50</td>
    <td align="right">15.91</td>
    <td align="right">17.20</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.78</td>
    <td align="right">14.47</td>
    <td align="right">19.40</td>
    <td align="right">18.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.10</td>
    <td align="right">12.00</td>
    <td align="right">13.98</td>
    <td align="right">17.01</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.36</td>
    <td align="right">12.95</td>
    <td align="right">16.89</td>
    <td align="right">20.03</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.17</td>
    <td align="right">15.58</td>
    <td align="right">16.96</td>
    <td align="right">19.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.27</td>
    <td align="right">14.54</td>
    <td align="right">14.84</td>
    <td align="right">18.30</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.64</td>
    <td align="right">15.39</td>
    <td align="right">16.53</td>
    <td align="right">20.21</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.41</td>
    <td align="right">21.75</td>
    <td align="right">17.96</td>
    <td align="right">23.01</td>
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
    <td align="right">6.42</td>
    <td align="right">6.94</td>
    <td align="right">6.94</td>
    <td align="right">6.92</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.22</td>
    <td align="right">8.33</td>
    <td align="right">8.34</td>
    <td align="right">8.33</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.17</td>
    <td align="right">10.94</td>
    <td align="right">10.93</td>
    <td align="right">10.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.10</td>
    <td align="right">10.05</td>
    <td align="right">10.03</td>
    <td align="right">10.04</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.65</td>
    <td align="right">10.88</td>
    <td align="right">10.89</td>
    <td align="right">10.88</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.64</td>
    <td align="right">13.54</td>
    <td align="right">13.54</td>
    <td align="right">13.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.09</td>
    <td align="right">11.16</td>
    <td align="right">11.16</td>
    <td align="right">11.17</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.35</td>
    <td align="right">13.18</td>
    <td align="right">13.18</td>
    <td align="right">13.17</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.20</td>
    <td align="right">15.92</td>
    <td align="right">15.77</td>
    <td align="right">15.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.27</td>
    <td align="right">14.43</td>
    <td align="right">14.43</td>
    <td align="right">14.43</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.64</td>
    <td align="right">16.06</td>
    <td align="right">16.06</td>
    <td align="right">16.05</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.06</td>
    <td align="right">19.85</td>
    <td align="right">19.81</td>
    <td align="right">19.79</td>
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
    <td align="right">58.32</td>
    <td align="right">23.30</td>
    <td align="right">14.52</td>
    <td align="right">31.80</td>
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
    <td align="right">17.52</td>
    <td align="right">19.56</td>
    <td align="right">21.59</td>
    <td align="right">21.83</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.65</td>
    <td align="right">6.34</td>
    <td align="right">6.38</td>
    <td align="right">6.37</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.12</td>
    <td align="right">6.80</td>
    <td align="right">6.81</td>
    <td align="right">6.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">50.71</td>
    <td align="right">55.67</td>
    <td align="right">28.28</td>
    <td align="right">43.21</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.57</td>
    <td align="right">11.58</td>
    <td align="right">11.56</td>
    <td align="right">11.56</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.13</td>
    <td align="right">12.16</td>
    <td align="right">12.16</td>
    <td align="right">12.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">84.59</td>
    <td align="right">93.51</td>
    <td align="right">33.63</td>
    <td align="right">66.03</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.64</td>
    <td align="right">18.41</td>
    <td align="right">18.44</td>
    <td align="right">18.42</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">19.21</td>
    <td align="right">19.30</td>
    <td align="right">19.35</td>
    <td align="right">19.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">124.83</td>
    <td align="right">135.23</td>
    <td align="right">39.57</td>
    <td align="right">91.88</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.87</td>
    <td align="right">22.07</td>
    <td align="right">22.07</td>
    <td align="right">22.06</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.88</td>
    <td align="right">25.33</td>
    <td align="right">25.36</td>
    <td align="right">25.35</td>
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
    <td align="right">16.12</td>
    <td align="right">19.19</td>
    <td align="right">19.18</td>
    <td align="right">19.15</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.91</td>
    <td align="right">6.60</td>
    <td align="right">6.60</td>
    <td align="right">6.61</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.80</td>
    <td align="right">6.51</td>
    <td align="right">6.51</td>
    <td align="right">6.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">51.40</td>
    <td align="right">55.40</td>
    <td align="right">55.39</td>
    <td align="right">55.41</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.94</td>
    <td align="right">12.24</td>
    <td align="right">11.99</td>
    <td align="right">11.94</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.89</td>
    <td align="right">12.66</td>
    <td align="right">12.62</td>
    <td align="right">12.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.93</td>
    <td align="right">83.09</td>
    <td align="right">83.01</td>
    <td align="right">83.05</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.34</td>
    <td align="right">18.43</td>
    <td align="right">18.46</td>
    <td align="right">18.46</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.89</td>
    <td align="right">19.12</td>
    <td align="right">19.06</td>
    <td align="right">19.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">124.91</td>
    <td align="right">127.87</td>
    <td align="right">127.87</td>
    <td align="right">127.87</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.11</td>
    <td align="right">22.16</td>
    <td align="right">22.20</td>
    <td align="right">22.18</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.90</td>
    <td align="right">25.39</td>
    <td align="right">25.39</td>
    <td align="right">25.41</td>
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
    <td align="right">13.63</td>
    <td align="right">16.54</td>
    <td align="right">22.59</td>
    <td align="right">19.85</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.08</td>
    <td align="right">5.55</td>
    <td align="right">5.56</td>
    <td align="right">5.52</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.80</td>
    <td align="right">6.39</td>
    <td align="right">6.40</td>
    <td align="right">6.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">47.74</td>
    <td align="right">55.50</td>
    <td align="right">30.04</td>
    <td align="right">43.57</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.63</td>
    <td align="right">11.77</td>
    <td align="right">11.66</td>
    <td align="right">11.69</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">12.03</td>
    <td align="right">12.35</td>
    <td align="right">12.37</td>
    <td align="right">12.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">79.42</td>
    <td align="right">97.12</td>
    <td align="right">37.00</td>
    <td align="right">67.88</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.80</td>
    <td align="right">18.08</td>
    <td align="right">18.07</td>
    <td align="right">18.06</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.45</td>
    <td align="right">20.52</td>
    <td align="right">20.55</td>
    <td align="right">20.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">115.91</td>
    <td align="right">139.38</td>
    <td align="right">44.04</td>
    <td align="right">94.26</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.72</td>
    <td align="right">24.67</td>
    <td align="right">24.68</td>
    <td align="right">24.69</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">25.35</td>
    <td align="right">25.43</td>
    <td align="right">25.50</td>
    <td align="right">25.39</td>
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
    <td align="right">12.60</td>
    <td align="right">16.84</td>
    <td align="right">16.90</td>
    <td align="right">16.86</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.51</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.75</td>
    <td align="right">6.35</td>
    <td align="right">6.37</td>
    <td align="right">6.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">45.98</td>
    <td align="right">58.06</td>
    <td align="right">57.68</td>
    <td align="right">57.98</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.91</td>
    <td align="right">11.94</td>
    <td align="right">11.98</td>
    <td align="right">11.95</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">12.29</td>
    <td align="right">12.59</td>
    <td align="right">12.63</td>
    <td align="right">13.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.15</td>
    <td align="right">112.80</td>
    <td align="right">112.88</td>
    <td align="right">112.75</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.95</td>
    <td align="right">18.19</td>
    <td align="right">18.21</td>
    <td align="right">18.24</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.65</td>
    <td align="right">20.74</td>
    <td align="right">20.75</td>
    <td align="right">20.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">115.84</td>
    <td align="right">163.41</td>
    <td align="right">163.94</td>
    <td align="right">163.26</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.69</td>
    <td align="right">24.68</td>
    <td align="right">24.70</td>
    <td align="right">24.74</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">25.22</td>
    <td align="right">25.27</td>
    <td align="right">25.29</td>
    <td align="right">25.27</td>
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
    <td align="right">7.41</td>
    <td align="right">8.40</td>
    <td align="right">15.50</td>
    <td align="right">14.52</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">6.82</td>
    <td align="right">9.18</td>
    <td align="right">16.67</td>
    <td align="right">15.27</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.19</td>
    <td align="right">3.93</td>
    <td align="right">3.92</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.40</td>
    <td align="right">16.02</td>
    <td align="right">19.32</td>
    <td align="right">20.43</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.91</td>
    <td align="right">19.39</td>
    <td align="right">22.12</td>
    <td align="right">23.47</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.60</td>
    <td align="right">7.89</td>
    <td align="right">7.87</td>
    <td align="right">7.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.35</td>
    <td align="right">30.94</td>
    <td align="right">25.67</td>
    <td align="right">30.97</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">34.81</td>
    <td align="right">32.42</td>
    <td align="right">28.74</td>
    <td align="right">34.21</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">18.99</td>
    <td align="right">20.58</td>
    <td align="right">14.90</td>
    <td align="right">23.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.31</td>
    <td align="right">39.41</td>
    <td align="right">26.61</td>
    <td align="right">39.35</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.91</td>
    <td align="right">44.66</td>
    <td align="right">33.72</td>
    <td align="right">47.99</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.19</td>
    <td align="right">23.95</td>
    <td align="right">16.87</td>
    <td align="right">28.43</td>
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
    <td align="right">6.35</td>
    <td align="right">7.03</td>
    <td align="right">7.02</td>
    <td align="right">7.01</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.23</td>
    <td align="right">8.97</td>
    <td align="right">8.93</td>
    <td align="right">8.94</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.89</td>
    <td align="right">4.70</td>
    <td align="right">4.75</td>
    <td align="right">4.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.19</td>
    <td align="right">16.59</td>
    <td align="right">16.67</td>
    <td align="right">16.62</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.66</td>
    <td align="right">20.96</td>
    <td align="right">20.92</td>
    <td align="right">20.90</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.67</td>
    <td align="right">7.83</td>
    <td align="right">7.79</td>
    <td align="right">7.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.77</td>
    <td align="right">30.94</td>
    <td align="right">30.92</td>
    <td align="right">30.93</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">34.86</td>
    <td align="right">34.16</td>
    <td align="right">34.17</td>
    <td align="right">34.27</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.27</td>
    <td align="right">21.17</td>
    <td align="right">21.19</td>
    <td align="right">21.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.45</td>
    <td align="right">39.33</td>
    <td align="right">39.35</td>
    <td align="right">39.37</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.80</td>
    <td align="right">51.71</td>
    <td align="right">51.90</td>
    <td align="right">50.34</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.17</td>
    <td align="right">24.20</td>
    <td align="right">24.24</td>
    <td align="right">24.26</td>
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
    <td align="right">6.44</td>
    <td align="right">7.65</td>
    <td align="right">15.38</td>
    <td align="right">13.88</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">6.66</td>
    <td align="right">8.97</td>
    <td align="right">16.17</td>
    <td align="right">14.90</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.67</td>
    <td align="right">5.07</td>
    <td align="right">4.98</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.73</td>
    <td align="right">15.72</td>
    <td align="right">19.11</td>
    <td align="right">20.03</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.61</td>
    <td align="right">19.84</td>
    <td align="right">23.01</td>
    <td align="right">23.93</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.45</td>
    <td align="right">8.26</td>
    <td align="right">8.21</td>
    <td align="right">8.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.29</td>
    <td align="right">30.06</td>
    <td align="right">23.69</td>
    <td align="right">30.65</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">34.51</td>
    <td align="right">31.96</td>
    <td align="right">27.94</td>
    <td align="right">33.13</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">18.43</td>
    <td align="right">20.52</td>
    <td align="right">14.63</td>
    <td align="right">24.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.21</td>
    <td align="right">39.81</td>
    <td align="right">25.00</td>
    <td align="right">39.02</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.06</td>
    <td align="right">43.04</td>
    <td align="right">33.03</td>
    <td align="right">44.53</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.46</td>
    <td align="right">23.57</td>
    <td align="right">16.34</td>
    <td align="right">27.95</td>
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
    <td align="right">6.31</td>
    <td align="right">7.28</td>
    <td align="right">7.21</td>
    <td align="right">7.22</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.11</td>
    <td align="right">8.40</td>
    <td align="right">8.42</td>
    <td align="right">8.41</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.50</td>
    <td align="right">3.65</td>
    <td align="right">3.64</td>
    <td align="right">3.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.17</td>
    <td align="right">16.24</td>
    <td align="right">16.26</td>
    <td align="right">16.24</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.28</td>
    <td align="right">20.94</td>
    <td align="right">21.00</td>
    <td align="right">21.17</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.63</td>
    <td align="right">8.45</td>
    <td align="right">8.42</td>
    <td align="right">8.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.25</td>
    <td align="right">31.15</td>
    <td align="right">31.22</td>
    <td align="right">31.16</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">34.51</td>
    <td align="right">31.33</td>
    <td align="right">31.40</td>
    <td align="right">31.37</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">18.51</td>
    <td align="right">20.76</td>
    <td align="right">20.77</td>
    <td align="right">20.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.17</td>
    <td align="right">39.01</td>
    <td align="right">39.04</td>
    <td align="right">39.07</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.97</td>
    <td align="right">50.16</td>
    <td align="right">50.16</td>
    <td align="right">50.12</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.37</td>
    <td align="right">23.69</td>
    <td align="right">23.80</td>
    <td align="right">23.72</td>
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
    <td align="right">4.65</td>
    <td align="right">4.34</td>
    <td align="right">4.34</td>
    <td align="right">4.36</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.96</td>
    <td align="right">6.19</td>
    <td align="right">6.20</td>
    <td align="right">6.24</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.44</td>
    <td align="right">6.54</td>
    <td align="right">6.54</td>
    <td align="right">6.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.48</td>
    <td align="right">8.32</td>
    <td align="right">8.35</td>
    <td align="right">8.32</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.62</td>
    <td align="right">9.57</td>
    <td align="right">9.59</td>
    <td align="right">9.56</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.68</td>
    <td align="right">12.81</td>
    <td align="right">12.83</td>
    <td align="right">12.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.68</td>
    <td align="right">20.47</td>
    <td align="right">14.67</td>
    <td align="right">24.53</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.12</td>
    <td align="right">26.33</td>
    <td align="right">21.68</td>
    <td align="right">30.95</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.32</td>
    <td align="right">26.73</td>
    <td align="right">22.09</td>
    <td align="right">30.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.88</td>
    <td align="right">23.83</td>
    <td align="right">16.58</td>
    <td align="right">27.00</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.19</td>
    <td align="right">36.64</td>
    <td align="right">24.99</td>
    <td align="right">36.93</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.57</td>
    <td align="right">36.87</td>
    <td align="right">25.26</td>
    <td align="right">36.83</td>
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
    <td align="right">4.32</td>
    <td align="right">3.99</td>
    <td align="right">3.98</td>
    <td align="right">4.01</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.01</td>
    <td align="right">6.05</td>
    <td align="right">6.09</td>
    <td align="right">6.09</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.72</td>
    <td align="right">5.43</td>
    <td align="right">5.47</td>
    <td align="right">5.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.64</td>
    <td align="right">8.46</td>
    <td align="right">8.46</td>
    <td align="right">8.46</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.93</td>
    <td align="right">9.90</td>
    <td align="right">9.90</td>
    <td align="right">9.85</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.77</td>
    <td align="right">12.83</td>
    <td align="right">12.82</td>
    <td align="right">12.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.84</td>
    <td align="right">20.80</td>
    <td align="right">20.82</td>
    <td align="right">20.89</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.47</td>
    <td align="right">26.23</td>
    <td align="right">26.25</td>
    <td align="right">26.33</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.22</td>
    <td align="right">26.47</td>
    <td align="right">26.49</td>
    <td align="right">26.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.94</td>
    <td align="right">23.93</td>
    <td align="right">23.95</td>
    <td align="right">23.95</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">31.90</td>
    <td align="right">31.79</td>
    <td align="right">31.78</td>
    <td align="right">31.79</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.80</td>
    <td align="right">32.09</td>
    <td align="right">32.09</td>
    <td align="right">32.05</td>
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
    <td align="right">4.39</td>
    <td align="right">4.58</td>
    <td align="right">4.59</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.79</td>
    <td align="right">6.12</td>
    <td align="right">6.09</td>
    <td align="right">6.11</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.45</td>
    <td align="right">6.49</td>
    <td align="right">6.49</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.66</td>
    <td align="right">8.36</td>
    <td align="right">8.36</td>
    <td align="right">8.34</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.51</td>
    <td align="right">10.53</td>
    <td align="right">10.54</td>
    <td align="right">10.51</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.34</td>
    <td align="right">12.44</td>
    <td align="right">12.48</td>
    <td align="right">12.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.37</td>
    <td align="right">18.83</td>
    <td align="right">14.41</td>
    <td align="right">24.35</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.39</td>
    <td align="right">26.00</td>
    <td align="right">19.78</td>
    <td align="right">29.89</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.85</td>
    <td align="right">26.09</td>
    <td align="right">19.81</td>
    <td align="right">30.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.54</td>
    <td align="right">21.45</td>
    <td align="right">16.13</td>
    <td align="right">27.14</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">30.90</td>
    <td align="right">35.72</td>
    <td align="right">22.68</td>
    <td align="right">36.22</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.89</td>
    <td align="right">31.98</td>
    <td align="right">22.74</td>
    <td align="right">35.85</td>
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
    <td align="right">3.95</td>
    <td align="right">4.12</td>
    <td align="right">4.19</td>
    <td align="right">4.24</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.79</td>
    <td align="right">5.90</td>
    <td align="right">5.90</td>
    <td align="right">5.91</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.22</td>
    <td align="right">6.04</td>
    <td align="right">6.02</td>
    <td align="right">6.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.44</td>
    <td align="right">9.17</td>
    <td align="right">9.18</td>
    <td align="right">9.19</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.70</td>
    <td align="right">9.63</td>
    <td align="right">9.63</td>
    <td align="right">9.64</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.53</td>
    <td align="right">11.41</td>
    <td align="right">11.44</td>
    <td align="right">11.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.85</td>
    <td align="right">21.42</td>
    <td align="right">21.01</td>
    <td align="right">21.00</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.08</td>
    <td align="right">25.58</td>
    <td align="right">25.57</td>
    <td align="right">25.57</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.00</td>
    <td align="right">25.76</td>
    <td align="right">25.79</td>
    <td align="right">25.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.47</td>
    <td align="right">23.68</td>
    <td align="right">23.68</td>
    <td align="right">23.69</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">30.69</td>
    <td align="right">31.42</td>
    <td align="right">31.44</td>
    <td align="right">31.45</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.34</td>
    <td align="right">31.73</td>
    <td align="right">31.72</td>
    <td align="right">31.76</td>
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
    <td align="right">8.49</td>
    <td align="right">9.45</td>
    <td align="right">16.12</td>
    <td align="right">15.30</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.13</td>
    <td align="right">10.95</td>
    <td align="right">20.70</td>
    <td align="right">18.31</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.86</td>
    <td align="right">14.39</td>
    <td align="right">21.59</td>
    <td align="right">19.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.04</td>
    <td align="right">17.42</td>
    <td align="right">18.29</td>
    <td align="right">21.86</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.54</td>
    <td align="right">22.40</td>
    <td align="right">21.20</td>
    <td align="right">26.43</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.49</td>
    <td align="right">30.76</td>
    <td align="right">27.39</td>
    <td align="right">29.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.36</td>
    <td align="right">27.87</td>
    <td align="right">21.79</td>
    <td align="right">31.08</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.81</td>
    <td align="right">34.31</td>
    <td align="right">26.93</td>
    <td align="right">37.84</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.72</td>
    <td align="right">47.50</td>
    <td align="right">31.26</td>
    <td align="right">41.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.05</td>
    <td align="right">42.82</td>
    <td align="right">25.05</td>
    <td align="right">43.18</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.38</td>
    <td align="right">50.98</td>
    <td align="right">30.10</td>
    <td align="right">49.03</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">73.11</td>
    <td align="right">69.37</td>
    <td align="right">38.66</td>
    <td align="right">56.58</td>
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
    <td align="right">8.16</td>
    <td align="right">8.74</td>
    <td align="right">8.74</td>
    <td align="right">8.75</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.42</td>
    <td align="right">11.19</td>
    <td align="right">11.22</td>
    <td align="right">11.20</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.23</td>
    <td align="right">14.57</td>
    <td align="right">14.56</td>
    <td align="right">14.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.17</td>
    <td align="right">18.29</td>
    <td align="right">18.36</td>
    <td align="right">18.35</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.96</td>
    <td align="right">22.70</td>
    <td align="right">22.59</td>
    <td align="right">22.56</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">27.02</td>
    <td align="right">29.09</td>
    <td align="right">29.08</td>
    <td align="right">29.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.65</td>
    <td align="right">27.59</td>
    <td align="right">27.45</td>
    <td align="right">27.54</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.11</td>
    <td align="right">39.86</td>
    <td align="right">39.88</td>
    <td align="right">39.85</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.53</td>
    <td align="right">49.95</td>
    <td align="right">49.89</td>
    <td align="right">49.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.72</td>
    <td align="right">42.92</td>
    <td align="right">42.91</td>
    <td align="right">42.98</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.51</td>
    <td align="right">52.22</td>
    <td align="right">52.24</td>
    <td align="right">52.10</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">73.38</td>
    <td align="right">74.30</td>
    <td align="right">74.39</td>
    <td align="right">74.41</td>
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
    <td align="right">7.71</td>
    <td align="right">8.67</td>
    <td align="right">15.71</td>
    <td align="right">15.05</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.35</td>
    <td align="right">11.59</td>
    <td align="right">20.74</td>
    <td align="right">18.74</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.64</td>
    <td align="right">13.78</td>
    <td align="right">20.60</td>
    <td align="right">19.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.99</td>
    <td align="right">19.00</td>
    <td align="right">18.95</td>
    <td align="right">22.83</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.39</td>
    <td align="right">21.21</td>
    <td align="right">20.44</td>
    <td align="right">25.62</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.68</td>
    <td align="right">30.83</td>
    <td align="right">24.24</td>
    <td align="right">31.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.01</td>
    <td align="right">28.07</td>
    <td align="right">21.80</td>
    <td align="right">31.22</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.60</td>
    <td align="right">33.78</td>
    <td align="right">25.75</td>
    <td align="right">37.31</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.45</td>
    <td align="right">45.96</td>
    <td align="right">25.38</td>
    <td align="right">40.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.55</td>
    <td align="right">43.03</td>
    <td align="right">25.02</td>
    <td align="right">42.97</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.32</td>
    <td align="right">51.42</td>
    <td align="right">28.20</td>
    <td align="right">49.02</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">74.20</td>
    <td align="right">65.88</td>
    <td align="right">27.02</td>
    <td align="right">55.20</td>
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
    <td align="right">7.97</td>
    <td align="right">8.62</td>
    <td align="right">8.62</td>
    <td align="right">8.59</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.57</td>
    <td align="right">10.63</td>
    <td align="right">10.62</td>
    <td align="right">10.63</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.57</td>
    <td align="right">14.95</td>
    <td align="right">14.95</td>
    <td align="right">14.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.57</td>
    <td align="right">17.48</td>
    <td align="right">17.52</td>
    <td align="right">17.46</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.75</td>
    <td align="right">21.48</td>
    <td align="right">21.56</td>
    <td align="right">21.56</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">28.37</td>
    <td align="right">29.48</td>
    <td align="right">29.39</td>
    <td align="right">29.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.88</td>
    <td align="right">30.75</td>
    <td align="right">30.75</td>
    <td align="right">30.79</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.56</td>
    <td align="right">40.14</td>
    <td align="right">40.19</td>
    <td align="right">40.17</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.50</td>
    <td align="right">48.91</td>
    <td align="right">48.85</td>
    <td align="right">48.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.43</td>
    <td align="right">43.42</td>
    <td align="right">43.35</td>
    <td align="right">43.34</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.20</td>
    <td align="right">51.96</td>
    <td align="right">52.02</td>
    <td align="right">51.97</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">73.26</td>
    <td align="right">72.66</td>
    <td align="right">72.67</td>
    <td align="right">72.67</td>
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
    <td align="right">26.16</td>
    <td align="right">6.48</td>
    <td align="right">4.35</td>
    <td align="right">13.18</td>
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
    <td align="right">10.30</td>
    <td align="right">10.87</td>
    <td align="right">17.43</td>
    <td align="right">15.44</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.08</td>
    <td align="right">4.10</td>
    <td align="right">4.09</td>
    <td align="right">4.11</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.07</td>
    <td align="right">4.60</td>
    <td align="right">4.62</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.75</td>
    <td align="right">16.15</td>
    <td align="right">18.59</td>
    <td align="right">19.86</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.58</td>
    <td align="right">4.69</td>
    <td align="right">4.70</td>
    <td align="right">4.70</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.55</td>
    <td align="right">5.27</td>
    <td align="right">5.25</td>
    <td align="right">5.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">19.09</td>
    <td align="right">19.90</td>
    <td align="right">17.92</td>
    <td align="right">22.26</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">5.30</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.92</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="right">5.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.93</td>
    <td align="right">24.25</td>
    <td align="right">17.86</td>
    <td align="right">25.07</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.42</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.31</td>
    <td align="right">3.45</td>
    <td align="right">3.45</td>
    <td align="right">3.43</td>
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
    <td align="right">10.31</td>
    <td align="right">10.87</td>
    <td align="right">10.94</td>
    <td align="right">10.93</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.05</td>
    <td align="right">4.08</td>
    <td align="right">4.09</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.07</td>
    <td align="right">4.59</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.70</td>
    <td align="right">14.76</td>
    <td align="right">14.77</td>
    <td align="right">14.77</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.58</td>
    <td align="right">4.69</td>
    <td align="right">4.69</td>
    <td align="right">4.69</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.57</td>
    <td align="right">5.26</td>
    <td align="right">5.25</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.88</td>
    <td align="right">17.68</td>
    <td align="right">17.74</td>
    <td align="right">17.72</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">5.30</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.93</td>
    <td align="right">5.73</td>
    <td align="right">5.73</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.16</td>
    <td align="right">24.83</td>
    <td align="right">24.84</td>
    <td align="right">24.82</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.41</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.31</td>
    <td align="right">3.44</td>
    <td align="right">3.45</td>
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
    <td align="right">10.45</td>
    <td align="right">10.51</td>
    <td align="right">18.51</td>
    <td align="right">15.64</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.50</td>
    <td align="right">2.50</td>
    <td align="right">2.48</td>
    <td align="right">2.47</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.03</td>
    <td align="right">2.00</td>
    <td align="right">2.00</td>
    <td align="right">2.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.29</td>
    <td align="right">15.22</td>
    <td align="right">19.71</td>
    <td align="right">19.36</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.02</td>
    <td align="right">2.76</td>
    <td align="right">2.73</td>
    <td align="right">2.73</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.48</td>
    <td align="right">2.24</td>
    <td align="right">2.20</td>
    <td align="right">2.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.56</td>
    <td align="right">18.62</td>
    <td align="right">19.57</td>
    <td align="right">21.20</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.42</td>
    <td align="right">2.91</td>
    <td align="right">2.90</td>
    <td align="right">2.87</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.90</td>
    <td align="right">2.38</td>
    <td align="right">2.39</td>
    <td align="right">2.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.72</td>
    <td align="right">22.84</td>
    <td align="right">19.90</td>
    <td align="right">23.76</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">4.82</td>
    <td align="right">3.21</td>
    <td align="right">3.22</td>
    <td align="right">3.20</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.23</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="right">2.54</td>
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
    <td align="right">10.32</td>
    <td align="right">11.22</td>
    <td align="right">11.19</td>
    <td align="right">11.39</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.50</td>
    <td align="right">2.52</td>
    <td align="right">2.48</td>
    <td align="right">2.50</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.04</td>
    <td align="right">1.98</td>
    <td align="right">1.99</td>
    <td align="right">1.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.56</td>
    <td align="right">17.17</td>
    <td align="right">17.47</td>
    <td align="right">17.03</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.01</td>
    <td align="right">2.76</td>
    <td align="right">2.73</td>
    <td align="right">2.72</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.48</td>
    <td align="right">2.22</td>
    <td align="right">2.22</td>
    <td align="right">2.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.54</td>
    <td align="right">21.11</td>
    <td align="right">21.13</td>
    <td align="right">20.98</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.42</td>
    <td align="right">2.92</td>
    <td align="right">2.87</td>
    <td align="right">2.92</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.90</td>
    <td align="right">2.40</td>
    <td align="right">2.39</td>
    <td align="right">2.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.67</td>
    <td align="right">26.92</td>
    <td align="right">26.47</td>
    <td align="right">26.20</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">4.82</td>
    <td align="right">3.21</td>
    <td align="right">3.19</td>
    <td align="right">3.22</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.23</td>
    <td align="right">2.54</td>
    <td align="right">2.56</td>
    <td align="right">2.55</td>
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
    <td align="right">3.24</td>
    <td align="right">5.87</td>
    <td align="right">13.84</td>
    <td align="right">11.59</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.31</td>
    <td align="right">5.75</td>
    <td align="right">13.15</td>
    <td align="right">11.44</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.88</td>
    <td align="right">2.68</td>
    <td align="right">2.69</td>
    <td align="right">2.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.40</td>
    <td align="right">8.29</td>
    <td align="right">14.53</td>
    <td align="right">13.58</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.07</td>
    <td align="right">8.28</td>
    <td align="right">14.60</td>
    <td align="right">14.05</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.77</td>
    <td align="right">2.50</td>
    <td align="right">2.51</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.83</td>
    <td align="right">11.73</td>
    <td align="right">15.81</td>
    <td align="right">17.24</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.97</td>
    <td align="right">11.39</td>
    <td align="right">15.30</td>
    <td align="right">16.08</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.38</td>
    <td align="right">4.49</td>
    <td align="right">3.35</td>
    <td align="right">13.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.21</td>
    <td align="right">13.00</td>
    <td align="right">15.16</td>
    <td align="right">18.18</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.96</td>
    <td align="right">13.07</td>
    <td align="right">16.07</td>
    <td align="right">17.42</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.43</td>
    <td align="right">4.50</td>
    <td align="right">3.33</td>
    <td align="right">13.79</td>
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
    <td align="right">3.26</td>
    <td align="right">3.89</td>
    <td align="right">3.89</td>
    <td align="right">3.89</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.32</td>
    <td align="right">3.71</td>
    <td align="right">3.71</td>
    <td align="right">3.70</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.88</td>
    <td align="right">2.68</td>
    <td align="right">2.69</td>
    <td align="right">2.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.39</td>
    <td align="right">4.80</td>
    <td align="right">4.81</td>
    <td align="right">4.81</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.02</td>
    <td align="right">4.95</td>
    <td align="right">4.95</td>
    <td align="right">4.95</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">2.50</td>
    <td align="right">2.51</td>
    <td align="right">2.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.86</td>
    <td align="right">7.79</td>
    <td align="right">7.78</td>
    <td align="right">7.76</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.99</td>
    <td align="right">7.49</td>
    <td align="right">7.48</td>
    <td align="right">7.50</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.40</td>
    <td align="right">4.46</td>
    <td align="right">4.46</td>
    <td align="right">4.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.17</td>
    <td align="right">8.17</td>
    <td align="right">8.18</td>
    <td align="right">8.16</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.95</td>
    <td align="right">8.34</td>
    <td align="right">8.39</td>
    <td align="right">8.39</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.43</td>
    <td align="right">4.48</td>
    <td align="right">4.48</td>
    <td align="right">4.49</td>
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
    <td align="right">5.83</td>
    <td align="right">15.31</td>
    <td align="right">11.45</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.17</td>
    <td align="right">5.54</td>
    <td align="right">13.96</td>
    <td align="right">10.81</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.61</td>
    <td align="right">2.64</td>
    <td align="right">2.64</td>
    <td align="right">2.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.97</td>
    <td align="right">8.23</td>
    <td align="right">14.54</td>
    <td align="right">13.56</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">3.84</td>
    <td align="right">8.08</td>
    <td align="right">14.29</td>
    <td align="right">13.39</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.24</td>
    <td align="right">2.52</td>
    <td align="right">2.51</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.35</td>
    <td align="right">11.42</td>
    <td align="right">15.63</td>
    <td align="right">16.44</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.57</td>
    <td align="right">11.11</td>
    <td align="right">14.78</td>
    <td align="right">15.44</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.21</td>
    <td align="right">4.12</td>
    <td align="right">3.18</td>
    <td align="right">13.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">5.81</td>
    <td align="right">13.07</td>
    <td align="right">14.88</td>
    <td align="right">17.28</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.78</td>
    <td align="right">13.21</td>
    <td align="right">15.23</td>
    <td align="right">17.28</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.27</td>
    <td align="right">4.15</td>
    <td align="right">3.17</td>
    <td align="right">13.58</td>
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
    <td align="right">3.11</td>
    <td align="right">3.25</td>
    <td align="right">3.26</td>
    <td align="right">3.21</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.19</td>
    <td align="right">3.40</td>
    <td align="right">3.41</td>
    <td align="right">3.39</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.66</td>
    <td align="right">2.64</td>
    <td align="right">2.64</td>
    <td align="right">2.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.94</td>
    <td align="right">4.98</td>
    <td align="right">4.98</td>
    <td align="right">4.98</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">3.88</td>
    <td align="right">4.90</td>
    <td align="right">4.94</td>
    <td align="right">4.94</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.24</td>
    <td align="right">2.52</td>
    <td align="right">2.52</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.36</td>
    <td align="right">7.22</td>
    <td align="right">7.21</td>
    <td align="right">7.24</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.57</td>
    <td align="right">7.31</td>
    <td align="right">7.27</td>
    <td align="right">7.29</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.20</td>
    <td align="right">4.30</td>
    <td align="right">4.30</td>
    <td align="right">4.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">5.81</td>
    <td align="right">8.59</td>
    <td align="right">8.59</td>
    <td align="right">8.58</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.75</td>
    <td align="right">9.11</td>
    <td align="right">9.01</td>
    <td align="right">9.12</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.25</td>
    <td align="right">4.32</td>
    <td align="right">4.32</td>
    <td align="right">4.32</td>
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
    <td align="right">2.83</td>
    <td align="right">2.49</td>
    <td align="right">2.49</td>
    <td align="right">2.49</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.91</td>
    <td align="right">4.17</td>
    <td align="right">4.17</td>
    <td align="right">4.17</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.08</td>
    <td align="right">4.02</td>
    <td align="right">4.02</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.97</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.51</td>
    <td align="right">3.88</td>
    <td align="right">3.89</td>
    <td align="right">3.88</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.23</td>
    <td align="right">4.11</td>
    <td align="right">4.11</td>
    <td align="right">4.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.47</td>
    <td align="right">4.22</td>
    <td align="right">3.17</td>
    <td align="right">13.46</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.81</td>
    <td align="right">6.29</td>
    <td align="right">5.20</td>
    <td align="right">16.56</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.05</td>
    <td align="right">6.13</td>
    <td align="right">4.92</td>
    <td align="right">16.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.49</td>
    <td align="right">4.23</td>
    <td align="right">3.14</td>
    <td align="right">13.36</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.90</td>
    <td align="right">7.22</td>
    <td align="right">5.29</td>
    <td align="right">17.30</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.24</td>
    <td align="right">7.05</td>
    <td align="right">5.09</td>
    <td align="right">16.89</td>
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
    <td align="right">2.86</td>
    <td align="right">2.50</td>
    <td align="right">2.48</td>
    <td align="right">2.48</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.90</td>
    <td align="right">4.18</td>
    <td align="right">4.19</td>
    <td align="right">4.18</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.06</td>
    <td align="right">4.02</td>
    <td align="right">4.03</td>
    <td align="right">4.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.95</td>
    <td align="right">2.53</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.49</td>
    <td align="right">3.88</td>
    <td align="right">3.90</td>
    <td align="right">3.90</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.25</td>
    <td align="right">4.11</td>
    <td align="right">4.11</td>
    <td align="right">4.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.45</td>
    <td align="right">4.19</td>
    <td align="right">4.20</td>
    <td align="right">4.20</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.82</td>
    <td align="right">6.45</td>
    <td align="right">6.43</td>
    <td align="right">6.44</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.03</td>
    <td align="right">6.22</td>
    <td align="right">6.21</td>
    <td align="right">6.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.50</td>
    <td align="right">4.21</td>
    <td align="right">4.21</td>
    <td align="right">4.21</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.91</td>
    <td align="right">7.39</td>
    <td align="right">7.37</td>
    <td align="right">7.37</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.25</td>
    <td align="right">7.19</td>
    <td align="right">7.13</td>
    <td align="right">7.13</td>
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
    <td align="right">2.60</td>
    <td align="right">2.37</td>
    <td align="right">2.37</td>
    <td align="right">2.37</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.67</td>
    <td align="right">3.98</td>
    <td align="right">3.98</td>
    <td align="right">3.98</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.88</td>
    <td align="right">3.95</td>
    <td align="right">3.95</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.76</td>
    <td align="right">2.41</td>
    <td align="right">2.41</td>
    <td align="right">2.41</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.14</td>
    <td align="right">3.82</td>
    <td align="right">3.81</td>
    <td align="right">3.82</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
    <td align="right">4.06</td>
    <td align="right">4.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.43</td>
    <td align="right">4.07</td>
    <td align="right">3.01</td>
    <td align="right">13.14</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.48</td>
    <td align="right">5.62</td>
    <td align="right">4.31</td>
    <td align="right">16.22</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">5.85</td>
    <td align="right">5.31</td>
    <td align="right">4.16</td>
    <td align="right">16.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.48</td>
    <td align="right">4.09</td>
    <td align="right">2.99</td>
    <td align="right">13.12</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.73</td>
    <td align="right">7.05</td>
    <td align="right">4.31</td>
    <td align="right">16.89</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.16</td>
    <td align="right">6.93</td>
    <td align="right">4.20</td>
    <td align="right">16.62</td>
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
    <td align="right">2.63</td>
    <td align="right">2.37</td>
    <td align="right">2.37</td>
    <td align="right">2.37</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.63</td>
    <td align="right">3.98</td>
    <td align="right">3.98</td>
    <td align="right">3.97</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.92</td>
    <td align="right">3.97</td>
    <td align="right">3.97</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.74</td>
    <td align="right">2.42</td>
    <td align="right">2.42</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.15</td>
    <td align="right">3.84</td>
    <td align="right">3.82</td>
    <td align="right">3.83</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.02</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.40</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.51</td>
    <td align="right">6.03</td>
    <td align="right">6.02</td>
    <td align="right">6.03</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">5.85</td>
    <td align="right">5.67</td>
    <td align="right">5.66</td>
    <td align="right">5.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.45</td>
    <td align="right">4.09</td>
    <td align="right">4.10</td>
    <td align="right">4.10</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.70</td>
    <td align="right">7.19</td>
    <td align="right">7.22</td>
    <td align="right">7.19</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.18</td>
    <td align="right">7.08</td>
    <td align="right">7.05</td>
    <td align="right">7.08</td>
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
    <td align="right">6.66</td>
    <td align="right">14.98</td>
    <td align="right">12.45</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.76</td>
    <td align="right">7.89</td>
    <td align="right">18.15</td>
    <td align="right">15.03</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.24</td>
    <td align="right">9.94</td>
    <td align="right">18.63</td>
    <td align="right">14.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.63</td>
    <td align="right">9.07</td>
    <td align="right">13.47</td>
    <td align="right">14.46</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.55</td>
    <td align="right">9.26</td>
    <td align="right">15.32</td>
    <td align="right">16.11</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.95</td>
    <td align="right">13.55</td>
    <td align="right">20.10</td>
    <td align="right">18.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">12.01</td>
    <td align="right">10.67</td>
    <td align="right">13.14</td>
    <td align="right">15.93</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.52</td>
    <td align="right">11.99</td>
    <td align="right">16.45</td>
    <td align="right">18.50</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.82</td>
    <td align="right">14.50</td>
    <td align="right">18.52</td>
    <td align="right">19.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.30</td>
    <td align="right">13.36</td>
    <td align="right">13.95</td>
    <td align="right">17.43</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.16</td>
    <td align="right">13.63</td>
    <td align="right">15.70</td>
    <td align="right">19.63</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.83</td>
    <td align="right">20.27</td>
    <td align="right">22.50</td>
    <td align="right">22.87</td>
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
    <td align="right">6.32</td>
    <td align="right">6.65</td>
    <td align="right">6.65</td>
    <td align="right">6.65</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.79</td>
    <td align="right">8.05</td>
    <td align="right">8.05</td>
    <td align="right">8.05</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.28</td>
    <td align="right">10.44</td>
    <td align="right">10.42</td>
    <td align="right">10.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.69</td>
    <td align="right">9.05</td>
    <td align="right">9.05</td>
    <td align="right">9.05</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.55</td>
    <td align="right">10.29</td>
    <td align="right">10.30</td>
    <td align="right">10.30</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.77</td>
    <td align="right">14.57</td>
    <td align="right">14.60</td>
    <td align="right">14.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.99</td>
    <td align="right">10.88</td>
    <td align="right">10.87</td>
    <td align="right">10.87</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">16.13</td>
    <td align="right">12.42</td>
    <td align="right">12.42</td>
    <td align="right">12.44</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.50</td>
    <td align="right">15.84</td>
    <td align="right">15.04</td>
    <td align="right">15.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.33</td>
    <td align="right">13.76</td>
    <td align="right">13.77</td>
    <td align="right">13.77</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.12</td>
    <td align="right">15.40</td>
    <td align="right">15.40</td>
    <td align="right">15.44</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.64</td>
    <td align="right">20.96</td>
    <td align="right">20.90</td>
    <td align="right">21.20</td>
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
    <td align="right">6.85</td>
    <td align="right">15.25</td>
    <td align="right">12.72</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.74</td>
    <td align="right">7.79</td>
    <td align="right">17.83</td>
    <td align="right">15.69</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.28</td>
    <td align="right">9.82</td>
    <td align="right">18.06</td>
    <td align="right">15.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.03</td>
    <td align="right">9.40</td>
    <td align="right">13.91</td>
    <td align="right">14.87</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.72</td>
    <td align="right">9.26</td>
    <td align="right">15.00</td>
    <td align="right">16.03</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.49</td>
    <td align="right">13.38</td>
    <td align="right">19.08</td>
    <td align="right">17.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.03</td>
    <td align="right">11.16</td>
    <td align="right">13.52</td>
    <td align="right">16.58</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.69</td>
    <td align="right">11.91</td>
    <td align="right">16.08</td>
    <td align="right">18.14</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.34</td>
    <td align="right">13.45</td>
    <td align="right">16.57</td>
    <td align="right">18.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.34</td>
    <td align="right">13.60</td>
    <td align="right">14.32</td>
    <td align="right">17.53</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.81</td>
    <td align="right">13.37</td>
    <td align="right">15.70</td>
    <td align="right">19.36</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.83</td>
    <td align="right">20.89</td>
    <td align="right">19.35</td>
    <td align="right">22.80</td>
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
    <td align="right">5.99</td>
    <td align="right">4.15</td>
    <td align="right">4.16</td>
    <td align="right">4.17</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.76</td>
    <td align="right">7.99</td>
    <td align="right">8.01</td>
    <td align="right">8.01</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.44</td>
    <td align="right">9.89</td>
    <td align="right">9.41</td>
    <td align="right">9.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.15</td>
    <td align="right">6.40</td>
    <td align="right">6.33</td>
    <td align="right">6.34</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">14.76</td>
    <td align="right">10.20</td>
    <td align="right">10.20</td>
    <td align="right">10.17</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.54</td>
    <td align="right">12.73</td>
    <td align="right">13.19</td>
    <td align="right">12.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.05</td>
    <td align="right">7.29</td>
    <td align="right">7.29</td>
    <td align="right">7.34</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.64</td>
    <td align="right">12.38</td>
    <td align="right">12.39</td>
    <td align="right">12.39</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.76</td>
    <td align="right">14.50</td>
    <td align="right">14.44</td>
    <td align="right">14.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">13.33</td>
    <td align="right">9.28</td>
    <td align="right">9.14</td>
    <td align="right">9.16</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.14</td>
    <td align="right">15.21</td>
    <td align="right">15.20</td>
    <td align="right">15.20</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.92</td>
    <td align="right">19.33</td>
    <td align="right">19.66</td>
    <td align="right">19.87</td>
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
    <td align="right">52.05</td>
    <td align="right">23.76</td>
    <td align="right">14.41</td>
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
    <td align="right">14.65</td>
    <td align="right">15.19</td>
    <td align="right">20.22</td>
    <td align="right">18.70</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.75</td>
    <td align="right">5.77</td>
    <td align="right">5.76</td>
    <td align="right">5.78</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.81</td>
    <td align="right">7.43</td>
    <td align="right">7.42</td>
    <td align="right">7.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">47.70</td>
    <td align="right">51.89</td>
    <td align="right">26.52</td>
    <td align="right">39.33</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.94</td>
    <td align="right">10.90</td>
    <td align="right">10.89</td>
    <td align="right">10.87</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">12.07</td>
    <td align="right">13.16</td>
    <td align="right">13.16</td>
    <td align="right">13.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">85.55</td>
    <td align="right">84.90</td>
    <td align="right">31.57</td>
    <td align="right">60.61</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.08</td>
    <td align="right">18.11</td>
    <td align="right">18.11</td>
    <td align="right">18.11</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.07</td>
    <td align="right">18.89</td>
    <td align="right">18.89</td>
    <td align="right">18.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">122.17</td>
    <td align="right">118.59</td>
    <td align="right">35.84</td>
    <td align="right">81.07</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.92</td>
    <td align="right">21.65</td>
    <td align="right">21.65</td>
    <td align="right">21.66</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.68</td>
    <td align="right">15.26</td>
    <td align="right">15.25</td>
    <td align="right">15.24</td>
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
    <td align="right">13.12</td>
    <td align="right">13.78</td>
    <td align="right">13.82</td>
    <td align="right">13.79</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.01</td>
    <td align="right">5.04</td>
    <td align="right">5.06</td>
    <td align="right">5.05</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.37</td>
    <td align="right">5.94</td>
    <td align="right">5.97</td>
    <td align="right">5.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">43.45</td>
    <td align="right">38.19</td>
    <td align="right">38.21</td>
    <td align="right">38.24</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.91</td>
    <td align="right">10.88</td>
    <td align="right">10.87</td>
    <td align="right">10.87</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.40</td>
    <td align="right">12.44</td>
    <td align="right">12.41</td>
    <td align="right">12.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">82.16</td>
    <td align="right">68.05</td>
    <td align="right">68.12</td>
    <td align="right">68.10</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.88</td>
    <td align="right">17.91</td>
    <td align="right">17.91</td>
    <td align="right">17.93</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.03</td>
    <td align="right">18.82</td>
    <td align="right">18.82</td>
    <td align="right">18.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">120.55</td>
    <td align="right">106.96</td>
    <td align="right">106.89</td>
    <td align="right">106.85</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.00</td>
    <td align="right">21.79</td>
    <td align="right">21.70</td>
    <td align="right">21.72</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.59</td>
    <td align="right">15.17</td>
    <td align="right">15.19</td>
    <td align="right">15.19</td>
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
    <td align="right">17.61</td>
    <td align="right">17.50</td>
    <td align="right">22.12</td>
    <td align="right">20.26</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.55</td>
    <td align="right">3.84</td>
    <td align="right">3.81</td>
    <td align="right">3.82</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.27</td>
    <td align="right">3.18</td>
    <td align="right">3.21</td>
    <td align="right">3.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">46.93</td>
    <td align="right">45.40</td>
    <td align="right">26.83</td>
    <td align="right">35.89</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.49</td>
    <td align="right">8.30</td>
    <td align="right">8.31</td>
    <td align="right">8.28</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.31</td>
    <td align="right">7.18</td>
    <td align="right">7.17</td>
    <td align="right">7.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">84.94</td>
    <td align="right">83.59</td>
    <td align="right">33.53</td>
    <td align="right">59.23</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.70</td>
    <td align="right">11.96</td>
    <td align="right">11.99</td>
    <td align="right">11.98</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.23</td>
    <td align="right">9.37</td>
    <td align="right">9.35</td>
    <td align="right">9.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">122.51</td>
    <td align="right">116.96</td>
    <td align="right">38.93</td>
    <td align="right">79.72</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.58</td>
    <td align="right">14.74</td>
    <td align="right">14.76</td>
    <td align="right">14.73</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.21</td>
    <td align="right">11.12</td>
    <td align="right">11.12</td>
    <td align="right">11.12</td>
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
    <td align="right">14.16</td>
    <td align="right">15.68</td>
    <td align="right">15.61</td>
    <td align="right">15.64</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.38</td>
    <td align="right">3.59</td>
    <td align="right">3.65</td>
    <td align="right">3.59</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.97</td>
    <td align="right">3.70</td>
    <td align="right">3.74</td>
    <td align="right">3.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">45.93</td>
    <td align="right">50.07</td>
    <td align="right">47.54</td>
    <td align="right">47.46</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.52</td>
    <td align="right">8.13</td>
    <td align="right">8.16</td>
    <td align="right">8.17</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.15</td>
    <td align="right">6.99</td>
    <td align="right">7.01</td>
    <td align="right">7.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.87</td>
    <td align="right">82.82</td>
    <td align="right">84.62</td>
    <td align="right">82.54</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.63</td>
    <td align="right">12.11</td>
    <td align="right">12.09</td>
    <td align="right">12.10</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.30</td>
    <td align="right">9.58</td>
    <td align="right">9.60</td>
    <td align="right">9.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">121.72</td>
    <td align="right">116.47</td>
    <td align="right">121.40</td>
    <td align="right">116.78</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.41</td>
    <td align="right">14.60</td>
    <td align="right">14.62</td>
    <td align="right">14.64</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.21</td>
    <td align="right">11.14</td>
    <td align="right">11.13</td>
    <td align="right">11.14</td>
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
    <td align="right">4.49</td>
    <td align="right">7.66</td>
    <td align="right">14.88</td>
    <td align="right">13.60</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.01</td>
    <td align="right">6.76</td>
    <td align="right">13.73</td>
    <td align="right">13.04</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.68</td>
    <td align="right">3.60</td>
    <td align="right">3.61</td>
    <td align="right">3.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.57</td>
    <td align="right">14.91</td>
    <td align="right">18.73</td>
    <td align="right">19.55</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.53</td>
    <td align="right">17.49</td>
    <td align="right">18.44</td>
    <td align="right">20.40</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.58</td>
    <td align="right">7.26</td>
    <td align="right">7.24</td>
    <td align="right">7.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.22</td>
    <td align="right">29.46</td>
    <td align="right">24.00</td>
    <td align="right">30.60</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.62</td>
    <td align="right">29.60</td>
    <td align="right">23.68</td>
    <td align="right">30.01</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.27</td>
    <td align="right">16.36</td>
    <td align="right">12.50</td>
    <td align="right">21.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.74</td>
    <td align="right">38.62</td>
    <td align="right">26.52</td>
    <td align="right">38.96</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.83</td>
    <td align="right">40.34</td>
    <td align="right">27.63</td>
    <td align="right">40.02</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.37</td>
    <td align="right">18.36</td>
    <td align="right">13.98</td>
    <td align="right">23.92</td>
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
    <td align="right">4.32</td>
    <td align="right">5.17</td>
    <td align="right">5.14</td>
    <td align="right">5.16</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">5.08</td>
    <td align="right">5.67</td>
    <td align="right">5.71</td>
    <td align="right">5.70</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.57</td>
    <td align="right">3.38</td>
    <td align="right">3.41</td>
    <td align="right">3.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.91</td>
    <td align="right">10.71</td>
    <td align="right">10.71</td>
    <td align="right">10.72</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.20</td>
    <td align="right">11.64</td>
    <td align="right">11.58</td>
    <td align="right">11.60</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.73</td>
    <td align="right">7.41</td>
    <td align="right">7.44</td>
    <td align="right">7.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.34</td>
    <td align="right">22.66</td>
    <td align="right">22.64</td>
    <td align="right">22.64</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.80</td>
    <td align="right">22.59</td>
    <td align="right">22.62</td>
    <td align="right">22.62</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.28</td>
    <td align="right">16.34</td>
    <td align="right">16.33</td>
    <td align="right">16.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.90</td>
    <td align="right">29.69</td>
    <td align="right">29.67</td>
    <td align="right">29.63</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.74</td>
    <td align="right">30.62</td>
    <td align="right">30.62</td>
    <td align="right">30.64</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.37</td>
    <td align="right">18.29</td>
    <td align="right">18.30</td>
    <td align="right">18.29</td>
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
    <td align="right">4.31</td>
    <td align="right">7.52</td>
    <td align="right">16.22</td>
    <td align="right">13.59</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">3.77</td>
    <td align="right">6.54</td>
    <td align="right">14.74</td>
    <td align="right">12.48</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.36</td>
    <td align="right">3.60</td>
    <td align="right">3.55</td>
    <td align="right">3.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">7.68</td>
    <td align="right">14.52</td>
    <td align="right">18.57</td>
    <td align="right">19.27</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">8.77</td>
    <td align="right">16.51</td>
    <td align="right">18.46</td>
    <td align="right">19.59</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.78</td>
    <td align="right">7.42</td>
    <td align="right">7.40</td>
    <td align="right">7.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">17.39</td>
    <td align="right">28.78</td>
    <td align="right">23.49</td>
    <td align="right">29.36</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">17.96</td>
    <td align="right">29.02</td>
    <td align="right">22.73</td>
    <td align="right">29.24</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.86</td>
    <td align="right">15.71</td>
    <td align="right">12.05</td>
    <td align="right">21.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.17</td>
    <td align="right">38.51</td>
    <td align="right">24.97</td>
    <td align="right">38.37</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.49</td>
    <td align="right">40.42</td>
    <td align="right">25.58</td>
    <td align="right">39.67</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.99</td>
    <td align="right">17.56</td>
    <td align="right">13.33</td>
    <td align="right">23.28</td>
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
    <td align="right">4.11</td>
    <td align="right">4.48</td>
    <td align="right">4.49</td>
    <td align="right">4.46</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">3.94</td>
    <td align="right">4.49</td>
    <td align="right">4.51</td>
    <td align="right">4.51</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.62</td>
    <td align="right">3.77</td>
    <td align="right">3.76</td>
    <td align="right">3.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">7.98</td>
    <td align="right">11.99</td>
    <td align="right">11.95</td>
    <td align="right">11.93</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">8.86</td>
    <td align="right">12.20</td>
    <td align="right">12.22</td>
    <td align="right">12.19</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.91</td>
    <td align="right">7.57</td>
    <td align="right">7.55</td>
    <td align="right">7.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">17.48</td>
    <td align="right">26.33</td>
    <td align="right">26.30</td>
    <td align="right">26.78</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.26</td>
    <td align="right">27.65</td>
    <td align="right">27.68</td>
    <td align="right">27.66</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.83</td>
    <td align="right">16.09</td>
    <td align="right">16.10</td>
    <td align="right">16.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.27</td>
    <td align="right">34.53</td>
    <td align="right">34.55</td>
    <td align="right">34.56</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.55</td>
    <td align="right">38.53</td>
    <td align="right">36.85</td>
    <td align="right">36.79</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.07</td>
    <td align="right">18.14</td>
    <td align="right">18.15</td>
    <td align="right">18.15</td>
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
    <td align="right">3.99</td>
    <td align="right">3.79</td>
    <td align="right">3.79</td>
    <td align="right">3.78</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.39</td>
    <td align="right">5.95</td>
    <td align="right">5.96</td>
    <td align="right">5.99</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.06</td>
    <td align="right">6.40</td>
    <td align="right">6.40</td>
    <td align="right">6.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.11</td>
    <td align="right">8.08</td>
    <td align="right">8.09</td>
    <td align="right">8.08</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.76</td>
    <td align="right">10.40</td>
    <td align="right">10.39</td>
    <td align="right">10.40</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">9.96</td>
    <td align="right">11.20</td>
    <td align="right">11.54</td>
    <td align="right">11.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.35</td>
    <td align="right">16.01</td>
    <td align="right">11.82</td>
    <td align="right">20.60</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.86</td>
    <td align="right">21.22</td>
    <td align="right">16.99</td>
    <td align="right">27.28</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.07</td>
    <td align="right">21.45</td>
    <td align="right">17.09</td>
    <td align="right">26.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.56</td>
    <td align="right">18.22</td>
    <td align="right">13.41</td>
    <td align="right">23.12</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.09</td>
    <td align="right">29.49</td>
    <td align="right">20.09</td>
    <td align="right">32.73</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.53</td>
    <td align="right">26.96</td>
    <td align="right">19.38</td>
    <td align="right">31.90</td>
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
    <td align="right">4.34</td>
    <td align="right">4.07</td>
    <td align="right">4.04</td>
    <td align="right">4.03</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.71</td>
    <td align="right">6.28</td>
    <td align="right">6.29</td>
    <td align="right">6.37</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.01</td>
    <td align="right">5.16</td>
    <td align="right">5.11</td>
    <td align="right">5.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.64</td>
    <td align="right">7.64</td>
    <td align="right">7.64</td>
    <td align="right">7.64</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.13</td>
    <td align="right">9.72</td>
    <td align="right">9.76</td>
    <td align="right">9.71</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.60</td>
    <td align="right">11.88</td>
    <td align="right">11.92</td>
    <td align="right">11.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.56</td>
    <td align="right">16.20</td>
    <td align="right">16.17</td>
    <td align="right">16.19</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">20.18</td>
    <td align="right">21.81</td>
    <td align="right">21.82</td>
    <td align="right">21.81</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.70</td>
    <td align="right">21.35</td>
    <td align="right">21.36</td>
    <td align="right">21.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.49</td>
    <td align="right">18.12</td>
    <td align="right">18.10</td>
    <td align="right">18.11</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.53</td>
    <td align="right">30.05</td>
    <td align="right">30.01</td>
    <td align="right">30.03</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.36</td>
    <td align="right">29.24</td>
    <td align="right">29.24</td>
    <td align="right">29.24</td>
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
    <td align="right">3.72</td>
    <td align="right">3.69</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.40</td>
    <td align="right">4.78</td>
    <td align="right">4.82</td>
    <td align="right">4.72</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.40</td>
    <td align="right">5.84</td>
    <td align="right">5.86</td>
    <td align="right">5.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.07</td>
    <td align="right">7.55</td>
    <td align="right">7.54</td>
    <td align="right">7.55</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.27</td>
    <td align="right">9.48</td>
    <td align="right">9.51</td>
    <td align="right">9.50</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">9.65</td>
    <td align="right">11.01</td>
    <td align="right">10.99</td>
    <td align="right">10.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.15</td>
    <td align="right">15.97</td>
    <td align="right">11.83</td>
    <td align="right">20.80</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.41</td>
    <td align="right">19.16</td>
    <td align="right">15.82</td>
    <td align="right">26.37</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.64</td>
    <td align="right">18.98</td>
    <td align="right">15.82</td>
    <td align="right">25.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.30</td>
    <td align="right">17.90</td>
    <td align="right">13.05</td>
    <td align="right">22.82</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.08</td>
    <td align="right">27.06</td>
    <td align="right">18.04</td>
    <td align="right">32.13</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">26.81</td>
    <td align="right">27.06</td>
    <td align="right">18.09</td>
    <td align="right">30.79</td>
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
    <td align="right">3.31</td>
    <td align="right">3.18</td>
    <td align="right">3.19</td>
    <td align="right">3.18</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.71</td>
    <td align="right">5.14</td>
    <td align="right">5.14</td>
    <td align="right">5.16</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.76</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.11</td>
    <td align="right">7.60</td>
    <td align="right">7.62</td>
    <td align="right">7.61</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.36</td>
    <td align="right">9.60</td>
    <td align="right">9.77</td>
    <td align="right">9.60</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">9.65</td>
    <td align="right">10.98</td>
    <td align="right">11.00</td>
    <td align="right">10.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.98</td>
    <td align="right">15.65</td>
    <td align="right">15.70</td>
    <td align="right">15.70</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.26</td>
    <td align="right">21.08</td>
    <td align="right">21.08</td>
    <td align="right">21.09</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.52</td>
    <td align="right">20.53</td>
    <td align="right">22.30</td>
    <td align="right">22.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.36</td>
    <td align="right">17.81</td>
    <td align="right">17.84</td>
    <td align="right">17.85</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">24.97</td>
    <td align="right">27.18</td>
    <td align="right">27.19</td>
    <td align="right">27.18</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">27.08</td>
    <td align="right">27.19</td>
    <td align="right">27.15</td>
    <td align="right">27.19</td>
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
    <td align="right">8.26</td>
    <td align="right">8.53</td>
    <td align="right">16.13</td>
    <td align="right">14.85</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.20</td>
    <td align="right">9.25</td>
    <td align="right">19.45</td>
    <td align="right">17.17</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.08</td>
    <td align="right">13.54</td>
    <td align="right">20.60</td>
    <td align="right">17.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">18.69</td>
    <td align="right">17.06</td>
    <td align="right">18.27</td>
    <td align="right">21.77</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">21.93</td>
    <td align="right">18.24</td>
    <td align="right">19.20</td>
    <td align="right">23.36</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">30.76</td>
    <td align="right">28.58</td>
    <td align="right">26.43</td>
    <td align="right">28.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">29.26</td>
    <td align="right">26.75</td>
    <td align="right">21.40</td>
    <td align="right">29.66</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.33</td>
    <td align="right">32.77</td>
    <td align="right">25.07</td>
    <td align="right">35.20</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.07</td>
    <td align="right">43.20</td>
    <td align="right">30.02</td>
    <td align="right">38.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.14</td>
    <td align="right">35.70</td>
    <td align="right">24.30</td>
    <td align="right">39.66</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.70</td>
    <td align="right">40.35</td>
    <td align="right">26.24</td>
    <td align="right">43.87</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">77.86</td>
    <td align="right">65.67</td>
    <td align="right">39.70</td>
    <td align="right">55.68</td>
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
    <td align="right">8.26</td>
    <td align="right">8.70</td>
    <td align="right">8.68</td>
    <td align="right">8.70</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.66</td>
    <td align="right">9.58</td>
    <td align="right">9.55</td>
    <td align="right">9.52</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.38</td>
    <td align="right">14.28</td>
    <td align="right">14.36</td>
    <td align="right">14.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">18.47</td>
    <td align="right">17.60</td>
    <td align="right">17.64</td>
    <td align="right">17.66</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">24.39</td>
    <td align="right">22.52</td>
    <td align="right">22.46</td>
    <td align="right">22.41</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">31.01</td>
    <td align="right">32.79</td>
    <td align="right">32.81</td>
    <td align="right">32.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.62</td>
    <td align="right">30.48</td>
    <td align="right">30.44</td>
    <td align="right">30.38</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">39.21</td>
    <td align="right">42.26</td>
    <td align="right">42.18</td>
    <td align="right">42.24</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.19</td>
    <td align="right">49.04</td>
    <td align="right">49.11</td>
    <td align="right">49.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.31</td>
    <td align="right">42.50</td>
    <td align="right">42.50</td>
    <td align="right">42.51</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.57</td>
    <td align="right">50.99</td>
    <td align="right">50.91</td>
    <td align="right">51.00</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">77.86</td>
    <td align="right">72.94</td>
    <td align="right">72.69</td>
    <td align="right">72.84</td>
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
    <td align="right">7.58</td>
    <td align="right">8.49</td>
    <td align="right">16.26</td>
    <td align="right">15.00</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.57</td>
    <td align="right">9.20</td>
    <td align="right">19.11</td>
    <td align="right">17.32</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.42</td>
    <td align="right">12.98</td>
    <td align="right">19.46</td>
    <td align="right">17.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.46</td>
    <td align="right">15.97</td>
    <td align="right">17.98</td>
    <td align="right">21.17</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">21.83</td>
    <td align="right">18.68</td>
    <td align="right">18.70</td>
    <td align="right">23.60</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">31.23</td>
    <td align="right">28.07</td>
    <td align="right">23.51</td>
    <td align="right">27.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.83</td>
    <td align="right">26.90</td>
    <td align="right">21.79</td>
    <td align="right">29.66</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.97</td>
    <td align="right">32.52</td>
    <td align="right">24.62</td>
    <td align="right">34.67</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">51.45</td>
    <td align="right">43.92</td>
    <td align="right">23.40</td>
    <td align="right">38.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.51</td>
    <td align="right">40.73</td>
    <td align="right">24.83</td>
    <td align="right">41.72</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.65</td>
    <td align="right">39.82</td>
    <td align="right">26.44</td>
    <td align="right">42.73</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.39</td>
    <td align="right">67.03</td>
    <td align="right">28.75</td>
    <td align="right">56.07</td>
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
    <td align="right">7.71</td>
    <td align="right">5.88</td>
    <td align="right">5.85</td>
    <td align="right">5.88</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.88</td>
    <td align="right">10.28</td>
    <td align="right">10.29</td>
    <td align="right">10.24</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.72</td>
    <td align="right">14.24</td>
    <td align="right">14.15</td>
    <td align="right">14.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.98</td>
    <td align="right">13.14</td>
    <td align="right">13.11</td>
    <td align="right">13.14</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">24.59</td>
    <td align="right">20.94</td>
    <td align="right">20.97</td>
    <td align="right">20.95</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">31.61</td>
    <td align="right">24.49</td>
    <td align="right">24.41</td>
    <td align="right">24.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.09</td>
    <td align="right">19.94</td>
    <td align="right">19.95</td>
    <td align="right">19.92</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.00</td>
    <td align="right">38.50</td>
    <td align="right">38.48</td>
    <td align="right">38.46</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">50.89</td>
    <td align="right">35.75</td>
    <td align="right">36.56</td>
    <td align="right">36.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.57</td>
    <td align="right">24.32</td>
    <td align="right">24.35</td>
    <td align="right">24.30</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.63</td>
    <td align="right">50.92</td>
    <td align="right">50.92</td>
    <td align="right">50.88</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.28</td>
    <td align="right">53.73</td>
    <td align="right">53.33</td>
    <td align="right">53.70</td>
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
    <td align="right">18.67</td>
    <td align="right">2.61</td>
    <td align="right">1.95</td>
    <td align="right">9.34</td>
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
    <td align="right">6.34</td>
    <td align="right">4.15</td>
    <td align="right">11.40</td>
    <td align="right">8.74</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.30</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.62</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.45</td>
    <td align="right">6.08</td>
    <td align="right">11.96</td>
    <td align="right">10.45</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
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
    <td align="right">11.66</td>
    <td align="right">7.33</td>
    <td align="right">11.20</td>
    <td align="right">11.06</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.75</td>
    <td align="right">1.58</td>
    <td align="right">1.59</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.95</td>
    <td align="right">9.30</td>
    <td align="right">11.37</td>
    <td align="right">12.49</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.80</td>
    <td align="right">1.82</td>
    <td align="right">1.81</td>
    <td align="right">1.82</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.79</td>
    <td align="right">1.58</td>
    <td align="right">1.57</td>
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
    <td align="right">3.85</td>
    <td align="right">3.86</td>
    <td align="right">3.86</td>
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
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.42</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="right">5.77</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.71</td>
    <td align="right">1.44</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.71</td>
    <td align="right">7.11</td>
    <td align="right">7.11</td>
    <td align="right">7.11</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
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
    <td align="right">14.90</td>
    <td align="right">9.05</td>
    <td align="right">9.05</td>
    <td align="right">9.03</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="right">1.81</td>
    <td align="right">1.82</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.80</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
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
    <td align="right">3.63</td>
    <td align="right">11.73</td>
    <td align="right">8.28</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.17</td>
    <td align="right">1.14</td>
    <td align="right">1.14</td>
    <td align="right">1.14</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.29</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">8.33</td>
    <td align="right">5.35</td>
    <td align="right">12.36</td>
    <td align="right">9.99</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.32</td>
    <td align="right">1.33</td>
    <td align="right">1.33</td>
    <td align="right">1.33</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.46</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">10.61</td>
    <td align="right">6.66</td>
    <td align="right">11.73</td>
    <td align="right">10.87</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.53</td>
    <td align="right">1.54</td>
    <td align="right">1.55</td>
    <td align="right">1.55</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.65</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">12.66</td>
    <td align="right">8.61</td>
    <td align="right">11.86</td>
    <td align="right">12.24</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.71</td>
    <td align="right">1.76</td>
    <td align="right">1.77</td>
    <td align="right">1.77</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.63</td>
    <td align="right">1.58</td>
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
    <td align="right">5.51</td>
    <td align="right">3.50</td>
    <td align="right">3.50</td>
    <td align="right">3.49</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.20</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.32</td>
    <td align="right">1.21</td>
    <td align="right">1.21</td>
    <td align="right">1.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">8.40</td>
    <td align="right">5.33</td>
    <td align="right">5.33</td>
    <td align="right">5.34</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.34</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.47</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">10.58</td>
    <td align="right">6.62</td>
    <td align="right">6.62</td>
    <td align="right">6.62</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.55</td>
    <td align="right">1.56</td>
    <td align="right">1.56</td>
    <td align="right">1.56</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.64</td>
    <td align="right">1.57</td>
    <td align="right">1.56</td>
    <td align="right">1.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">12.48</td>
    <td align="right">8.46</td>
    <td align="right">8.46</td>
    <td align="right">8.48</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.70</td>
    <td align="right">1.75</td>
    <td align="right">1.74</td>
    <td align="right">1.75</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.60</td>
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
    <td align="right">2.29</td>
    <td align="right">2.58</td>
    <td align="right">9.42</td>
    <td align="right">7.36</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.31</td>
    <td align="right">2.58</td>
    <td align="right">8.86</td>
    <td align="right">7.06</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.02</td>
    <td align="right">1.70</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.19</td>
    <td align="right">3.98</td>
    <td align="right">10.88</td>
    <td align="right">8.78</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.81</td>
    <td align="right">3.59</td>
    <td align="right">9.76</td>
    <td align="right">8.14</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.52</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.05</td>
    <td align="right">4.96</td>
    <td align="right">10.68</td>
    <td align="right">9.52</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">4.87</td>
    <td align="right">10.13</td>
    <td align="right">8.93</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.92</td>
    <td align="right">2.42</td>
    <td align="right">1.76</td>
    <td align="right">11.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.50</td>
    <td align="right">5.61</td>
    <td align="right">10.29</td>
    <td align="right">9.74</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.79</td>
    <td align="right">5.87</td>
    <td align="right">10.28</td>
    <td align="right">9.62</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.91</td>
    <td align="right">2.90</td>
    <td align="right">1.72</td>
    <td align="right">11.48</td>
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
    <td align="right">2.29</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.26</td>
    <td align="right">1.74</td>
    <td align="right">1.75</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.03</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.72</td>
    <td align="right">2.14</td>
    <td align="right">2.19</td>
    <td align="right">2.14</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.51</td>
    <td align="right">1.39</td>
    <td align="right">1.39</td>
    <td align="right">1.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.07</td>
    <td align="right">2.91</td>
    <td align="right">2.91</td>
    <td align="right">2.92</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.04</td>
    <td align="right">3.00</td>
    <td align="right">3.03</td>
    <td align="right">3.03</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.90</td>
    <td align="right">2.34</td>
    <td align="right">2.37</td>
    <td align="right">2.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.62</td>
    <td align="right">3.36</td>
    <td align="right">3.39</td>
    <td align="right">3.37</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.81</td>
    <td align="right">3.59</td>
    <td align="right">3.59</td>
    <td align="right">3.58</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.96</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
    <td align="right">2.91</td>
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
    <td align="right">1.90</td>
    <td align="right">2.54</td>
    <td align="right">9.45</td>
    <td align="right">7.31</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.95</td>
    <td align="right">2.56</td>
    <td align="right">9.04</td>
    <td align="right">6.90</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.62</td>
    <td align="right">1.72</td>
    <td align="right">1.70</td>
    <td align="right">1.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.09</td>
    <td align="right">3.91</td>
    <td align="right">10.73</td>
    <td align="right">8.79</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.53</td>
    <td align="right">3.55</td>
    <td align="right">9.99</td>
    <td align="right">7.97</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.40</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.51</td>
    <td align="right">4.77</td>
    <td align="right">10.61</td>
    <td align="right">9.22</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.52</td>
    <td align="right">4.78</td>
    <td align="right">10.28</td>
    <td align="right">9.31</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.68</td>
    <td align="right">2.48</td>
    <td align="right">1.63</td>
    <td align="right">11.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.21</td>
    <td align="right">5.44</td>
    <td align="right">10.22</td>
    <td align="right">9.58</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.31</td>
    <td align="right">5.78</td>
    <td align="right">10.50</td>
    <td align="right">9.62</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.74</td>
    <td align="right">2.93</td>
    <td align="right">1.60</td>
    <td align="right">11.31</td>
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
    <td align="right">1.91</td>
    <td align="right">1.47</td>
    <td align="right">1.41</td>
    <td align="right">1.42</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.00</td>
    <td align="right">1.53</td>
    <td align="right">1.52</td>
    <td align="right">1.53</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">1.65</td>
    <td align="right">1.71</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.08</td>
    <td align="right">1.83</td>
    <td align="right">1.84</td>
    <td align="right">1.86</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.53</td>
    <td align="right">2.24</td>
    <td align="right">2.18</td>
    <td align="right">2.17</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.41</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.55</td>
    <td align="right">2.67</td>
    <td align="right">2.55</td>
    <td align="right">2.53</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.52</td>
    <td align="right">2.67</td>
    <td align="right">2.67</td>
    <td align="right">2.68</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.68</td>
    <td align="right">2.43</td>
    <td align="right">2.41</td>
    <td align="right">2.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.13</td>
    <td align="right">3.09</td>
    <td align="right">3.19</td>
    <td align="right">3.19</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.45</td>
    <td align="right">3.31</td>
    <td align="right">3.30</td>
    <td align="right">3.27</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.69</td>
    <td align="right">2.92</td>
    <td align="right">2.94</td>
    <td align="right">2.93</td>
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
    <td align="right">1.98</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="right">1.68</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.22</td>
    <td align="right">2.58</td>
    <td align="right">9.47</td>
    <td align="right">7.39</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.32</td>
    <td align="right">2.60</td>
    <td align="right">8.81</td>
    <td align="right">7.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.04</td>
    <td align="right">1.57</td>
    <td align="right">1.61</td>
    <td align="right">1.59</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">3.95</td>
    <td align="right">10.87</td>
    <td align="right">8.77</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.77</td>
    <td align="right">3.60</td>
    <td align="right">9.75</td>
    <td align="right">8.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.85</td>
    <td align="right">2.38</td>
    <td align="right">1.74</td>
    <td align="right">11.26</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.09</td>
    <td align="right">4.96</td>
    <td align="right">10.71</td>
    <td align="right">9.49</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.03</td>
    <td align="right">4.84</td>
    <td align="right">10.11</td>
    <td align="right">8.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.89</td>
    <td align="right">2.88</td>
    <td align="right">1.73</td>
    <td align="right">11.38</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.61</td>
    <td align="right">5.61</td>
    <td align="right">10.29</td>
    <td align="right">9.81</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.65</td>
    <td align="right">5.85</td>
    <td align="right">10.29</td>
    <td align="right">9.60</td>
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
    <td align="right">1.68</td>
    <td align="right">1.67</td>
    <td align="right">1.67</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.30</td>
    <td align="right">1.73</td>
    <td align="right">1.73</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.28</td>
    <td align="right">1.75</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.05</td>
    <td align="right">1.58</td>
    <td align="right">1.59</td>
    <td align="right">1.58</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.17</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.72</td>
    <td align="right">2.15</td>
    <td align="right">2.15</td>
    <td align="right">2.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.86</td>
    <td align="right">2.34</td>
    <td align="right">2.36</td>
    <td align="right">2.33</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.10</td>
    <td align="right">2.91</td>
    <td align="right">2.90</td>
    <td align="right">2.90</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">3.01</td>
    <td align="right">3.01</td>
    <td align="right">3.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.88</td>
    <td align="right">2.81</td>
    <td align="right">2.80</td>
    <td align="right">2.81</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.61</td>
    <td align="right">3.35</td>
    <td align="right">3.34</td>
    <td align="right">3.36</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.72</td>
    <td align="right">3.58</td>
    <td align="right">3.59</td>
    <td align="right">3.57</td>
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
    <td align="right">1.71</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.94</td>
    <td align="right">2.54</td>
    <td align="right">9.42</td>
    <td align="right">7.29</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.95</td>
    <td align="right">2.56</td>
    <td align="right">9.02</td>
    <td align="right">6.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">1.68</td>
    <td align="right">1.44</td>
    <td align="right">1.44</td>
    <td align="right">1.43</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.08</td>
    <td align="right">3.90</td>
    <td align="right">10.70</td>
    <td align="right">8.76</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.61</td>
    <td align="right">3.55</td>
    <td align="right">9.94</td>
    <td align="right">7.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.67</td>
    <td align="right">2.47</td>
    <td align="right">1.61</td>
    <td align="right">11.19</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.62</td>
    <td align="right">4.79</td>
    <td align="right">10.60</td>
    <td align="right">9.22</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.49</td>
    <td align="right">4.77</td>
    <td align="right">10.27</td>
    <td align="right">9.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.71</td>
    <td align="right">2.90</td>
    <td align="right">1.59</td>
    <td align="right">11.26</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.12</td>
    <td align="right">5.43</td>
    <td align="right">10.25</td>
    <td align="right">9.59</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.32</td>
    <td align="right">5.77</td>
    <td align="right">10.47</td>
    <td align="right">9.64</td>
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
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">1.90</td>
    <td align="right">1.42</td>
    <td align="right">1.43</td>
    <td align="right">1.42</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">1.96</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="right">1.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">1.69</td>
    <td align="right">1.47</td>
    <td align="right">1.47</td>
    <td align="right">1.47</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.09</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="right">1.83</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.59</td>
    <td align="right">2.20</td>
    <td align="right">2.21</td>
    <td align="right">2.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.67</td>
    <td align="right">2.43</td>
    <td align="right">2.43</td>
    <td align="right">2.44</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">3.51</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="right">2.65</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">3.52</td>
    <td align="right">2.69</td>
    <td align="right">2.69</td>
    <td align="right">2.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.68</td>
    <td align="right">2.86</td>
    <td align="right">2.86</td>
    <td align="right">2.86</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.25</td>
    <td align="right">3.17</td>
    <td align="right">3.19</td>
    <td align="right">3.17</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.46</td>
    <td align="right">3.34</td>
    <td align="right">3.32</td>
    <td align="right">3.34</td>
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
    <td align="right">3.23</td>
    <td align="right">3.27</td>
    <td align="right">10.27</td>
    <td align="right">8.47</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.96</td>
    <td align="right">3.94</td>
    <td align="right">12.73</td>
    <td align="right">9.37</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.70</td>
    <td align="right">5.18</td>
    <td align="right">13.14</td>
    <td align="right">9.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.38</td>
    <td align="right">4.39</td>
    <td align="right">10.03</td>
    <td align="right">9.67</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.38</td>
    <td align="right">4.51</td>
    <td align="right">10.53</td>
    <td align="right">10.19</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.89</td>
    <td align="right">7.15</td>
    <td align="right">13.55</td>
    <td align="right">11.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.50</td>
    <td align="right">5.24</td>
    <td align="right">9.79</td>
    <td align="right">9.85</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.58</td>
    <td align="right">5.80</td>
    <td align="right">11.30</td>
    <td align="right">10.92</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.11</td>
    <td align="right">7.93</td>
    <td align="right">12.50</td>
    <td align="right">11.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.99</td>
    <td align="right">6.34</td>
    <td align="right">10.28</td>
    <td align="right">10.56</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.43</td>
    <td align="right">6.35</td>
    <td align="right">10.73</td>
    <td align="right">11.42</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.25</td>
    <td align="right">10.89</td>
    <td align="right">14.62</td>
    <td align="right">14.20</td>
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
    <td align="right">2.85</td>
    <td align="right">2.85</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.97</td>
    <td align="right">3.87</td>
    <td align="right">3.84</td>
    <td align="right">3.88</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.68</td>
    <td align="right">4.86</td>
    <td align="right">4.86</td>
    <td align="right">4.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.36</td>
    <td align="right">3.83</td>
    <td align="right">3.82</td>
    <td align="right">3.82</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.42</td>
    <td align="right">4.25</td>
    <td align="right">4.24</td>
    <td align="right">4.27</td>
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
    <td align="right">5.24</td>
    <td align="right">5.24</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.04</td>
    <td align="right">7.53</td>
    <td align="right">7.53</td>
    <td align="right">7.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.98</td>
    <td align="right">5.78</td>
    <td align="right">5.79</td>
    <td align="right">5.79</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.37</td>
    <td align="right">6.02</td>
    <td align="right">6.01</td>
    <td align="right">6.01</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.10</td>
    <td align="right">10.60</td>
    <td align="right">10.60</td>
    <td align="right">10.60</td>
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
    <td align="right">3.24</td>
    <td align="right">10.18</td>
    <td align="right">8.39</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.81</td>
    <td align="right">3.73</td>
    <td align="right">12.71</td>
    <td align="right">9.28</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">6.64</td>
    <td align="right">5.03</td>
    <td align="right">13.33</td>
    <td align="right">9.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.39</td>
    <td align="right">4.39</td>
    <td align="right">10.07</td>
    <td align="right">9.25</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.29</td>
    <td align="right">4.51</td>
    <td align="right">10.41</td>
    <td align="right">10.12</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">9.64</td>
    <td align="right">6.91</td>
    <td align="right">13.59</td>
    <td align="right">11.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.46</td>
    <td align="right">5.24</td>
    <td align="right">9.79</td>
    <td align="right">10.01</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.51</td>
    <td align="right">5.78</td>
    <td align="right">11.27</td>
    <td align="right">11.08</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">10.70</td>
    <td align="right">7.71</td>
    <td align="right">12.07</td>
    <td align="right">11.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.04</td>
    <td align="right">6.32</td>
    <td align="right">10.26</td>
    <td align="right">10.74</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.48</td>
    <td align="right">6.39</td>
    <td align="right">10.78</td>
    <td align="right">11.71</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">15.08</td>
    <td align="right">11.07</td>
    <td align="right">13.36</td>
    <td align="right">13.43</td>
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
    <td align="right">3.20</td>
    <td align="right">2.85</td>
    <td align="right">2.84</td>
    <td align="right">2.83</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.80</td>
    <td align="right">3.67</td>
    <td align="right">3.66</td>
    <td align="right">3.67</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">6.61</td>
    <td align="right">4.83</td>
    <td align="right">4.82</td>
    <td align="right">4.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.36</td>
    <td align="right">3.83</td>
    <td align="right">3.82</td>
    <td align="right">3.81</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.56</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="right">4.21</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">9.61</td>
    <td align="right">6.60</td>
    <td align="right">6.60</td>
    <td align="right">6.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.43</td>
    <td align="right">4.54</td>
    <td align="right">4.55</td>
    <td align="right">4.54</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.40</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">10.66</td>
    <td align="right">7.49</td>
    <td align="right">7.49</td>
    <td align="right">7.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.97</td>
    <td align="right">5.77</td>
    <td align="right">5.78</td>
    <td align="right">5.78</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.44</td>
    <td align="right">6.07</td>
    <td align="right">6.08</td>
    <td align="right">6.04</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">14.97</td>
    <td align="right">10.92</td>
    <td align="right">10.91</td>
    <td align="right">10.91</td>
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
    <td align="right">23.67</td>
    <td align="right">10.91</td>
    <td align="right">6.00</td>
    <td align="right">15.39</td>
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
    <td align="right">7.73</td>
    <td align="right">6.19</td>
    <td align="right">12.98</td>
    <td align="right">10.46</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.05</td>
    <td align="right">1.99</td>
    <td align="right">1.98</td>
    <td align="right">2.02</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.09</td>
    <td align="right">2.02</td>
    <td align="right">2.05</td>
    <td align="right">2.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.73</td>
    <td align="right">11.48</td>
    <td align="right">16.31</td>
    <td align="right">15.12</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.44</td>
    <td align="right">3.40</td>
    <td align="right">3.48</td>
    <td align="right">3.46</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.57</td>
    <td align="right">3.39</td>
    <td align="right">3.24</td>
    <td align="right">3.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">29.98</td>
    <td align="right">22.99</td>
    <td align="right">18.01</td>
    <td align="right">22.31</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">6.90</td>
    <td align="right">6.74</td>
    <td align="right">6.53</td>
    <td align="right">6.45</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.73</td>
    <td align="right">6.05</td>
    <td align="right">5.90</td>
    <td align="right">6.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">54.33</td>
    <td align="right">40.00</td>
    <td align="right">20.44</td>
    <td align="right">31.47</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.19</td>
    <td align="right">8.33</td>
    <td align="right">8.19</td>
    <td align="right">7.76</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.55</td>
    <td align="right">6.68</td>
    <td align="right">6.44</td>
    <td align="right">6.72</td>
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
    <td align="right">7.73</td>
    <td align="right">6.46</td>
    <td align="right">6.46</td>
    <td align="right">6.49</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.03</td>
    <td align="right">1.97</td>
    <td align="right">2.02</td>
    <td align="right">2.03</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.11</td>
    <td align="right">2.05</td>
    <td align="right">2.06</td>
    <td align="right">2.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.29</td>
    <td align="right">12.36</td>
    <td align="right">12.78</td>
    <td align="right">13.05</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.61</td>
    <td align="right">3.58</td>
    <td align="right">3.59</td>
    <td align="right">3.41</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.34</td>
    <td align="right">3.27</td>
    <td align="right">3.37</td>
    <td align="right">3.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">30.74</td>
    <td align="right">27.75</td>
    <td align="right">27.51</td>
    <td align="right">27.85</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">7.72</td>
    <td align="right">6.66</td>
    <td align="right">6.26</td>
    <td align="right">6.69</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.99</td>
    <td align="right">6.17</td>
    <td align="right">6.09</td>
    <td align="right">6.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">54.81</td>
    <td align="right">46.39</td>
    <td align="right">43.59</td>
    <td align="right">41.34</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.34</td>
    <td align="right">7.42</td>
    <td align="right">7.41</td>
    <td align="right">7.40</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">6.97</td>
    <td align="right">5.96</td>
    <td align="right">5.98</td>
    <td align="right">5.96</td>
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
    <td align="right">6.57</td>
    <td align="right">5.37</td>
    <td align="right">13.31</td>
    <td align="right">9.75</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.87</td>
    <td align="right">1.85</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.86</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">10.93</td>
    <td align="right">9.60</td>
    <td align="right">16.49</td>
    <td align="right">13.94</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.09</td>
    <td align="right">2.99</td>
    <td align="right">3.06</td>
    <td align="right">3.03</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.11</td>
    <td align="right">3.06</td>
    <td align="right">3.06</td>
    <td align="right">3.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">24.48</td>
    <td align="right">20.22</td>
    <td align="right">18.79</td>
    <td align="right">19.56</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">5.95</td>
    <td align="right">5.90</td>
    <td align="right">5.72</td>
    <td align="right">5.78</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.03</td>
    <td align="right">5.75</td>
    <td align="right">5.76</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">45.64</td>
    <td align="right">32.48</td>
    <td align="right">21.32</td>
    <td align="right">27.53</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.26</td>
    <td align="right">7.33</td>
    <td align="right">7.30</td>
    <td align="right">7.33</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">6.98</td>
    <td align="right">6.14</td>
    <td align="right">6.18</td>
    <td align="right">6.15</td>
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
    <td align="right">6.57</td>
    <td align="right">5.71</td>
    <td align="right">5.71</td>
    <td align="right">5.70</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">1.87</td>
    <td align="right">1.85</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">1.86</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">10.94</td>
    <td align="right">10.67</td>
    <td align="right">10.70</td>
    <td align="right">10.61</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">2.99</td>
    <td align="right">3.02</td>
    <td align="right">2.99</td>
    <td align="right">2.98</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.05</td>
    <td align="right">3.02</td>
    <td align="right">3.03</td>
    <td align="right">3.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">24.02</td>
    <td align="right">22.60</td>
    <td align="right">22.56</td>
    <td align="right">22.58</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">5.94</td>
    <td align="right">5.73</td>
    <td align="right">5.65</td>
    <td align="right">5.69</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">5.91</td>
    <td align="right">5.69</td>
    <td align="right">5.65</td>
    <td align="right">5.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">45.47</td>
    <td align="right">38.25</td>
    <td align="right">38.21</td>
    <td align="right">38.21</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">8.16</td>
    <td align="right">7.27</td>
    <td align="right">7.26</td>
    <td align="right">7.24</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">6.93</td>
    <td align="right">6.10</td>
    <td align="right">6.12</td>
    <td align="right">6.09</td>
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
    <td align="right">2.67</td>
    <td align="right">3.39</td>
    <td align="right">10.19</td>
    <td align="right">8.36</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.69</td>
    <td align="right">3.42</td>
    <td align="right">9.69</td>
    <td align="right">8.05</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.37</td>
    <td align="right">2.49</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.65</td>
    <td align="right">6.49</td>
    <td align="right">13.28</td>
    <td align="right">11.99</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.09</td>
    <td align="right">6.49</td>
    <td align="right">11.86</td>
    <td align="right">11.17</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.58</td>
    <td align="right">3.18</td>
    <td align="right">3.19</td>
    <td align="right">3.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.58</td>
    <td align="right">12.44</td>
    <td align="right">14.69</td>
    <td align="right">15.73</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.59</td>
    <td align="right">12.50</td>
    <td align="right">14.13</td>
    <td align="right">15.39</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.42</td>
    <td align="right">7.48</td>
    <td align="right">4.96</td>
    <td align="right">14.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.11</td>
    <td align="right">16.78</td>
    <td align="right">15.26</td>
    <td align="right">19.17</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.57</td>
    <td align="right">17.58</td>
    <td align="right">15.76</td>
    <td align="right">19.85</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.30</td>
    <td align="right">10.09</td>
    <td align="right">5.96</td>
    <td align="right">16.03</td>
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
    <td align="right">2.50</td>
    <td align="right">2.51</td>
    <td align="right">2.50</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.70</td>
    <td align="right">2.56</td>
    <td align="right">2.57</td>
    <td align="right">2.56</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.37</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
    <td align="right">2.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.63</td>
    <td align="right">3.95</td>
    <td align="right">3.91</td>
    <td align="right">3.87</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.08</td>
    <td align="right">4.54</td>
    <td align="right">4.43</td>
    <td align="right">4.41</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.57</td>
    <td align="right">3.20</td>
    <td align="right">3.20</td>
    <td align="right">3.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.59</td>
    <td align="right">8.91</td>
    <td align="right">8.87</td>
    <td align="right">8.90</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.66</td>
    <td align="right">8.80</td>
    <td align="right">8.82</td>
    <td align="right">8.82</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.36</td>
    <td align="right">7.49</td>
    <td align="right">7.51</td>
    <td align="right">7.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.13</td>
    <td align="right">11.79</td>
    <td align="right">11.79</td>
    <td align="right">11.81</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.60</td>
    <td align="right">12.53</td>
    <td align="right">12.52</td>
    <td align="right">12.51</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.30</td>
    <td align="right">10.19</td>
    <td align="right">10.19</td>
    <td align="right">10.19</td>
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
    <td align="right">3.33</td>
    <td align="right">10.28</td>
    <td align="right">8.31</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.36</td>
    <td align="right">3.41</td>
    <td align="right">9.93</td>
    <td align="right">7.93</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">1.99</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.57</td>
    <td align="right">6.46</td>
    <td align="right">13.13</td>
    <td align="right">11.90</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.18</td>
    <td align="right">6.57</td>
    <td align="right">12.11</td>
    <td align="right">11.04</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.54</td>
    <td align="right">3.20</td>
    <td align="right">3.19</td>
    <td align="right">3.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.67</td>
    <td align="right">12.38</td>
    <td align="right">15.01</td>
    <td align="right">15.64</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.81</td>
    <td align="right">12.61</td>
    <td align="right">14.57</td>
    <td align="right">15.75</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.17</td>
    <td align="right">7.87</td>
    <td align="right">5.44</td>
    <td align="right">14.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.87</td>
    <td align="right">16.54</td>
    <td align="right">15.15</td>
    <td align="right">18.91</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.59</td>
    <td align="right">18.05</td>
    <td align="right">15.94</td>
    <td align="right">19.70</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.33</td>
    <td align="right">10.64</td>
    <td align="right">6.57</td>
    <td align="right">16.15</td>
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
    <td align="right">2.29</td>
    <td align="right">2.33</td>
    <td align="right">2.34</td>
    <td align="right">2.33</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.36</td>
    <td align="right">2.45</td>
    <td align="right">2.45</td>
    <td align="right">2.44</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">1.98</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.55</td>
    <td align="right">3.90</td>
    <td align="right">3.85</td>
    <td align="right">3.87</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.19</td>
    <td align="right">4.77</td>
    <td align="right">4.66</td>
    <td align="right">4.65</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.54</td>
    <td align="right">3.18</td>
    <td align="right">3.18</td>
    <td align="right">3.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.68</td>
    <td align="right">8.91</td>
    <td align="right">9.05</td>
    <td align="right">8.89</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.78</td>
    <td align="right">8.88</td>
    <td align="right">8.89</td>
    <td align="right">8.92</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.20</td>
    <td align="right">7.87</td>
    <td align="right">7.90</td>
    <td align="right">7.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.94</td>
    <td align="right">12.16</td>
    <td align="right">12.16</td>
    <td align="right">12.17</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.63</td>
    <td align="right">12.74</td>
    <td align="right">12.76</td>
    <td align="right">12.77</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.32</td>
    <td align="right">10.75</td>
    <td align="right">10.73</td>
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
    <td align="right">2.35</td>
    <td align="right">2.48</td>
    <td align="right">2.48</td>
    <td align="right">2.48</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.68</td>
    <td align="right">3.39</td>
    <td align="right">10.19</td>
    <td align="right">8.38</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.69</td>
    <td align="right">3.43</td>
    <td align="right">9.69</td>
    <td align="right">8.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.84</td>
    <td align="right">3.08</td>
    <td align="right">3.07</td>
    <td align="right">3.04</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.63</td>
    <td align="right">6.48</td>
    <td align="right">13.28</td>
    <td align="right">12.00</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.09</td>
    <td align="right">6.51</td>
    <td align="right">11.86</td>
    <td align="right">11.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.37</td>
    <td align="right">7.46</td>
    <td align="right">5.12</td>
    <td align="right">14.11</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.61</td>
    <td align="right">12.43</td>
    <td align="right">14.69</td>
    <td align="right">15.73</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.55</td>
    <td align="right">12.47</td>
    <td align="right">14.14</td>
    <td align="right">15.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.38</td>
    <td align="right">10.14</td>
    <td align="right">5.96</td>
    <td align="right">15.82</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.11</td>
    <td align="right">16.77</td>
    <td align="right">15.25</td>
    <td align="right">19.13</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.58</td>
    <td align="right">17.59</td>
    <td align="right">15.75</td>
    <td align="right">19.85</td>
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
    <td align="right">2.48</td>
    <td align="right">2.48</td>
    <td align="right">2.48</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.68</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.70</td>
    <td align="right">2.57</td>
    <td align="right">2.57</td>
    <td align="right">2.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.83</td>
    <td align="right">3.08</td>
    <td align="right">3.04</td>
    <td align="right">3.02</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.64</td>
    <td align="right">3.90</td>
    <td align="right">3.91</td>
    <td align="right">3.87</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.08</td>
    <td align="right">4.62</td>
    <td align="right">4.40</td>
    <td align="right">4.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.38</td>
    <td align="right">7.50</td>
    <td align="right">7.48</td>
    <td align="right">7.49</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.59</td>
    <td align="right">8.90</td>
    <td align="right">8.92</td>
    <td align="right">8.91</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.58</td>
    <td align="right">8.83</td>
    <td align="right">8.86</td>
    <td align="right">8.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.43</td>
    <td align="right">10.29</td>
    <td align="right">10.26</td>
    <td align="right">10.29</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.16</td>
    <td align="right">11.82</td>
    <td align="right">11.82</td>
    <td align="right">11.80</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.60</td>
    <td align="right">12.55</td>
    <td align="right">12.52</td>
    <td align="right">12.51</td>
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
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.28</td>
    <td align="right">3.34</td>
    <td align="right">10.26</td>
    <td align="right">8.32</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.36</td>
    <td align="right">3.42</td>
    <td align="right">9.94</td>
    <td align="right">7.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.68</td>
    <td align="right">3.26</td>
    <td align="right">3.23</td>
    <td align="right">3.25</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.58</td>
    <td align="right">6.46</td>
    <td align="right">13.15</td>
    <td align="right">11.90</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.19</td>
    <td align="right">6.58</td>
    <td align="right">12.13</td>
    <td align="right">11.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.32</td>
    <td align="right">7.99</td>
    <td align="right">5.49</td>
    <td align="right">14.14</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.68</td>
    <td align="right">12.48</td>
    <td align="right">15.02</td>
    <td align="right">15.62</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.80</td>
    <td align="right">12.64</td>
    <td align="right">14.56</td>
    <td align="right">15.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.63</td>
    <td align="right">10.87</td>
    <td align="right">6.72</td>
    <td align="right">15.93</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.91</td>
    <td align="right">16.54</td>
    <td align="right">15.16</td>
    <td align="right">18.92</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.60</td>
    <td align="right">18.06</td>
    <td align="right">15.95</td>
    <td align="right">19.72</td>
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
    <td align="right">2.54</td>
    <td align="right">2.55</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.28</td>
    <td align="right">2.33</td>
    <td align="right">2.33</td>
    <td align="right">2.34</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.36</td>
    <td align="right">2.44</td>
    <td align="right">2.44</td>
    <td align="right">2.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.67</td>
    <td align="right">3.25</td>
    <td align="right">3.23</td>
    <td align="right">3.23</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.60</td>
    <td align="right">4.13</td>
    <td align="right">3.90</td>
    <td align="right">3.88</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.19</td>
    <td align="right">4.82</td>
    <td align="right">4.69</td>
    <td align="right">4.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.30</td>
    <td align="right">7.94</td>
    <td align="right">7.93</td>
    <td align="right">7.95</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">8.70</td>
    <td align="right">8.85</td>
    <td align="right">8.87</td>
    <td align="right">8.88</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">8.82</td>
    <td align="right">8.91</td>
    <td align="right">8.93</td>
    <td align="right">8.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.63</td>
    <td align="right">10.98</td>
    <td align="right">10.96</td>
    <td align="right">10.95</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">12.88</td>
    <td align="right">12.19</td>
    <td align="right">12.17</td>
    <td align="right">12.17</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.57</td>
    <td align="right">12.76</td>
    <td align="right">12.76</td>
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
    <td align="right">4.53</td>
    <td align="right">4.27</td>
    <td align="right">11.26</td>
    <td align="right">9.78</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.70</td>
    <td align="right">4.87</td>
    <td align="right">13.53</td>
    <td align="right">10.47</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">8.93</td>
    <td align="right">6.72</td>
    <td align="right">14.62</td>
    <td align="right">11.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.03</td>
    <td align="right">7.27</td>
    <td align="right">12.12</td>
    <td align="right">12.97</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.28</td>
    <td align="right">7.60</td>
    <td align="right">12.49</td>
    <td align="right">13.50</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.13</td>
    <td align="right">11.46</td>
    <td align="right">17.43</td>
    <td align="right">14.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.18</td>
    <td align="right">12.19</td>
    <td align="right">13.51</td>
    <td align="right">16.18</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">20.62</td>
    <td align="right">14.12</td>
    <td align="right">15.79</td>
    <td align="right">18.56</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">23.33</td>
    <td align="right">18.86</td>
    <td align="right">18.15</td>
    <td align="right">19.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.50</td>
    <td align="right">16.22</td>
    <td align="right">15.02</td>
    <td align="right">19.81</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.09</td>
    <td align="right">18.94</td>
    <td align="right">16.34</td>
    <td align="right">22.65</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.59</td>
    <td align="right">34.32</td>
    <td align="right">26.62</td>
    <td align="right">31.61</td>
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
    <td align="right">4.54</td>
    <td align="right">4.17</td>
    <td align="right">4.18</td>
    <td align="right">4.17</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.73</td>
    <td align="right">5.11</td>
    <td align="right">5.13</td>
    <td align="right">5.13</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">8.94</td>
    <td align="right">6.79</td>
    <td align="right">6.80</td>
    <td align="right">6.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.02</td>
    <td align="right">7.61</td>
    <td align="right">7.57</td>
    <td align="right">7.58</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.23</td>
    <td align="right">7.92</td>
    <td align="right">7.91</td>
    <td align="right">7.89</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.11</td>
    <td align="right">11.90</td>
    <td align="right">11.86</td>
    <td align="right">11.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.20</td>
    <td align="right">13.04</td>
    <td align="right">12.99</td>
    <td align="right">13.00</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">20.64</td>
    <td align="right">15.04</td>
    <td align="right">15.05</td>
    <td align="right">15.01</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">23.29</td>
    <td align="right">20.12</td>
    <td align="right">20.11</td>
    <td align="right">20.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.57</td>
    <td align="right">17.79</td>
    <td align="right">17.77</td>
    <td align="right">17.79</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.07</td>
    <td align="right">20.58</td>
    <td align="right">20.61</td>
    <td align="right">20.61</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.63</td>
    <td align="right">35.52</td>
    <td align="right">35.54</td>
    <td align="right">35.54</td>
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
    <td align="right">4.60</td>
    <td align="right">4.25</td>
    <td align="right">11.23</td>
    <td align="right">9.73</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.58</td>
    <td align="right">4.74</td>
    <td align="right">13.44</td>
    <td align="right">10.42</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">7.90</td>
    <td align="right">6.49</td>
    <td align="right">14.75</td>
    <td align="right">11.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.34</td>
    <td align="right">7.31</td>
    <td align="right">12.11</td>
    <td align="right">12.57</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.40</td>
    <td align="right">7.69</td>
    <td align="right">12.32</td>
    <td align="right">13.46</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">12.80</td>
    <td align="right">11.25</td>
    <td align="right">16.60</td>
    <td align="right">14.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.60</td>
    <td align="right">12.15</td>
    <td align="right">13.48</td>
    <td align="right">16.22</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">21.02</td>
    <td align="right">14.52</td>
    <td align="right">15.54</td>
    <td align="right">18.68</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">21.84</td>
    <td align="right">18.99</td>
    <td align="right">15.54</td>
    <td align="right">19.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.69</td>
    <td align="right">16.20</td>
    <td align="right">14.96</td>
    <td align="right">19.86</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.90</td>
    <td align="right">19.51</td>
    <td align="right">16.24</td>
    <td align="right">23.10</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.39</td>
    <td align="right">35.26</td>
    <td align="right">17.53</td>
    <td align="right">30.74</td>
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
    <td align="right">4.61</td>
    <td align="right">4.17</td>
    <td align="right">4.16</td>
    <td align="right">4.16</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.58</td>
    <td align="right">4.99</td>
    <td align="right">5.00</td>
    <td align="right">5.00</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">7.90</td>
    <td align="right">6.41</td>
    <td align="right">6.42</td>
    <td align="right">6.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.32</td>
    <td align="right">7.62</td>
    <td align="right">7.61</td>
    <td align="right">7.60</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.01</td>
    <td align="right">8.19</td>
    <td align="right">8.07</td>
    <td align="right">8.04</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">12.79</td>
    <td align="right">11.90</td>
    <td align="right">11.81</td>
    <td align="right">11.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.56</td>
    <td align="right">13.03</td>
    <td align="right">13.07</td>
    <td align="right">13.00</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">21.10</td>
    <td align="right">15.42</td>
    <td align="right">15.38</td>
    <td align="right">15.39</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">21.89</td>
    <td align="right">20.50</td>
    <td align="right">20.53</td>
    <td align="right">20.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.74</td>
    <td align="right">17.79</td>
    <td align="right">17.81</td>
    <td align="right">17.80</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.90</td>
    <td align="right">21.17</td>
    <td align="right">21.19</td>
    <td align="right">21.13</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.34</td>
    <td align="right">36.81</td>
    <td align="right">36.89</td>
    <td align="right">36.81</td>
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
    <td align="right">25.85</td>
    <td align="right">5.30</td>
    <td align="right">3.50</td>
    <td align="right">9.98</td>
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
    <td align="right">10.26</td>
    <td align="right">11.34</td>
    <td align="right">14.36</td>
    <td align="right">13.92</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.84</td>
    <td align="right">3.62</td>
    <td align="right">3.62</td>
    <td align="right">3.61</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.35</td>
    <td align="right">4.15</td>
    <td align="right">4.15</td>
    <td align="right">4.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.06</td>
    <td align="right">16.09</td>
    <td align="right">14.96</td>
    <td align="right">16.96</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.40</td>
    <td align="right">4.07</td>
    <td align="right">4.03</td>
    <td align="right">4.01</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.01</td>
    <td align="right">4.78</td>
    <td align="right">4.76</td>
    <td align="right">4.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.17</td>
    <td align="right">20.50</td>
    <td align="right">14.07</td>
    <td align="right">19.42</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.07</td>
    <td align="right">4.40</td>
    <td align="right">4.39</td>
    <td align="right">4.39</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.71</td>
    <td align="right">5.15</td>
    <td align="right">5.15</td>
    <td align="right">5.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.77</td>
    <td align="right">25.06</td>
    <td align="right">14.50</td>
    <td align="right">22.24</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.72</td>
    <td align="right">4.77</td>
    <td align="right">4.76</td>
    <td align="right">4.75</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.31</td>
    <td align="right">5.60</td>
    <td align="right">5.59</td>
    <td align="right">5.57</td>
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
    <td align="right">10.23</td>
    <td align="right">12.53</td>
    <td align="right">12.56</td>
    <td align="right">12.57</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.82</td>
    <td align="right">3.62</td>
    <td align="right">3.63</td>
    <td align="right">3.62</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.35</td>
    <td align="right">4.13</td>
    <td align="right">4.15</td>
    <td align="right">4.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">18.09</td>
    <td align="right">18.40</td>
    <td align="right">18.37</td>
    <td align="right">18.24</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.42</td>
    <td align="right">4.06</td>
    <td align="right">4.04</td>
    <td align="right">4.03</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.01</td>
    <td align="right">4.79</td>
    <td align="right">4.74</td>
    <td align="right">4.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.18</td>
    <td align="right">22.53</td>
    <td align="right">22.21</td>
    <td align="right">22.25</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.05</td>
    <td align="right">4.41</td>
    <td align="right">4.40</td>
    <td align="right">4.39</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.68</td>
    <td align="right">5.17</td>
    <td align="right">5.15</td>
    <td align="right">5.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.76</td>
    <td align="right">27.82</td>
    <td align="right">27.66</td>
    <td align="right">27.67</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.72</td>
    <td align="right">4.79</td>
    <td align="right">4.77</td>
    <td align="right">4.76</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.31</td>
    <td align="right">5.58</td>
    <td align="right">5.58</td>
    <td align="right">5.57</td>
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
    <td align="right">10.17</td>
    <td align="right">11.68</td>
    <td align="right">15.39</td>
    <td align="right">13.99</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.87</td>
    <td align="right">3.61</td>
    <td align="right">3.60</td>
    <td align="right">3.61</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.39</td>
    <td align="right">4.16</td>
    <td align="right">4.16</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.03</td>
    <td align="right">16.74</td>
    <td align="right">16.51</td>
    <td align="right">17.27</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.51</td>
    <td align="right">4.04</td>
    <td align="right">4.02</td>
    <td align="right">4.01</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.02</td>
    <td align="right">4.80</td>
    <td align="right">4.77</td>
    <td align="right">4.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.09</td>
    <td align="right">21.32</td>
    <td align="right">15.81</td>
    <td align="right">20.41</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.14</td>
    <td align="right">4.37</td>
    <td align="right">4.36</td>
    <td align="right">4.36</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.65</td>
    <td align="right">5.20</td>
    <td align="right">5.20</td>
    <td align="right">5.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.52</td>
    <td align="right">26.26</td>
    <td align="right">15.74</td>
    <td align="right">22.88</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.81</td>
    <td align="right">4.72</td>
    <td align="right">4.69</td>
    <td align="right">4.72</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.26</td>
    <td align="right">5.64</td>
    <td align="right">5.61</td>
    <td align="right">5.61</td>
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
    <td align="right">10.15</td>
    <td align="right">12.71</td>
    <td align="right">12.74</td>
    <td align="right">12.75</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.87</td>
    <td align="right">3.60</td>
    <td align="right">3.60</td>
    <td align="right">3.60</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.39</td>
    <td align="right">4.17</td>
    <td align="right">4.16</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.01</td>
    <td align="right">18.88</td>
    <td align="right">18.77</td>
    <td align="right">18.69</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.50</td>
    <td align="right">4.04</td>
    <td align="right">4.03</td>
    <td align="right">4.00</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.01</td>
    <td align="right">4.77</td>
    <td align="right">4.72</td>
    <td align="right">4.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.12</td>
    <td align="right">23.24</td>
    <td align="right">23.26</td>
    <td align="right">23.00</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.13</td>
    <td align="right">4.37</td>
    <td align="right">4.37</td>
    <td align="right">4.37</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.64</td>
    <td align="right">5.19</td>
    <td align="right">5.16</td>
    <td align="right">5.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.58</td>
    <td align="right">28.53</td>
    <td align="right">28.41</td>
    <td align="right">28.44</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.80</td>
    <td align="right">4.72</td>
    <td align="right">4.72</td>
    <td align="right">4.72</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.26</td>
    <td align="right">5.64</td>
    <td align="right">5.63</td>
    <td align="right">5.61</td>
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
    <td align="right">5.40</td>
    <td align="right">6.76</td>
    <td align="right">11.09</td>
    <td align="right">10.62</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">8.35</td>
    <td align="right">7.33</td>
    <td align="right">12.04</td>
    <td align="right">11.64</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.85</td>
    <td align="right">2.19</td>
    <td align="right">2.19</td>
    <td align="right">2.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.24</td>
    <td align="right">9.54</td>
    <td align="right">11.60</td>
    <td align="right">12.46</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.71</td>
    <td align="right">11.03</td>
    <td align="right">13.01</td>
    <td align="right">14.00</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.73</td>
    <td align="right">2.99</td>
    <td align="right">2.40</td>
    <td align="right">8.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.55</td>
    <td align="right">13.11</td>
    <td align="right">13.82</td>
    <td align="right">15.53</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.41</td>
    <td align="right">13.80</td>
    <td align="right">15.14</td>
    <td align="right">16.22</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.30</td>
    <td align="right">4.46</td>
    <td align="right">3.10</td>
    <td align="right">11.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.65</td>
    <td align="right">14.23</td>
    <td align="right">13.51</td>
    <td align="right">16.41</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.84</td>
    <td align="right">18.52</td>
    <td align="right">15.76</td>
    <td align="right">20.34</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.35</td>
    <td align="right">4.48</td>
    <td align="right">3.10</td>
    <td align="right">11.28</td>
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
    <td align="right">5.40</td>
    <td align="right">4.30</td>
    <td align="right">4.31</td>
    <td align="right">4.30</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">8.36</td>
    <td align="right">4.62</td>
    <td align="right">4.63</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.85</td>
    <td align="right">2.19</td>
    <td align="right">2.18</td>
    <td align="right">2.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.26</td>
    <td align="right">7.03</td>
    <td align="right">6.96</td>
    <td align="right">6.89</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.70</td>
    <td align="right">7.03</td>
    <td align="right">7.02</td>
    <td align="right">7.00</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.80</td>
    <td align="right">2.09</td>
    <td align="right">2.09</td>
    <td align="right">2.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.54</td>
    <td align="right">9.21</td>
    <td align="right">9.18</td>
    <td align="right">9.16</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.33</td>
    <td align="right">10.26</td>
    <td align="right">10.33</td>
    <td align="right">10.45</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.28</td>
    <td align="right">3.48</td>
    <td align="right">3.46</td>
    <td align="right">3.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.63</td>
    <td align="right">10.39</td>
    <td align="right">10.33</td>
    <td align="right">10.34</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.80</td>
    <td align="right">12.25</td>
    <td align="right">12.23</td>
    <td align="right">12.20</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.31</td>
    <td align="right">3.49</td>
    <td align="right">3.48</td>
    <td align="right">3.47</td>
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
    <td align="right">5.39</td>
    <td align="right">6.81</td>
    <td align="right">11.19</td>
    <td align="right">10.90</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">8.46</td>
    <td align="right">7.39</td>
    <td align="right">12.03</td>
    <td align="right">11.48</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.81</td>
    <td align="right">2.11</td>
    <td align="right">2.12</td>
    <td align="right">2.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.12</td>
    <td align="right">9.76</td>
    <td align="right">11.97</td>
    <td align="right">12.30</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.50</td>
    <td align="right">11.26</td>
    <td align="right">13.04</td>
    <td align="right">13.87</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.75</td>
    <td align="right">2.91</td>
    <td align="right">2.34</td>
    <td align="right">8.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.48</td>
    <td align="right">13.18</td>
    <td align="right">14.03</td>
    <td align="right">15.58</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.36</td>
    <td align="right">13.94</td>
    <td align="right">15.04</td>
    <td align="right">16.26</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.32</td>
    <td align="right">4.44</td>
    <td align="right">3.10</td>
    <td align="right">11.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.69</td>
    <td align="right">14.61</td>
    <td align="right">13.66</td>
    <td align="right">16.95</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.96</td>
    <td align="right">18.27</td>
    <td align="right">15.57</td>
    <td align="right">20.08</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.34</td>
    <td align="right">4.46</td>
    <td align="right">3.08</td>
    <td align="right">11.25</td>
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
    <td align="right">4.31</td>
    <td align="right">4.31</td>
    <td align="right">4.32</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">8.48</td>
    <td align="right">4.75</td>
    <td align="right">4.78</td>
    <td align="right">4.75</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.83</td>
    <td align="right">2.12</td>
    <td align="right">2.13</td>
    <td align="right">2.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.17</td>
    <td align="right">7.01</td>
    <td align="right">6.98</td>
    <td align="right">6.93</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.54</td>
    <td align="right">7.03</td>
    <td align="right">6.99</td>
    <td align="right">6.94</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">2.01</td>
    <td align="right">2.00</td>
    <td align="right">1.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.51</td>
    <td align="right">9.16</td>
    <td align="right">8.97</td>
    <td align="right">8.97</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.39</td>
    <td align="right">10.16</td>
    <td align="right">10.29</td>
    <td align="right">10.41</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.31</td>
    <td align="right">3.41</td>
    <td align="right">3.40</td>
    <td align="right">3.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.64</td>
    <td align="right">10.31</td>
    <td align="right">10.27</td>
    <td align="right">10.19</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.89</td>
    <td align="right">12.25</td>
    <td align="right">12.23</td>
    <td align="right">12.23</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.34</td>
    <td align="right">3.41</td>
    <td align="right">3.40</td>
    <td align="right">3.40</td>
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
    <td align="right">2.05</td>
    <td align="right">2.05</td>
    <td align="right">2.05</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.72</td>
    <td align="right">3.27</td>
    <td align="right">3.26</td>
    <td align="right">3.26</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.78</td>
    <td align="right">3.14</td>
    <td align="right">3.14</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.24</td>
    <td align="right">3.44</td>
    <td align="right">2.76</td>
    <td align="right">9.47</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.18</td>
    <td align="right">3.89</td>
    <td align="right">3.26</td>
    <td align="right">10.44</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.69</td>
    <td align="right">4.69</td>
    <td align="right">4.00</td>
    <td align="right">10.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.38</td>
    <td align="right">4.30</td>
    <td align="right">2.98</td>
    <td align="right">10.51</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.95</td>
    <td align="right">6.44</td>
    <td align="right">5.07</td>
    <td align="right">13.30</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.71</td>
    <td align="right">6.28</td>
    <td align="right">4.97</td>
    <td align="right">12.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.41</td>
    <td align="right">4.35</td>
    <td align="right">3.02</td>
    <td align="right">10.55</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.89</td>
    <td align="right">7.10</td>
    <td align="right">5.10</td>
    <td align="right">13.70</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.05</td>
    <td align="right">6.80</td>
    <td align="right">5.04</td>
    <td align="right">13.32</td>
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
    <td align="right">2.05</td>
    <td align="right">2.05</td>
    <td align="right">2.05</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.73</td>
    <td align="right">3.26</td>
    <td align="right">3.27</td>
    <td align="right">3.25</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.76</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.23</td>
    <td align="right">2.09</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.18</td>
    <td align="right">4.45</td>
    <td align="right">4.41</td>
    <td align="right">4.39</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.68</td>
    <td align="right">5.07</td>
    <td align="right">5.07</td>
    <td align="right">5.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.39</td>
    <td align="right">3.30</td>
    <td align="right">3.29</td>
    <td align="right">3.28</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.92</td>
    <td align="right">6.64</td>
    <td align="right">6.61</td>
    <td align="right">6.58</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.68</td>
    <td align="right">6.41</td>
    <td align="right">6.40</td>
    <td align="right">6.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.41</td>
    <td align="right">3.32</td>
    <td align="right">3.31</td>
    <td align="right">3.30</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.81</td>
    <td align="right">7.51</td>
    <td align="right">7.49</td>
    <td align="right">7.49</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.02</td>
    <td align="right">7.25</td>
    <td align="right">7.21</td>
    <td align="right">7.19</td>
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
    <td align="right">1.97</td>
    <td align="right">1.97</td>
    <td align="right">1.97</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.64</td>
    <td align="right">3.19</td>
    <td align="right">3.20</td>
    <td align="right">3.19</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.77</td>
    <td align="right">3.08</td>
    <td align="right">3.08</td>
    <td align="right">3.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.16</td>
    <td align="right">3.23</td>
    <td align="right">2.60</td>
    <td align="right">9.35</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.21</td>
    <td align="right">3.83</td>
    <td align="right">3.23</td>
    <td align="right">10.39</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.69</td>
    <td align="right">4.52</td>
    <td align="right">3.82</td>
    <td align="right">10.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.36</td>
    <td align="right">4.22</td>
    <td align="right">2.92</td>
    <td align="right">10.68</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.91</td>
    <td align="right">6.33</td>
    <td align="right">4.75</td>
    <td align="right">13.17</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.60</td>
    <td align="right">6.12</td>
    <td align="right">4.69</td>
    <td align="right">12.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.40</td>
    <td align="right">4.26</td>
    <td align="right">2.91</td>
    <td align="right">10.70</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.45</td>
    <td align="right">6.82</td>
    <td align="right">4.75</td>
    <td align="right">13.55</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.94</td>
    <td align="right">6.69</td>
    <td align="right">4.75</td>
    <td align="right">13.16</td>
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
    <td align="right">2.70</td>
    <td align="right">1.97</td>
    <td align="right">1.97</td>
    <td align="right">1.97</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.63</td>
    <td align="right">3.19</td>
    <td align="right">3.21</td>
    <td align="right">3.19</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.76</td>
    <td align="right">3.08</td>
    <td align="right">3.08</td>
    <td align="right">3.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.16</td>
    <td align="right">2.01</td>
    <td align="right">1.97</td>
    <td align="right">1.97</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.21</td>
    <td align="right">4.44</td>
    <td align="right">4.43</td>
    <td align="right">4.40</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.69</td>
    <td align="right">5.07</td>
    <td align="right">5.03</td>
    <td align="right">5.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.37</td>
    <td align="right">3.24</td>
    <td align="right">3.23</td>
    <td align="right">3.22</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.94</td>
    <td align="right">6.62</td>
    <td align="right">6.61</td>
    <td align="right">6.60</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.63</td>
    <td align="right">6.40</td>
    <td align="right">6.35</td>
    <td align="right">6.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.41</td>
    <td align="right">3.26</td>
    <td align="right">3.26</td>
    <td align="right">3.22</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.44</td>
    <td align="right">7.40</td>
    <td align="right">7.37</td>
    <td align="right">7.36</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.92</td>
    <td align="right">7.08</td>
    <td align="right">7.08</td>
    <td align="right">7.03</td>
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
    <td align="right">7.08</td>
    <td align="right">6.73</td>
    <td align="right">10.98</td>
    <td align="right">10.55</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.66</td>
    <td align="right">8.95</td>
    <td align="right">14.12</td>
    <td align="right">12.95</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.07</td>
    <td align="right">12.06</td>
    <td align="right">15.88</td>
    <td align="right">14.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.39</td>
    <td align="right">9.95</td>
    <td align="right">11.94</td>
    <td align="right">12.90</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.70</td>
    <td align="right">11.09</td>
    <td align="right">13.04</td>
    <td align="right">14.33</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.75</td>
    <td align="right">15.92</td>
    <td align="right">16.24</td>
    <td align="right">17.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.42</td>
    <td align="right">11.56</td>
    <td align="right">11.95</td>
    <td align="right">14.35</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.27</td>
    <td align="right">13.15</td>
    <td align="right">14.00</td>
    <td align="right">15.86</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.54</td>
    <td align="right">17.82</td>
    <td align="right">18.01</td>
    <td align="right">18.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.66</td>
    <td align="right">13.88</td>
    <td align="right">12.29</td>
    <td align="right">16.45</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.50</td>
    <td align="right">15.19</td>
    <td align="right">12.27</td>
    <td align="right">17.19</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.55</td>
    <td align="right">23.90</td>
    <td align="right">19.40</td>
    <td align="right">22.26</td>
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
    <td align="right">7.13</td>
    <td align="right">6.01</td>
    <td align="right">6.06</td>
    <td align="right">6.06</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.36</td>
    <td align="right">7.84</td>
    <td align="right">7.86</td>
    <td align="right">7.86</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.07</td>
    <td align="right">8.88</td>
    <td align="right">9.06</td>
    <td align="right">8.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.38</td>
    <td align="right">8.07</td>
    <td align="right">8.04</td>
    <td align="right">7.99</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.77</td>
    <td align="right">9.18</td>
    <td align="right">9.15</td>
    <td align="right">9.11</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.69</td>
    <td align="right">12.64</td>
    <td align="right">12.96</td>
    <td align="right">13.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.48</td>
    <td align="right">10.74</td>
    <td align="right">10.74</td>
    <td align="right">10.73</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.27</td>
    <td align="right">12.75</td>
    <td align="right">12.56</td>
    <td align="right">12.52</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.49</td>
    <td align="right">14.70</td>
    <td align="right">14.67</td>
    <td align="right">14.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.68</td>
    <td align="right">12.67</td>
    <td align="right">12.67</td>
    <td align="right">12.65</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.41</td>
    <td align="right">14.25</td>
    <td align="right">14.19</td>
    <td align="right">14.15</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.55</td>
    <td align="right">22.82</td>
    <td align="right">22.65</td>
    <td align="right">22.66</td>
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
    <td align="right">7.37</td>
    <td align="right">6.84</td>
    <td align="right">11.47</td>
    <td align="right">10.76</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.71</td>
    <td align="right">8.89</td>
    <td align="right">14.10</td>
    <td align="right">12.57</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.15</td>
    <td align="right">12.26</td>
    <td align="right">16.25</td>
    <td align="right">15.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.65</td>
    <td align="right">10.07</td>
    <td align="right">12.19</td>
    <td align="right">13.20</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.73</td>
    <td align="right">11.23</td>
    <td align="right">13.35</td>
    <td align="right">14.26</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.74</td>
    <td align="right">16.03</td>
    <td align="right">16.31</td>
    <td align="right">17.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.86</td>
    <td align="right">11.59</td>
    <td align="right">12.02</td>
    <td align="right">14.32</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.18</td>
    <td align="right">13.32</td>
    <td align="right">13.96</td>
    <td align="right">15.92</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.23</td>
    <td align="right">17.76</td>
    <td align="right">14.77</td>
    <td align="right">18.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">15.16</td>
    <td align="right">14.35</td>
    <td align="right">12.52</td>
    <td align="right">17.04</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.45</td>
    <td align="right">15.19</td>
    <td align="right">12.42</td>
    <td align="right">17.14</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.72</td>
    <td align="right">24.33</td>
    <td align="right">15.85</td>
    <td align="right">22.33</td>
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
    <td align="right">6.14</td>
    <td align="right">6.17</td>
    <td align="right">6.14</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.38</td>
    <td align="right">7.77</td>
    <td align="right">7.77</td>
    <td align="right">7.77</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.16</td>
    <td align="right">9.27</td>
    <td align="right">9.35</td>
    <td align="right">9.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.71</td>
    <td align="right">8.41</td>
    <td align="right">8.21</td>
    <td align="right">8.21</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.69</td>
    <td align="right">9.13</td>
    <td align="right">9.11</td>
    <td align="right">8.97</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.76</td>
    <td align="right">13.10</td>
    <td align="right">12.98</td>
    <td align="right">12.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.82</td>
    <td align="right">11.32</td>
    <td align="right">11.17</td>
    <td align="right">11.17</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.24</td>
    <td align="right">12.67</td>
    <td align="right">12.59</td>
    <td align="right">12.52</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.25</td>
    <td align="right">14.67</td>
    <td align="right">14.70</td>
    <td align="right">14.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">15.07</td>
    <td align="right">13.05</td>
    <td align="right">12.95</td>
    <td align="right">12.91</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.32</td>
    <td align="right">14.08</td>
    <td align="right">14.07</td>
    <td align="right">14.08</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.60</td>
    <td align="right">22.27</td>
    <td align="right">22.17</td>
    <td align="right">22.24</td>
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
    <td align="right">46.34</td>
    <td align="right">23.18</td>
    <td align="right">12.44</td>
    <td align="right">27.67</td>
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
    <td align="right">14.33</td>
    <td align="right">11.85</td>
    <td align="right">15.71</td>
    <td align="right">14.88</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.15</td>
    <td align="right">3.85</td>
    <td align="right">3.85</td>
    <td align="right">3.85</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.74</td>
    <td align="right">4.53</td>
    <td align="right">4.52</td>
    <td align="right">4.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">47.56</td>
    <td align="right">62.08</td>
    <td align="right">26.29</td>
    <td align="right">45.81</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.28</td>
    <td align="right">5.85</td>
    <td align="right">5.79</td>
    <td align="right">5.83</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">7.13</td>
    <td align="right">6.66</td>
    <td align="right">6.59</td>
    <td align="right">6.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">73.87</td>
    <td align="right">91.19</td>
    <td align="right">29.32</td>
    <td align="right">62.96</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.60</td>
    <td align="right">13.89</td>
    <td align="right">13.94</td>
    <td align="right">13.90</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.37</td>
    <td align="right">15.85</td>
    <td align="right">15.99</td>
    <td align="right">15.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.16</td>
    <td align="right">121.45</td>
    <td align="right">31.89</td>
    <td align="right">79.73</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.75</td>
    <td align="right">18.72</td>
    <td align="right">18.69</td>
    <td align="right">18.79</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.80</td>
    <td align="right">22.61</td>
    <td align="right">22.59</td>
    <td align="right">22.59</td>
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
    <td align="right">11.13</td>
    <td align="right">13.06</td>
    <td align="right">13.03</td>
    <td align="right">13.02</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.13</td>
    <td align="right">3.85</td>
    <td align="right">3.84</td>
    <td align="right">3.84</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.67</td>
    <td align="right">4.51</td>
    <td align="right">4.53</td>
    <td align="right">4.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">25.58</td>
    <td align="right">60.38</td>
    <td align="right">60.22</td>
    <td align="right">60.35</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.14</td>
    <td align="right">5.75</td>
    <td align="right">5.97</td>
    <td align="right">5.79</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.77</td>
    <td align="right">6.43</td>
    <td align="right">6.59</td>
    <td align="right">6.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.64</td>
    <td align="right">86.88</td>
    <td align="right">86.64</td>
    <td align="right">86.63</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.59</td>
    <td align="right">13.98</td>
    <td align="right">13.93</td>
    <td align="right">13.92</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.44</td>
    <td align="right">15.94</td>
    <td align="right">15.95</td>
    <td align="right">15.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">102.30</td>
    <td align="right">129.23</td>
    <td align="right">129.45</td>
    <td align="right">129.26</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.58</td>
    <td align="right">18.72</td>
    <td align="right">18.82</td>
    <td align="right">18.78</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.86</td>
    <td align="right">22.77</td>
    <td align="right">22.74</td>
    <td align="right">22.72</td>
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
    <td align="right">10.81</td>
    <td align="right">12.22</td>
    <td align="right">17.18</td>
    <td align="right">15.22</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.19</td>
    <td align="right">3.83</td>
    <td align="right">3.83</td>
    <td align="right">3.83</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.73</td>
    <td align="right">4.58</td>
    <td align="right">4.59</td>
    <td align="right">4.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">25.01</td>
    <td align="right">18.31</td>
    <td align="right">18.13</td>
    <td align="right">19.60</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.27</td>
    <td align="right">5.81</td>
    <td align="right">5.93</td>
    <td align="right">5.89</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.90</td>
    <td align="right">6.76</td>
    <td align="right">6.83</td>
    <td align="right">6.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">71.70</td>
    <td align="right">95.31</td>
    <td align="right">32.32</td>
    <td align="right">65.50</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.47</td>
    <td align="right">14.83</td>
    <td align="right">14.77</td>
    <td align="right">14.74</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.47</td>
    <td align="right">15.99</td>
    <td align="right">15.96</td>
    <td align="right">16.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.56</td>
    <td align="right">131.13</td>
    <td align="right">36.36</td>
    <td align="right">85.81</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.60</td>
    <td align="right">18.61</td>
    <td align="right">18.64</td>
    <td align="right">18.70</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.56</td>
    <td align="right">22.85</td>
    <td align="right">22.89</td>
    <td align="right">22.89</td>
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
    <td align="right">10.79</td>
    <td align="right">55.79</td>
    <td align="right">55.75</td>
    <td align="right">55.83</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.19</td>
    <td align="right">3.83</td>
    <td align="right">3.83</td>
    <td align="right">3.83</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.73</td>
    <td align="right">4.57</td>
    <td align="right">4.59</td>
    <td align="right">4.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">24.86</td>
    <td align="right">21.01</td>
    <td align="right">21.14</td>
    <td align="right">21.06</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.23</td>
    <td align="right">15.22</td>
    <td align="right">15.23</td>
    <td align="right">15.26</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">6.88</td>
    <td align="right">6.61</td>
    <td align="right">6.79</td>
    <td align="right">6.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">73.13</td>
    <td align="right">90.76</td>
    <td align="right">90.85</td>
    <td align="right">90.81</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.52</td>
    <td align="right">14.78</td>
    <td align="right">14.71</td>
    <td align="right">14.79</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.57</td>
    <td align="right">16.04</td>
    <td align="right">15.95</td>
    <td align="right">15.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.13</td>
    <td align="right">141.81</td>
    <td align="right">141.95</td>
    <td align="right">141.96</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.67</td>
    <td align="right">18.75</td>
    <td align="right">18.77</td>
    <td align="right">18.71</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.54</td>
    <td align="right">22.82</td>
    <td align="right">22.83</td>
    <td align="right">22.91</td>
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
    <td align="right">6.11</td>
    <td align="right">7.43</td>
    <td align="right">11.77</td>
    <td align="right">11.48</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.71</td>
    <td align="right">7.87</td>
    <td align="right">12.90</td>
    <td align="right">12.51</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.09</td>
    <td align="right">2.32</td>
    <td align="right">2.33</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.27</td>
    <td align="right">11.57</td>
    <td align="right">13.26</td>
    <td align="right">14.56</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.93</td>
    <td align="right">13.85</td>
    <td align="right">14.00</td>
    <td align="right">16.77</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">5.41</td>
    <td align="right">5.59</td>
    <td align="right">4.99</td>
    <td align="right">10.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.89</td>
    <td align="right">34.19</td>
    <td align="right">23.95</td>
    <td align="right">34.12</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">30.68</td>
    <td align="right">38.24</td>
    <td align="right">29.45</td>
    <td align="right">39.67</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.08</td>
    <td align="right">15.46</td>
    <td align="right">10.97</td>
    <td align="right">17.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">35.98</td>
    <td align="right">39.53</td>
    <td align="right">24.30</td>
    <td align="right">38.09</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.47</td>
    <td align="right">56.36</td>
    <td align="right">30.37</td>
    <td align="right">53.68</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.34</td>
    <td align="right">17.83</td>
    <td align="right">12.35</td>
    <td align="right">20.04</td>
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
    <td align="right">6.23</td>
    <td align="right">4.58</td>
    <td align="right">4.61</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.63</td>
    <td align="right">4.96</td>
    <td align="right">4.99</td>
    <td align="right">4.97</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.11</td>
    <td align="right">2.33</td>
    <td align="right">2.31</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.42</td>
    <td align="right">8.89</td>
    <td align="right">8.90</td>
    <td align="right">8.95</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.29</td>
    <td align="right">14.19</td>
    <td align="right">14.25</td>
    <td align="right">14.24</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.96</td>
    <td align="right">4.13</td>
    <td align="right">4.09</td>
    <td align="right">4.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">27.12</td>
    <td align="right">23.71</td>
    <td align="right">23.71</td>
    <td align="right">23.94</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">31.18</td>
    <td align="right">28.37</td>
    <td align="right">28.35</td>
    <td align="right">28.43</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.13</td>
    <td align="right">13.24</td>
    <td align="right">13.22</td>
    <td align="right">13.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">35.91</td>
    <td align="right">34.83</td>
    <td align="right">34.91</td>
    <td align="right">35.05</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.51</td>
    <td align="right">38.14</td>
    <td align="right">38.17</td>
    <td align="right">38.14</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.35</td>
    <td align="right">15.16</td>
    <td align="right">15.16</td>
    <td align="right">15.15</td>
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
    <td align="right">5.98</td>
    <td align="right">7.51</td>
    <td align="right">11.92</td>
    <td align="right">11.84</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.66</td>
    <td align="right">8.09</td>
    <td align="right">12.91</td>
    <td align="right">12.40</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.08</td>
    <td align="right">2.25</td>
    <td align="right">2.26</td>
    <td align="right">2.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.12</td>
    <td align="right">12.17</td>
    <td align="right">13.58</td>
    <td align="right">14.83</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">17.28</td>
    <td align="right">14.68</td>
    <td align="right">14.23</td>
    <td align="right">17.25</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.89</td>
    <td align="right">4.74</td>
    <td align="right">4.38</td>
    <td align="right">10.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.65</td>
    <td align="right">34.25</td>
    <td align="right">24.45</td>
    <td align="right">34.12</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">30.27</td>
    <td align="right">31.74</td>
    <td align="right">25.63</td>
    <td align="right">33.04</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.14</td>
    <td align="right">15.14</td>
    <td align="right">10.78</td>
    <td align="right">17.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.13</td>
    <td align="right">45.47</td>
    <td align="right">25.08</td>
    <td align="right">43.41</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.76</td>
    <td align="right">55.39</td>
    <td align="right">30.29</td>
    <td align="right">53.36</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">18.02</td>
    <td align="right">17.91</td>
    <td align="right">12.37</td>
    <td align="right">20.10</td>
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
    <td align="right">5.98</td>
    <td align="right">4.57</td>
    <td align="right">4.58</td>
    <td align="right">4.57</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.80</td>
    <td align="right">5.02</td>
    <td align="right">5.03</td>
    <td align="right">5.02</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.08</td>
    <td align="right">2.25</td>
    <td align="right">2.25</td>
    <td align="right">2.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.20</td>
    <td align="right">8.93</td>
    <td align="right">9.03</td>
    <td align="right">8.98</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">14.49</td>
    <td align="right">23.10</td>
    <td align="right">23.04</td>
    <td align="right">23.10</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.81</td>
    <td align="right">4.07</td>
    <td align="right">4.08</td>
    <td align="right">4.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">27.43</td>
    <td align="right">31.40</td>
    <td align="right">31.51</td>
    <td align="right">31.51</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">30.09</td>
    <td align="right">28.31</td>
    <td align="right">28.22</td>
    <td align="right">28.28</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.11</td>
    <td align="right">13.07</td>
    <td align="right">13.04</td>
    <td align="right">13.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.09</td>
    <td align="right">35.19</td>
    <td align="right">35.28</td>
    <td align="right">35.30</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.71</td>
    <td align="right">38.07</td>
    <td align="right">38.09</td>
    <td align="right">38.01</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.94</td>
    <td align="right">14.85</td>
    <td align="right">14.85</td>
    <td align="right">14.93</td>
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
    <td align="right">3.04</td>
    <td align="right">2.16</td>
    <td align="right">2.18</td>
    <td align="right">2.16</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.04</td>
    <td align="right">3.43</td>
    <td align="right">3.43</td>
    <td align="right">3.43</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.14</td>
    <td align="right">3.30</td>
    <td align="right">3.32</td>
    <td align="right">3.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.16</td>
    <td align="right">5.41</td>
    <td align="right">4.67</td>
    <td align="right">10.93</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">5.95</td>
    <td align="right">5.56</td>
    <td align="right">5.18</td>
    <td align="right">12.14</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.51</td>
    <td align="right">6.74</td>
    <td align="right">6.01</td>
    <td align="right">12.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.15</td>
    <td align="right">15.45</td>
    <td align="right">10.97</td>
    <td align="right">17.38</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.56</td>
    <td align="right">19.06</td>
    <td align="right">16.12</td>
    <td align="right">22.61</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.98</td>
    <td align="right">21.81</td>
    <td align="right">18.33</td>
    <td align="right">24.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.65</td>
    <td align="right">17.89</td>
    <td align="right">12.39</td>
    <td align="right">19.62</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.50</td>
    <td align="right">26.83</td>
    <td align="right">19.00</td>
    <td align="right">26.97</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.56</td>
    <td align="right">26.73</td>
    <td align="right">19.06</td>
    <td align="right">26.12</td>
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
    <td align="right">3.08</td>
    <td align="right">2.16</td>
    <td align="right">2.17</td>
    <td align="right">2.16</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.05</td>
    <td align="right">5.45</td>
    <td align="right">5.44</td>
    <td align="right">5.44</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.13</td>
    <td align="right">7.63</td>
    <td align="right">7.63</td>
    <td align="right">7.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.23</td>
    <td align="right">4.16</td>
    <td align="right">4.14</td>
    <td align="right">4.11</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">6.04</td>
    <td align="right">6.16</td>
    <td align="right">6.20</td>
    <td align="right">6.16</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.44</td>
    <td align="right">7.43</td>
    <td align="right">7.49</td>
    <td align="right">7.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.96</td>
    <td align="right">14.57</td>
    <td align="right">14.59</td>
    <td align="right">14.58</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.81</td>
    <td align="right">19.48</td>
    <td align="right">19.44</td>
    <td align="right">19.44</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">21.04</td>
    <td align="right">20.31</td>
    <td align="right">20.29</td>
    <td align="right">20.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.81</td>
    <td align="right">15.03</td>
    <td align="right">15.03</td>
    <td align="right">15.03</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.54</td>
    <td align="right">27.53</td>
    <td align="right">27.62</td>
    <td align="right">27.61</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.69</td>
    <td align="right">27.61</td>
    <td align="right">27.55</td>
    <td align="right">27.64</td>
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
    <td align="right">2.95</td>
    <td align="right">2.08</td>
    <td align="right">2.08</td>
    <td align="right">2.08</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">3.98</td>
    <td align="right">3.37</td>
    <td align="right">3.38</td>
    <td align="right">3.37</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.13</td>
    <td align="right">7.20</td>
    <td align="right">7.20</td>
    <td align="right">7.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">4.89</td>
    <td align="right">5.01</td>
    <td align="right">4.31</td>
    <td align="right">10.68</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">6.19</td>
    <td align="right">5.64</td>
    <td align="right">5.11</td>
    <td align="right">12.07</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.50</td>
    <td align="right">6.37</td>
    <td align="right">5.57</td>
    <td align="right">12.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.20</td>
    <td align="right">15.36</td>
    <td align="right">10.87</td>
    <td align="right">17.13</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.91</td>
    <td align="right">19.15</td>
    <td align="right">15.86</td>
    <td align="right">22.20</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">21.12</td>
    <td align="right">19.22</td>
    <td align="right">16.12</td>
    <td align="right">21.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.88</td>
    <td align="right">17.89</td>
    <td align="right">12.26</td>
    <td align="right">19.55</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">29.14</td>
    <td align="right">26.27</td>
    <td align="right">18.70</td>
    <td align="right">26.13</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">29.02</td>
    <td align="right">25.64</td>
    <td align="right">18.63</td>
    <td align="right">25.76</td>
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
    <td align="right">2.94</td>
    <td align="right">2.09</td>
    <td align="right">2.08</td>
    <td align="right">2.08</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">3.98</td>
    <td align="right">3.37</td>
    <td align="right">3.38</td>
    <td align="right">3.37</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.25</td>
    <td align="right">3.24</td>
    <td align="right">3.25</td>
    <td align="right">3.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">4.82</td>
    <td align="right">3.98</td>
    <td align="right">3.96</td>
    <td align="right">3.99</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">5.94</td>
    <td align="right">5.91</td>
    <td align="right">6.06</td>
    <td align="right">6.04</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.94</td>
    <td align="right">7.48</td>
    <td align="right">7.54</td>
    <td align="right">7.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.14</td>
    <td align="right">12.99</td>
    <td align="right">12.95</td>
    <td align="right">12.95</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.40</td>
    <td align="right">19.30</td>
    <td align="right">19.31</td>
    <td align="right">19.25</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.88</td>
    <td align="right">21.70</td>
    <td align="right">21.72</td>
    <td align="right">21.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.93</td>
    <td align="right">14.81</td>
    <td align="right">14.79</td>
    <td align="right">14.80</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">29.35</td>
    <td align="right">27.36</td>
    <td align="right">27.31</td>
    <td align="right">27.40</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.87</td>
    <td align="right">27.22</td>
    <td align="right">27.32</td>
    <td align="right">27.29</td>
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
    <td align="right">7.61</td>
    <td align="right">10.64</td>
    <td align="right">13.69</td>
    <td align="right">14.29</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.98</td>
    <td align="right">9.80</td>
    <td align="right">14.65</td>
    <td align="right">13.99</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.62</td>
    <td align="right">13.69</td>
    <td align="right">16.92</td>
    <td align="right">16.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">12.34</td>
    <td align="right">16.25</td>
    <td align="right">16.12</td>
    <td align="right">18.95</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">15.01</td>
    <td align="right">14.39</td>
    <td align="right">14.53</td>
    <td align="right">17.62</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">18.47</td>
    <td align="right">17.82</td>
    <td align="right">17.26</td>
    <td align="right">19.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">26.34</td>
    <td align="right">29.86</td>
    <td align="right">21.49</td>
    <td align="right">30.44</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.15</td>
    <td align="right">32.55</td>
    <td align="right">23.88</td>
    <td align="right">34.10</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.09</td>
    <td align="right">43.67</td>
    <td align="right">28.13</td>
    <td align="right">38.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.86</td>
    <td align="right">34.73</td>
    <td align="right">23.05</td>
    <td align="right">36.84</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.72</td>
    <td align="right">41.28</td>
    <td align="right">22.02</td>
    <td align="right">41.76</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">68.62</td>
    <td align="right">65.10</td>
    <td align="right">37.41</td>
    <td align="right">55.02</td>
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
    <td align="right">7.63</td>
    <td align="right">10.66</td>
    <td align="right">10.72</td>
    <td align="right">10.68</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.62</td>
    <td align="right">8.38</td>
    <td align="right">8.37</td>
    <td align="right">8.37</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.47</td>
    <td align="right">10.09</td>
    <td align="right">10.05</td>
    <td align="right">10.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">12.48</td>
    <td align="right">9.77</td>
    <td align="right">9.80</td>
    <td align="right">9.75</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">15.41</td>
    <td align="right">15.96</td>
    <td align="right">15.98</td>
    <td align="right">15.95</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">16.65</td>
    <td align="right">19.61</td>
    <td align="right">19.41</td>
    <td align="right">19.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">26.21</td>
    <td align="right">24.19</td>
    <td align="right">24.20</td>
    <td align="right">24.26</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.97</td>
    <td align="right">32.14</td>
    <td align="right">32.02</td>
    <td align="right">32.13</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.69</td>
    <td align="right">39.76</td>
    <td align="right">39.74</td>
    <td align="right">39.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.62</td>
    <td align="right">33.53</td>
    <td align="right">33.64</td>
    <td align="right">33.44</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.56</td>
    <td align="right">40.23</td>
    <td align="right">40.32</td>
    <td align="right">40.20</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">68.36</td>
    <td align="right">64.39</td>
    <td align="right">64.48</td>
    <td align="right">64.46</td>
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
    <td align="right">7.96</td>
    <td align="right">7.51</td>
    <td align="right">12.18</td>
    <td align="right">11.96</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.66</td>
    <td align="right">9.57</td>
    <td align="right">14.79</td>
    <td align="right">13.61</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.32</td>
    <td align="right">13.89</td>
    <td align="right">17.27</td>
    <td align="right">16.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">12.56</td>
    <td align="right">16.05</td>
    <td align="right">16.13</td>
    <td align="right">18.96</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.85</td>
    <td align="right">18.61</td>
    <td align="right">17.44</td>
    <td align="right">21.07</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">22.21</td>
    <td align="right">17.92</td>
    <td align="right">17.35</td>
    <td align="right">20.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.07</td>
    <td align="right">25.43</td>
    <td align="right">19.74</td>
    <td align="right">27.00</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.34</td>
    <td align="right">32.51</td>
    <td align="right">23.13</td>
    <td align="right">33.79</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.25</td>
    <td align="right">46.06</td>
    <td align="right">24.39</td>
    <td align="right">42.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.79</td>
    <td align="right">42.04</td>
    <td align="right">23.58</td>
    <td align="right">45.26</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.57</td>
    <td align="right">41.21</td>
    <td align="right">21.99</td>
    <td align="right">41.83</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">70.96</td>
    <td align="right">66.48</td>
    <td align="right">26.00</td>
    <td align="right">55.39</td>
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
    <td align="right">7.97</td>
    <td align="right">6.58</td>
    <td align="right">6.59</td>
    <td align="right">6.59</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.78</td>
    <td align="right">8.30</td>
    <td align="right">8.30</td>
    <td align="right">8.35</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.32</td>
    <td align="right">10.30</td>
    <td align="right">10.35</td>
    <td align="right">10.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">12.57</td>
    <td align="right">13.97</td>
    <td align="right">14.09</td>
    <td align="right">14.06</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">16.22</td>
    <td align="right">11.04</td>
    <td align="right">11.19</td>
    <td align="right">11.20</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">20.67</td>
    <td align="right">21.84</td>
    <td align="right">21.86</td>
    <td align="right">21.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">26.81</td>
    <td align="right">29.30</td>
    <td align="right">29.19</td>
    <td align="right">29.29</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.95</td>
    <td align="right">34.90</td>
    <td align="right">34.91</td>
    <td align="right">34.93</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">40.48</td>
    <td align="right">39.73</td>
    <td align="right">39.83</td>
    <td align="right">39.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.83</td>
    <td align="right">33.87</td>
    <td align="right">33.81</td>
    <td align="right">33.77</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.56</td>
    <td align="right">40.58</td>
    <td align="right">40.55</td>
    <td align="right">40.50</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">70.65</td>
    <td align="right">66.75</td>
    <td align="right">66.87</td>
    <td align="right">66.83</td>
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
    <td align="right">73.71</td>
    <td align="right">33.56</td>
    <td align="right">14.26</td>
    <td align="right">28.25</td>
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
    <td align="right">31.72</td>
    <td align="right">44.14</td>
    <td align="right">37.51</td>
    <td align="right">41.00</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.22</td>
    <td align="right">16.05</td>
    <td align="right">16.17</td>
    <td align="right">16.21</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.51</td>
    <td align="right">17.59</td>
    <td align="right">17.45</td>
    <td align="right">17.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">47.02</td>
    <td align="right">67.33</td>
    <td align="right">40.55</td>
    <td align="right">54.21</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.22</td>
    <td align="right">18.12</td>
    <td align="right">18.21</td>
    <td align="right">18.13</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.06</td>
    <td align="right">19.54</td>
    <td align="right">19.08</td>
    <td align="right">18.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.26</td>
    <td align="right">81.83</td>
    <td align="right">39.23</td>
    <td align="right">61.01</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.41</td>
    <td align="right">20.48</td>
    <td align="right">20.55</td>
    <td align="right">20.48</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.03</td>
    <td align="right">20.96</td>
    <td align="right">20.96</td>
    <td align="right">21.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">73.36</td>
    <td align="right">106.82</td>
    <td align="right">40.81</td>
    <td align="right">72.58</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.66</td>
    <td align="right">22.20</td>
    <td align="right">22.21</td>
    <td align="right">22.20</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.12</td>
    <td align="right">22.03</td>
    <td align="right">23.30</td>
    <td align="right">22.05</td>
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
    <td align="right">31.22</td>
    <td align="right">41.91</td>
    <td align="right">41.77</td>
    <td align="right">41.59</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.25</td>
    <td align="right">16.08</td>
    <td align="right">16.19</td>
    <td align="right">16.23</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.60</td>
    <td align="right">17.68</td>
    <td align="right">17.55</td>
    <td align="right">17.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.57</td>
    <td align="right">60.72</td>
    <td align="right">61.07</td>
    <td align="right">61.19</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.32</td>
    <td align="right">18.30</td>
    <td align="right">18.52</td>
    <td align="right">18.45</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.08</td>
    <td align="right">18.98</td>
    <td align="right">19.40</td>
    <td align="right">19.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.38</td>
    <td align="right">70.70</td>
    <td align="right">71.96</td>
    <td align="right">70.06</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.38</td>
    <td align="right">20.45</td>
    <td align="right">20.53</td>
    <td align="right">20.49</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">16.94</td>
    <td align="right">21.06</td>
    <td align="right">21.14</td>
    <td align="right">21.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.84</td>
    <td align="right">112.94</td>
    <td align="right">113.05</td>
    <td align="right">114.05</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.67</td>
    <td align="right">22.20</td>
    <td align="right">22.20</td>
    <td align="right">22.22</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.18</td>
    <td align="right">22.17</td>
    <td align="right">22.31</td>
    <td align="right">22.07</td>
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
    <td align="right">31.42</td>
    <td align="right">44.49</td>
    <td align="right">37.54</td>
    <td align="right">42.01</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.36</td>
    <td align="right">18.99</td>
    <td align="right">19.07</td>
    <td align="right">19.00</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.53</td>
    <td align="right">21.78</td>
    <td align="right">21.82</td>
    <td align="right">21.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.06</td>
    <td align="right">67.35</td>
    <td align="right">41.11</td>
    <td align="right">53.91</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.43</td>
    <td align="right">22.88</td>
    <td align="right">22.86</td>
    <td align="right">22.75</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.07</td>
    <td align="right">20.88</td>
    <td align="right">20.91</td>
    <td align="right">20.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.29</td>
    <td align="right">82.82</td>
    <td align="right">40.14</td>
    <td align="right">62.26</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.53</td>
    <td align="right">21.28</td>
    <td align="right">21.28</td>
    <td align="right">21.27</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.13</td>
    <td align="right">23.09</td>
    <td align="right">23.11</td>
    <td align="right">23.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">71.55</td>
    <td align="right">102.68</td>
    <td align="right">41.86</td>
    <td align="right">72.53</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.80</td>
    <td align="right">23.55</td>
    <td align="right">23.55</td>
    <td align="right">23.26</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.83</td>
    <td align="right">24.58</td>
    <td align="right">24.68</td>
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
    <td align="right">30.99</td>
    <td align="right">47.33</td>
    <td align="right">47.43</td>
    <td align="right">47.56</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.29</td>
    <td align="right">19.07</td>
    <td align="right">18.98</td>
    <td align="right">19.06</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.62</td>
    <td align="right">21.77</td>
    <td align="right">21.82</td>
    <td align="right">21.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.26</td>
    <td align="right">71.63</td>
    <td align="right">71.49</td>
    <td align="right">71.30</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.50</td>
    <td align="right">22.73</td>
    <td align="right">22.85</td>
    <td align="right">22.81</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.07</td>
    <td align="right">20.90</td>
    <td align="right">20.90</td>
    <td align="right">20.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.88</td>
    <td align="right">88.10</td>
    <td align="right">88.35</td>
    <td align="right">87.84</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.52</td>
    <td align="right">21.29</td>
    <td align="right">21.28</td>
    <td align="right">21.26</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.07</td>
    <td align="right">23.08</td>
    <td align="right">22.99</td>
    <td align="right">23.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.16</td>
    <td align="right">116.27</td>
    <td align="right">116.33</td>
    <td align="right">113.58</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.79</td>
    <td align="right">23.58</td>
    <td align="right">23.44</td>
    <td align="right">23.63</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.94</td>
    <td align="right">24.58</td>
    <td align="right">24.58</td>
    <td align="right">24.69</td>
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
    <td align="right">19.95</td>
    <td align="right">23.88</td>
    <td align="right">26.99</td>
    <td align="right">27.97</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.25</td>
    <td align="right">27.37</td>
    <td align="right">29.25</td>
    <td align="right">31.58</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.84</td>
    <td align="right">14.98</td>
    <td align="right">24.10</td>
    <td align="right">21.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.76</td>
    <td align="right">30.75</td>
    <td align="right">28.30</td>
    <td align="right">31.91</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.07</td>
    <td align="right">34.52</td>
    <td align="right">34.01</td>
    <td align="right">35.61</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.19</td>
    <td align="right">17.61</td>
    <td align="right">25.58</td>
    <td align="right">23.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.51</td>
    <td align="right">42.77</td>
    <td align="right">30.48</td>
    <td align="right">40.02</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.49</td>
    <td align="right">49.50</td>
    <td align="right">39.82</td>
    <td align="right">44.91</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.18</td>
    <td align="right">20.15</td>
    <td align="right">26.35</td>
    <td align="right">25.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">38.02</td>
    <td align="right">47.41</td>
    <td align="right">29.70</td>
    <td align="right">42.02</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.71</td>
    <td align="right">57.06</td>
    <td align="right">41.91</td>
    <td align="right">49.33</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.85</td>
    <td align="right">27.73</td>
    <td align="right">25.98</td>
    <td align="right">30.45</td>
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
    <td align="right">19.72</td>
    <td align="right">23.73</td>
    <td align="right">23.73</td>
    <td align="right">23.81</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.25</td>
    <td align="right">26.56</td>
    <td align="right">26.58</td>
    <td align="right">26.55</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.91</td>
    <td align="right">15.97</td>
    <td align="right">15.60</td>
    <td align="right">15.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.53</td>
    <td align="right">30.71</td>
    <td align="right">30.13</td>
    <td align="right">30.13</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.09</td>
    <td align="right">34.62</td>
    <td align="right">34.64</td>
    <td align="right">34.76</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.85</td>
    <td align="right">17.77</td>
    <td align="right">18.35</td>
    <td align="right">18.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.22</td>
    <td align="right">36.90</td>
    <td align="right">36.94</td>
    <td align="right">36.90</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.42</td>
    <td align="right">48.98</td>
    <td align="right">48.99</td>
    <td align="right">49.13</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.00</td>
    <td align="right">20.85</td>
    <td align="right">20.88</td>
    <td align="right">20.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.44</td>
    <td align="right">41.60</td>
    <td align="right">41.50</td>
    <td align="right">41.65</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.61</td>
    <td align="right">58.57</td>
    <td align="right">58.57</td>
    <td align="right">58.51</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.93</td>
    <td align="right">25.97</td>
    <td align="right">25.95</td>
    <td align="right">25.94</td>
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
    <td align="right">19.95</td>
    <td align="right">23.80</td>
    <td align="right">26.97</td>
    <td align="right">27.86</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.19</td>
    <td align="right">27.30</td>
    <td align="right">29.27</td>
    <td align="right">30.52</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">13.05</td>
    <td align="right">14.98</td>
    <td align="right">23.96</td>
    <td align="right">21.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.55</td>
    <td align="right">30.73</td>
    <td align="right">28.59</td>
    <td align="right">31.91</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.07</td>
    <td align="right">34.54</td>
    <td align="right">33.89</td>
    <td align="right">35.60</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">15.06</td>
    <td align="right">17.63</td>
    <td align="right">25.14</td>
    <td align="right">23.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.23</td>
    <td align="right">43.16</td>
    <td align="right">30.51</td>
    <td align="right">39.44</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.79</td>
    <td align="right">49.52</td>
    <td align="right">39.82</td>
    <td align="right">44.89</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.42</td>
    <td align="right">20.16</td>
    <td align="right">26.26</td>
    <td align="right">25.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.52</td>
    <td align="right">47.22</td>
    <td align="right">29.69</td>
    <td align="right">42.07</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.50</td>
    <td align="right">57.27</td>
    <td align="right">41.94</td>
    <td align="right">49.39</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.37</td>
    <td align="right">27.73</td>
    <td align="right">25.89</td>
    <td align="right">30.39</td>
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
    <td align="right">19.93</td>
    <td align="right">23.78</td>
    <td align="right">23.84</td>
    <td align="right">23.74</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.22</td>
    <td align="right">26.58</td>
    <td align="right">26.55</td>
    <td align="right">26.56</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.99</td>
    <td align="right">15.56</td>
    <td align="right">15.56</td>
    <td align="right">15.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.72</td>
    <td align="right">30.01</td>
    <td align="right">30.08</td>
    <td align="right">29.99</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.05</td>
    <td align="right">34.62</td>
    <td align="right">34.62</td>
    <td align="right">34.62</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.88</td>
    <td align="right">18.49</td>
    <td align="right">18.40</td>
    <td align="right">18.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.22</td>
    <td align="right">36.95</td>
    <td align="right">37.11</td>
    <td align="right">36.92</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.47</td>
    <td align="right">49.05</td>
    <td align="right">49.05</td>
    <td align="right">49.03</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.52</td>
    <td align="right">20.86</td>
    <td align="right">20.85</td>
    <td align="right">20.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.53</td>
    <td align="right">41.70</td>
    <td align="right">41.69</td>
    <td align="right">41.70</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.63</td>
    <td align="right">58.67</td>
    <td align="right">58.71</td>
    <td align="right">58.67</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.15</td>
    <td align="right">25.98</td>
    <td align="right">26.04</td>
    <td align="right">25.99</td>
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
    <td align="right">14.41</td>
    <td align="right">16.47</td>
    <td align="right">26.11</td>
    <td align="right">23.78</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.91</td>
    <td align="right">23.93</td>
    <td align="right">26.97</td>
    <td align="right">27.87</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.24</td>
    <td align="right">27.33</td>
    <td align="right">29.24</td>
    <td align="right">31.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.01</td>
    <td align="right">19.85</td>
    <td align="right">26.90</td>
    <td align="right">25.56</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.71</td>
    <td align="right">30.73</td>
    <td align="right">28.29</td>
    <td align="right">31.79</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.07</td>
    <td align="right">34.53</td>
    <td align="right">34.06</td>
    <td align="right">35.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.55</td>
    <td align="right">22.93</td>
    <td align="right">28.31</td>
    <td align="right">28.47</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.23</td>
    <td align="right">44.42</td>
    <td align="right">30.55</td>
    <td align="right">39.48</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.55</td>
    <td align="right">49.56</td>
    <td align="right">39.83</td>
    <td align="right">44.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.80</td>
    <td align="right">30.62</td>
    <td align="right">28.80</td>
    <td align="right">32.96</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">38.10</td>
    <td align="right">50.66</td>
    <td align="right">29.73</td>
    <td align="right">44.25</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.62</td>
    <td align="right">57.01</td>
    <td align="right">41.89</td>
    <td align="right">49.30</td>
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
    <td align="right">14.45</td>
    <td align="right">16.99</td>
    <td align="right">17.13</td>
    <td align="right">16.83</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.91</td>
    <td align="right">23.68</td>
    <td align="right">23.70</td>
    <td align="right">23.74</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.24</td>
    <td align="right">26.68</td>
    <td align="right">26.62</td>
    <td align="right">26.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.24</td>
    <td align="right">21.05</td>
    <td align="right">21.21</td>
    <td align="right">21.14</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.56</td>
    <td align="right">30.10</td>
    <td align="right">30.52</td>
    <td align="right">30.15</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.06</td>
    <td align="right">34.61</td>
    <td align="right">34.62</td>
    <td align="right">34.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.49</td>
    <td align="right">25.12</td>
    <td align="right">25.11</td>
    <td align="right">25.20</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.23</td>
    <td align="right">36.94</td>
    <td align="right">37.15</td>
    <td align="right">37.03</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.48</td>
    <td align="right">49.03</td>
    <td align="right">49.07</td>
    <td align="right">49.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.86</td>
    <td align="right">33.10</td>
    <td align="right">33.09</td>
    <td align="right">33.10</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.48</td>
    <td align="right">41.62</td>
    <td align="right">41.51</td>
    <td align="right">41.69</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.57</td>
    <td align="right">58.54</td>
    <td align="right">58.53</td>
    <td align="right">58.56</td>
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
    <td align="right">14.59</td>
    <td align="right">16.50</td>
    <td align="right">25.13</td>
    <td align="right">23.78</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.81</td>
    <td align="right">23.89</td>
    <td align="right">26.99</td>
    <td align="right">27.85</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.20</td>
    <td align="right">27.31</td>
    <td align="right">29.26</td>
    <td align="right">30.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.07</td>
    <td align="right">19.84</td>
    <td align="right">26.82</td>
    <td align="right">25.61</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.61</td>
    <td align="right">30.81</td>
    <td align="right">28.30</td>
    <td align="right">31.89</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">36.99</td>
    <td align="right">34.51</td>
    <td align="right">33.85</td>
    <td align="right">35.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.57</td>
    <td align="right">22.96</td>
    <td align="right">28.37</td>
    <td align="right">28.65</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.79</td>
    <td align="right">43.25</td>
    <td align="right">30.52</td>
    <td align="right">39.48</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.87</td>
    <td align="right">49.52</td>
    <td align="right">39.84</td>
    <td align="right">44.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.86</td>
    <td align="right">30.62</td>
    <td align="right">28.49</td>
    <td align="right">32.97</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.53</td>
    <td align="right">48.67</td>
    <td align="right">29.65</td>
    <td align="right">43.62</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.50</td>
    <td align="right">57.31</td>
    <td align="right">41.97</td>
    <td align="right">49.43</td>
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
    <td align="right">16.86</td>
    <td align="right">16.85</td>
    <td align="right">16.97</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.90</td>
    <td align="right">23.73</td>
    <td align="right">23.73</td>
    <td align="right">23.70</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.22</td>
    <td align="right">26.56</td>
    <td align="right">26.56</td>
    <td align="right">26.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.10</td>
    <td align="right">21.04</td>
    <td align="right">21.06</td>
    <td align="right">21.08</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.83</td>
    <td align="right">30.02</td>
    <td align="right">30.06</td>
    <td align="right">30.11</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.01</td>
    <td align="right">34.63</td>
    <td align="right">34.61</td>
    <td align="right">34.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.48</td>
    <td align="right">25.14</td>
    <td align="right">25.16</td>
    <td align="right">25.15</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.27</td>
    <td align="right">36.96</td>
    <td align="right">36.99</td>
    <td align="right">36.94</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.41</td>
    <td align="right">49.11</td>
    <td align="right">49.06</td>
    <td align="right">49.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.82</td>
    <td align="right">33.13</td>
    <td align="right">33.12</td>
    <td align="right">33.12</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.69</td>
    <td align="right">41.54</td>
    <td align="right">41.50</td>
    <td align="right">41.75</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.63</td>
    <td align="right">58.57</td>
    <td align="right">58.65</td>
    <td align="right">58.66</td>
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
    <td align="right">18.36</td>
    <td align="right">24.62</td>
    <td align="right">28.09</td>
    <td align="right">27.87</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.72</td>
    <td align="right">31.69</td>
    <td align="right">36.25</td>
    <td align="right">33.76</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.19</td>
    <td align="right">36.66</td>
    <td align="right">33.71</td>
    <td align="right">35.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.38</td>
    <td align="right">37.06</td>
    <td align="right">28.37</td>
    <td align="right">35.93</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.32</td>
    <td align="right">40.87</td>
    <td align="right">34.50</td>
    <td align="right">39.33</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.66</td>
    <td align="right">48.69</td>
    <td align="right">36.95</td>
    <td align="right">43.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.11</td>
    <td align="right">44.10</td>
    <td align="right">28.00</td>
    <td align="right">39.89</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.47</td>
    <td align="right">49.81</td>
    <td align="right">35.92</td>
    <td align="right">44.53</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.20</td>
    <td align="right">50.43</td>
    <td align="right">32.74</td>
    <td align="right">45.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.30</td>
    <td align="right">49.46</td>
    <td align="right">29.58</td>
    <td align="right">42.73</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.36</td>
    <td align="right">52.87</td>
    <td align="right">35.65</td>
    <td align="right">46.18</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">63.19</td>
    <td align="right">65.36</td>
    <td align="right">35.45</td>
    <td align="right">51.09</td>
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
    <td align="right">18.33</td>
    <td align="right">24.31</td>
    <td align="right">24.28</td>
    <td align="right">24.22</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.72</td>
    <td align="right">32.59</td>
    <td align="right">32.60</td>
    <td align="right">32.68</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.30</td>
    <td align="right">34.78</td>
    <td align="right">34.61</td>
    <td align="right">34.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.33</td>
    <td align="right">33.70</td>
    <td align="right">33.69</td>
    <td align="right">33.68</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.22</td>
    <td align="right">39.39</td>
    <td align="right">39.44</td>
    <td align="right">39.45</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.82</td>
    <td align="right">44.72</td>
    <td align="right">44.77</td>
    <td align="right">44.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.12</td>
    <td align="right">41.19</td>
    <td align="right">41.18</td>
    <td align="right">41.17</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.52</td>
    <td align="right">48.26</td>
    <td align="right">48.25</td>
    <td align="right">48.25</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">43.99</td>
    <td align="right">47.32</td>
    <td align="right">47.31</td>
    <td align="right">47.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.30</td>
    <td align="right">46.99</td>
    <td align="right">46.97</td>
    <td align="right">46.91</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.37</td>
    <td align="right">52.48</td>
    <td align="right">52.50</td>
    <td align="right">52.49</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">62.61</td>
    <td align="right">65.54</td>
    <td align="right">65.02</td>
    <td align="right">65.43</td>
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
    <td align="right">18.30</td>
    <td align="right">24.40</td>
    <td align="right">28.33</td>
    <td align="right">28.12</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.22</td>
    <td align="right">31.73</td>
    <td align="right">36.30</td>
    <td align="right">33.84</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.61</td>
    <td align="right">37.02</td>
    <td align="right">35.98</td>
    <td align="right">36.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.43</td>
    <td align="right">36.87</td>
    <td align="right">28.63</td>
    <td align="right">36.00</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.02</td>
    <td align="right">40.72</td>
    <td align="right">34.33</td>
    <td align="right">39.32</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">41.75</td>
    <td align="right">47.60</td>
    <td align="right">36.27</td>
    <td align="right">42.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.14</td>
    <td align="right">43.90</td>
    <td align="right">27.92</td>
    <td align="right">39.86</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.53</td>
    <td align="right">50.05</td>
    <td align="right">35.86</td>
    <td align="right">44.42</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.55</td>
    <td align="right">50.55</td>
    <td align="right">33.12</td>
    <td align="right">45.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.31</td>
    <td align="right">49.20</td>
    <td align="right">29.36</td>
    <td align="right">42.54</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.39</td>
    <td align="right">52.70</td>
    <td align="right">36.23</td>
    <td align="right">46.09</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">61.31</td>
    <td align="right">65.80</td>
    <td align="right">33.57</td>
    <td align="right">52.49</td>
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
    <td align="right">18.36</td>
    <td align="right">24.32</td>
    <td align="right">24.24</td>
    <td align="right">24.27</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.18</td>
    <td align="right">32.62</td>
    <td align="right">32.59</td>
    <td align="right">32.60</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">30.05</td>
    <td align="right">34.71</td>
    <td align="right">34.51</td>
    <td align="right">34.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.40</td>
    <td align="right">33.66</td>
    <td align="right">33.68</td>
    <td align="right">33.72</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.39</td>
    <td align="right">39.35</td>
    <td align="right">39.34</td>
    <td align="right">39.35</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.01</td>
    <td align="right">44.87</td>
    <td align="right">44.94</td>
    <td align="right">45.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.11</td>
    <td align="right">41.23</td>
    <td align="right">41.23</td>
    <td align="right">41.18</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.58</td>
    <td align="right">48.28</td>
    <td align="right">48.30</td>
    <td align="right">48.28</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">43.75</td>
    <td align="right">47.15</td>
    <td align="right">47.22</td>
    <td align="right">47.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.35</td>
    <td align="right">46.84</td>
    <td align="right">47.00</td>
    <td align="right">46.97</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.45</td>
    <td align="right">52.45</td>
    <td align="right">52.47</td>
    <td align="right">52.46</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">61.38</td>
    <td align="right">64.69</td>
    <td align="right">65.08</td>
    <td align="right">65.41</td>
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
    <td align="right">108.12</td>
    <td align="right">125.88</td>
    <td align="right">27.22</td>
    <td align="right">82.64</td>
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
    <td align="right">37.97</td>
    <td align="right">53.86</td>
    <td align="right">44.62</td>
    <td align="right">49.73</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.22</td>
    <td align="right">19.67</td>
    <td align="right">19.56</td>
    <td align="right">19.69</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.31</td>
    <td align="right">20.46</td>
    <td align="right">20.30</td>
    <td align="right">20.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">96.22</td>
    <td align="right">126.28</td>
    <td align="right">58.50</td>
    <td align="right">92.61</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.30</td>
    <td align="right">28.97</td>
    <td align="right">28.42</td>
    <td align="right">28.31</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">25.08</td>
    <td align="right">30.51</td>
    <td align="right">30.49</td>
    <td align="right">30.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">189.82</td>
    <td align="right">247.82</td>
    <td align="right">77.92</td>
    <td align="right">163.22</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.50</td>
    <td align="right">47.30</td>
    <td align="right">47.28</td>
    <td align="right">47.29</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.66</td>
    <td align="right">50.00</td>
    <td align="right">49.91</td>
    <td align="right">49.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">298.12</td>
    <td align="right">404.14</td>
    <td align="right">99.47</td>
    <td align="right">251.82</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">46.90</td>
    <td align="right">63.87</td>
    <td align="right">63.88</td>
    <td align="right">63.93</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.91</td>
    <td align="right">63.15</td>
    <td align="right">64.28</td>
    <td align="right">63.08</td>
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
    <td align="right">35.52</td>
    <td align="right">46.30</td>
    <td align="right">46.43</td>
    <td align="right">46.34</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.40</td>
    <td align="right">20.43</td>
    <td align="right">20.00</td>
    <td align="right">19.90</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.63</td>
    <td align="right">20.97</td>
    <td align="right">21.26</td>
    <td align="right">21.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">98.71</td>
    <td align="right">112.19</td>
    <td align="right">112.15</td>
    <td align="right">112.14</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.88</td>
    <td align="right">29.05</td>
    <td align="right">29.02</td>
    <td align="right">29.08</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.89</td>
    <td align="right">28.54</td>
    <td align="right">28.64</td>
    <td align="right">28.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">192.71</td>
    <td align="right">178.37</td>
    <td align="right">179.84</td>
    <td align="right">177.70</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">38.31</td>
    <td align="right">48.09</td>
    <td align="right">48.00</td>
    <td align="right">48.01</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.12</td>
    <td align="right">48.69</td>
    <td align="right">48.96</td>
    <td align="right">49.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.64</td>
    <td align="right">414.85</td>
    <td align="right">414.94</td>
    <td align="right">414.52</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.03</td>
    <td align="right">64.10</td>
    <td align="right">64.09</td>
    <td align="right">64.01</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">62.03</td>
    <td align="right">63.50</td>
    <td align="right">63.52</td>
    <td align="right">63.53</td>
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
    <td align="right">40.55</td>
    <td align="right">57.17</td>
    <td align="right">45.87</td>
    <td align="right">51.09</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.72</td>
    <td align="right">20.70</td>
    <td align="right">20.96</td>
    <td align="right">20.66</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.34</td>
    <td align="right">26.57</td>
    <td align="right">26.42</td>
    <td align="right">26.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">107.48</td>
    <td align="right">139.00</td>
    <td align="right">62.24</td>
    <td align="right">100.66</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.15</td>
    <td align="right">34.81</td>
    <td align="right">34.81</td>
    <td align="right">34.71</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.00</td>
    <td align="right">32.45</td>
    <td align="right">32.52</td>
    <td align="right">32.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">189.02</td>
    <td align="right">251.73</td>
    <td align="right">80.23</td>
    <td align="right">168.58</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.36</td>
    <td align="right">47.05</td>
    <td align="right">46.93</td>
    <td align="right">46.88</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.31</td>
    <td align="right">51.08</td>
    <td align="right">51.19</td>
    <td align="right">51.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">296.00</td>
    <td align="right">399.17</td>
    <td align="right">98.68</td>
    <td align="right">271.56</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.35</td>
    <td align="right">65.01</td>
    <td align="right">64.99</td>
    <td align="right">64.35</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.77</td>
    <td align="right">68.15</td>
    <td align="right">68.30</td>
    <td align="right">68.10</td>
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
    <td align="right">34.86</td>
    <td align="right">50.79</td>
    <td align="right">50.77</td>
    <td align="right">50.76</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.33</td>
    <td align="right">21.48</td>
    <td align="right">21.31</td>
    <td align="right">21.54</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.40</td>
    <td align="right">26.39</td>
    <td align="right">26.37</td>
    <td align="right">26.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">94.93</td>
    <td align="right">111.25</td>
    <td align="right">110.94</td>
    <td align="right">110.82</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.90</td>
    <td align="right">31.69</td>
    <td align="right">31.90</td>
    <td align="right">31.91</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">25.63</td>
    <td align="right">32.80</td>
    <td align="right">32.86</td>
    <td align="right">32.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">193.44</td>
    <td align="right">207.61</td>
    <td align="right">207.73</td>
    <td align="right">207.66</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.54</td>
    <td align="right">47.50</td>
    <td align="right">47.54</td>
    <td align="right">47.50</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">40.12</td>
    <td align="right">54.45</td>
    <td align="right">54.06</td>
    <td align="right">54.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">300.77</td>
    <td align="right">421.09</td>
    <td align="right">440.06</td>
    <td align="right">454.20</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.10</td>
    <td align="right">65.71</td>
    <td align="right">65.21</td>
    <td align="right">65.87</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.58</td>
    <td align="right">68.23</td>
    <td align="right">68.07</td>
    <td align="right">68.21</td>
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
    <td align="right">23.86</td>
    <td align="right">28.23</td>
    <td align="right">30.74</td>
    <td align="right">33.28</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.77</td>
    <td align="right">31.85</td>
    <td align="right">31.34</td>
    <td align="right">35.20</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.39</td>
    <td align="right">18.95</td>
    <td align="right">26.63</td>
    <td align="right">24.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.60</td>
    <td align="right">45.49</td>
    <td align="right">38.41</td>
    <td align="right">46.68</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">52.82</td>
    <td align="right">52.05</td>
    <td align="right">45.86</td>
    <td align="right">53.08</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.83</td>
    <td align="right">26.81</td>
    <td align="right">33.00</td>
    <td align="right">31.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.38</td>
    <td align="right">77.74</td>
    <td align="right">49.64</td>
    <td align="right">70.03</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.86</td>
    <td align="right">82.87</td>
    <td align="right">66.55</td>
    <td align="right">76.96</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.25</td>
    <td align="right">44.55</td>
    <td align="right">44.54</td>
    <td align="right">47.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.56</td>
    <td align="right">98.89</td>
    <td align="right">56.62</td>
    <td align="right">88.81</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.66</td>
    <td align="right">108.30</td>
    <td align="right">87.20</td>
    <td align="right">98.29</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.64</td>
    <td align="right">75.88</td>
    <td align="right">50.15</td>
    <td align="right">74.18</td>
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
    <td align="right">24.88</td>
    <td align="right">29.04</td>
    <td align="right">29.10</td>
    <td align="right">29.12</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.85</td>
    <td align="right">32.35</td>
    <td align="right">32.35</td>
    <td align="right">32.36</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.73</td>
    <td align="right">19.96</td>
    <td align="right">18.95</td>
    <td align="right">19.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.68</td>
    <td align="right">44.16</td>
    <td align="right">44.32</td>
    <td align="right">44.23</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.45</td>
    <td align="right">52.99</td>
    <td align="right">53.01</td>
    <td align="right">54.63</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.60</td>
    <td align="right">27.78</td>
    <td align="right">28.39</td>
    <td align="right">28.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.69</td>
    <td align="right">71.94</td>
    <td align="right">72.19</td>
    <td align="right">71.98</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">101.90</td>
    <td align="right">81.39</td>
    <td align="right">81.39</td>
    <td align="right">81.45</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.37</td>
    <td align="right">44.90</td>
    <td align="right">44.88</td>
    <td align="right">45.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.58</td>
    <td align="right">92.91</td>
    <td align="right">93.06</td>
    <td align="right">93.17</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">135.18</td>
    <td align="right">110.99</td>
    <td align="right">110.89</td>
    <td align="right">110.96</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.76</td>
    <td align="right">75.79</td>
    <td align="right">75.74</td>
    <td align="right">75.76</td>
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
    <td align="right">23.51</td>
    <td align="right">27.98</td>
    <td align="right">30.80</td>
    <td align="right">32.86</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.59</td>
    <td align="right">33.53</td>
    <td align="right">32.12</td>
    <td align="right">35.81</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">16.10</td>
    <td align="right">19.48</td>
    <td align="right">26.91</td>
    <td align="right">25.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.01</td>
    <td align="right">45.83</td>
    <td align="right">38.07</td>
    <td align="right">47.05</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">55.18</td>
    <td align="right">54.23</td>
    <td align="right">46.82</td>
    <td align="right">55.26</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">24.32</td>
    <td align="right">25.04</td>
    <td align="right">31.84</td>
    <td align="right">30.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.39</td>
    <td align="right">75.53</td>
    <td align="right">48.50</td>
    <td align="right">68.02</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.27</td>
    <td align="right">85.99</td>
    <td align="right">68.41</td>
    <td align="right">79.23</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.49</td>
    <td align="right">44.38</td>
    <td align="right">44.00</td>
    <td align="right">47.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.18</td>
    <td align="right">98.38</td>
    <td align="right">56.65</td>
    <td align="right">88.13</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.28</td>
    <td align="right">109.18</td>
    <td align="right">87.84</td>
    <td align="right">99.02</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.89</td>
    <td align="right">75.75</td>
    <td align="right">49.81</td>
    <td align="right">73.50</td>
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
    <td align="right">24.58</td>
    <td align="right">28.52</td>
    <td align="right">28.58</td>
    <td align="right">28.56</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.38</td>
    <td align="right">32.09</td>
    <td align="right">31.95</td>
    <td align="right">32.05</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.88</td>
    <td align="right">19.44</td>
    <td align="right">18.89</td>
    <td align="right">19.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.47</td>
    <td align="right">44.37</td>
    <td align="right">44.35</td>
    <td align="right">44.49</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">52.52</td>
    <td align="right">51.31</td>
    <td align="right">52.32</td>
    <td align="right">51.79</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.44</td>
    <td align="right">26.64</td>
    <td align="right">26.60</td>
    <td align="right">25.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.28</td>
    <td align="right">71.37</td>
    <td align="right">71.32</td>
    <td align="right">71.35</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.67</td>
    <td align="right">83.81</td>
    <td align="right">83.78</td>
    <td align="right">83.82</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">43.17</td>
    <td align="right">45.99</td>
    <td align="right">46.03</td>
    <td align="right">46.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.65</td>
    <td align="right">93.41</td>
    <td align="right">93.52</td>
    <td align="right">93.35</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.18</td>
    <td align="right">108.57</td>
    <td align="right">108.56</td>
    <td align="right">108.46</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.99</td>
    <td align="right">75.16</td>
    <td align="right">75.03</td>
    <td align="right">75.16</td>
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
    <td align="right">15.20</td>
    <td align="right">17.74</td>
    <td align="right">27.51</td>
    <td align="right">25.27</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">22.10</td>
    <td align="right">26.73</td>
    <td align="right">29.20</td>
    <td align="right">31.87</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">31.15</td>
    <td align="right">35.40</td>
    <td align="right">33.22</td>
    <td align="right">38.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.55</td>
    <td align="right">30.09</td>
    <td align="right">37.01</td>
    <td align="right">35.91</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.85</td>
    <td align="right">45.44</td>
    <td align="right">38.85</td>
    <td align="right">46.57</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.46</td>
    <td align="right">53.30</td>
    <td align="right">47.22</td>
    <td align="right">54.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.91</td>
    <td align="right">46.44</td>
    <td align="right">50.45</td>
    <td align="right">50.36</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.89</td>
    <td align="right">79.11</td>
    <td align="right">50.02</td>
    <td align="right">71.63</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.33</td>
    <td align="right">83.30</td>
    <td align="right">67.22</td>
    <td align="right">77.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">83.17</td>
    <td align="right">80.62</td>
    <td align="right">59.53</td>
    <td align="right">78.23</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.88</td>
    <td align="right">100.37</td>
    <td align="right">56.83</td>
    <td align="right">88.74</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.60</td>
    <td align="right">109.05</td>
    <td align="right">87.87</td>
    <td align="right">99.19</td>
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
    <td align="right">17.14</td>
    <td align="right">20.17</td>
    <td align="right">20.11</td>
    <td align="right">20.14</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.20</td>
    <td align="right">28.34</td>
    <td align="right">28.30</td>
    <td align="right">28.35</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.41</td>
    <td align="right">31.89</td>
    <td align="right">32.04</td>
    <td align="right">31.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">29.75</td>
    <td align="right">32.27</td>
    <td align="right">32.24</td>
    <td align="right">32.30</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.66</td>
    <td align="right">43.76</td>
    <td align="right">43.76</td>
    <td align="right">43.73</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.91</td>
    <td align="right">51.93</td>
    <td align="right">51.57</td>
    <td align="right">53.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.96</td>
    <td align="right">57.64</td>
    <td align="right">57.87</td>
    <td align="right">58.60</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.73</td>
    <td align="right">72.79</td>
    <td align="right">72.82</td>
    <td align="right">72.54</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">101.71</td>
    <td align="right">82.88</td>
    <td align="right">82.62</td>
    <td align="right">82.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">83.72</td>
    <td align="right">86.00</td>
    <td align="right">85.96</td>
    <td align="right">86.61</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.73</td>
    <td align="right">95.22</td>
    <td align="right">95.48</td>
    <td align="right">96.92</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.19</td>
    <td align="right">110.40</td>
    <td align="right">110.46</td>
    <td align="right">110.52</td>
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
    <td align="right">17.45</td>
    <td align="right">19.74</td>
    <td align="right">29.76</td>
    <td align="right">26.61</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.48</td>
    <td align="right">27.82</td>
    <td align="right">30.03</td>
    <td align="right">33.06</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.36</td>
    <td align="right">34.63</td>
    <td align="right">33.12</td>
    <td align="right">37.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.66</td>
    <td align="right">31.29</td>
    <td align="right">40.78</td>
    <td align="right">37.37</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.93</td>
    <td align="right">46.18</td>
    <td align="right">39.00</td>
    <td align="right">47.17</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.14</td>
    <td align="right">53.43</td>
    <td align="right">46.77</td>
    <td align="right">54.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.69</td>
    <td align="right">47.27</td>
    <td align="right">51.53</td>
    <td align="right">52.24</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.90</td>
    <td align="right">80.42</td>
    <td align="right">51.74</td>
    <td align="right">73.11</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.26</td>
    <td align="right">82.83</td>
    <td align="right">66.64</td>
    <td align="right">76.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">84.85</td>
    <td align="right">83.22</td>
    <td align="right">60.63</td>
    <td align="right">80.85</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.11</td>
    <td align="right">97.17</td>
    <td align="right">56.64</td>
    <td align="right">91.09</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.46</td>
    <td align="right">109.81</td>
    <td align="right">88.42</td>
    <td align="right">99.56</td>
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
    <td align="right">16.70</td>
    <td align="right">19.47</td>
    <td align="right">19.41</td>
    <td align="right">19.45</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.01</td>
    <td align="right">28.03</td>
    <td align="right">28.17</td>
    <td align="right">28.00</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.26</td>
    <td align="right">31.92</td>
    <td align="right">31.96</td>
    <td align="right">31.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.45</td>
    <td align="right">32.22</td>
    <td align="right">32.24</td>
    <td align="right">32.33</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.09</td>
    <td align="right">43.96</td>
    <td align="right">44.08</td>
    <td align="right">44.00</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">55.00</td>
    <td align="right">49.39</td>
    <td align="right">49.38</td>
    <td align="right">49.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.61</td>
    <td align="right">55.52</td>
    <td align="right">55.59</td>
    <td align="right">55.58</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.71</td>
    <td align="right">74.13</td>
    <td align="right">74.19</td>
    <td align="right">74.26</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.84</td>
    <td align="right">82.06</td>
    <td align="right">82.14</td>
    <td align="right">82.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.37</td>
    <td align="right">83.76</td>
    <td align="right">83.42</td>
    <td align="right">83.40</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.97</td>
    <td align="right">91.99</td>
    <td align="right">92.16</td>
    <td align="right">92.12</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.34</td>
    <td align="right">110.35</td>
    <td align="right">110.44</td>
    <td align="right">110.45</td>
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
    <td align="right">22.02</td>
    <td align="right">29.26</td>
    <td align="right">31.96</td>
    <td align="right">34.35</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">37.36</td>
    <td align="right">40.08</td>
    <td align="right">41.02</td>
    <td align="right">40.51</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">36.47</td>
    <td align="right">45.73</td>
    <td align="right">41.31</td>
    <td align="right">43.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.86</td>
    <td align="right">51.88</td>
    <td align="right">39.44</td>
    <td align="right">50.75</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">60.16</td>
    <td align="right">60.38</td>
    <td align="right">47.37</td>
    <td align="right">58.18</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">61.76</td>
    <td align="right">68.82</td>
    <td align="right">46.08</td>
    <td align="right">61.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">66.42</td>
    <td align="right">72.72</td>
    <td align="right">47.14</td>
    <td align="right">68.23</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">86.58</td>
    <td align="right">88.08</td>
    <td align="right">60.08</td>
    <td align="right">80.05</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">90.91</td>
    <td align="right">94.14</td>
    <td align="right">44.74</td>
    <td align="right">78.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.83</td>
    <td align="right">90.99</td>
    <td align="right">56.80</td>
    <td align="right">84.55</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">105.76</td>
    <td align="right">106.61</td>
    <td align="right">68.31</td>
    <td align="right">95.86</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.76</td>
    <td align="right">143.60</td>
    <td align="right">51.82</td>
    <td align="right">113.35</td>
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
    <td align="right">21.84</td>
    <td align="right">28.94</td>
    <td align="right">29.24</td>
    <td align="right">29.24</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">37.05</td>
    <td align="right">38.05</td>
    <td align="right">37.94</td>
    <td align="right">39.42</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">33.77</td>
    <td align="right">38.05</td>
    <td align="right">38.17</td>
    <td align="right">38.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.26</td>
    <td align="right">48.12</td>
    <td align="right">48.05</td>
    <td align="right">48.09</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">61.07</td>
    <td align="right">58.29</td>
    <td align="right">58.33</td>
    <td align="right">58.26</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">64.44</td>
    <td align="right">67.88</td>
    <td align="right">68.06</td>
    <td align="right">67.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">66.06</td>
    <td align="right">70.57</td>
    <td align="right">70.68</td>
    <td align="right">70.62</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">86.82</td>
    <td align="right">87.65</td>
    <td align="right">87.58</td>
    <td align="right">87.65</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">89.80</td>
    <td align="right">95.22</td>
    <td align="right">95.15</td>
    <td align="right">95.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.69</td>
    <td align="right">89.24</td>
    <td align="right">88.90</td>
    <td align="right">89.16</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">103.65</td>
    <td align="right">103.85</td>
    <td align="right">103.86</td>
    <td align="right">103.88</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.13</td>
    <td align="right">141.36</td>
    <td align="right">140.25</td>
    <td align="right">140.55</td>
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
    <td align="right">21.59</td>
    <td align="right">28.90</td>
    <td align="right">31.26</td>
    <td align="right">33.16</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.99</td>
    <td align="right">38.78</td>
    <td align="right">42.07</td>
    <td align="right">39.47</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">35.76</td>
    <td align="right">44.70</td>
    <td align="right">40.95</td>
    <td align="right">44.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.37</td>
    <td align="right">50.48</td>
    <td align="right">37.60</td>
    <td align="right">49.42</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">61.05</td>
    <td align="right">61.05</td>
    <td align="right">47.21</td>
    <td align="right">58.64</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">62.88</td>
    <td align="right">68.45</td>
    <td align="right">46.11</td>
    <td align="right">60.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.78</td>
    <td align="right">72.53</td>
    <td align="right">46.91</td>
    <td align="right">67.86</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.26</td>
    <td align="right">88.85</td>
    <td align="right">60.25</td>
    <td align="right">80.34</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">89.60</td>
    <td align="right">95.40</td>
    <td align="right">45.87</td>
    <td align="right">79.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">84.02</td>
    <td align="right">89.90</td>
    <td align="right">56.20</td>
    <td align="right">83.58</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.15</td>
    <td align="right">104.45</td>
    <td align="right">68.17</td>
    <td align="right">94.01</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.42</td>
    <td align="right">142.14</td>
    <td align="right">52.24</td>
    <td align="right">110.60</td>
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
    <td align="right">21.33</td>
    <td align="right">28.64</td>
    <td align="right">28.63</td>
    <td align="right">28.36</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.70</td>
    <td align="right">36.95</td>
    <td align="right">36.97</td>
    <td align="right">37.00</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">34.83</td>
    <td align="right">39.55</td>
    <td align="right">39.48</td>
    <td align="right">39.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.84</td>
    <td align="right">47.06</td>
    <td align="right">46.96</td>
    <td align="right">46.99</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">60.03</td>
    <td align="right">58.63</td>
    <td align="right">59.63</td>
    <td align="right">58.96</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">63.69</td>
    <td align="right">61.02</td>
    <td align="right">61.10</td>
    <td align="right">60.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.96</td>
    <td align="right">70.42</td>
    <td align="right">70.37</td>
    <td align="right">70.34</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.29</td>
    <td align="right">86.81</td>
    <td align="right">86.79</td>
    <td align="right">86.80</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">91.48</td>
    <td align="right">93.76</td>
    <td align="right">93.85</td>
    <td align="right">93.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">84.21</td>
    <td align="right">89.16</td>
    <td align="right">89.12</td>
    <td align="right">89.15</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">106.03</td>
    <td align="right">106.03</td>
    <td align="right">106.02</td>
    <td align="right">105.99</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.45</td>
    <td align="right">142.69</td>
    <td align="right">142.92</td>
    <td align="right">144.11</td>
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
    <td align="right">79.68</td>
    <td align="right">14.44</td>
    <td align="right">8.57</td>
    <td align="right">18.10</td>
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
    <td align="right">28.32</td>
    <td align="right">29.52</td>
    <td align="right">29.10</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.47</td>
    <td align="right">14.08</td>
    <td align="right">13.94</td>
    <td align="right">14.09</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.84</td>
    <td align="right">18.04</td>
    <td align="right">18.04</td>
    <td align="right">18.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.64</td>
    <td align="right">42.51</td>
    <td align="right">31.41</td>
    <td align="right">37.53</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.04</td>
    <td align="right">18.41</td>
    <td align="right">18.41</td>
    <td align="right">18.42</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.21</td>
    <td align="right">20.89</td>
    <td align="right">20.76</td>
    <td align="right">20.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.05</td>
    <td align="right">65.63</td>
    <td align="right">32.19</td>
    <td align="right">47.68</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.69</td>
    <td align="right">21.19</td>
    <td align="right">21.22</td>
    <td align="right">21.36</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.13</td>
    <td align="right">22.98</td>
    <td align="right">22.89</td>
    <td align="right">22.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">63.62</td>
    <td align="right">76.48</td>
    <td align="right">33.06</td>
    <td align="right">60.05</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.27</td>
    <td align="right">23.28</td>
    <td align="right">23.21</td>
    <td align="right">23.28</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.10</td>
    <td align="right">25.76</td>
    <td align="right">25.80</td>
    <td align="right">25.79</td>
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
    <td align="right">21.57</td>
    <td align="right">30.08</td>
    <td align="right">30.02</td>
    <td align="right">30.14</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.46</td>
    <td align="right">13.92</td>
    <td align="right">13.92</td>
    <td align="right">13.93</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.85</td>
    <td align="right">18.06</td>
    <td align="right">18.09</td>
    <td align="right">18.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.54</td>
    <td align="right">46.10</td>
    <td align="right">46.28</td>
    <td align="right">46.46</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.05</td>
    <td align="right">18.44</td>
    <td align="right">18.44</td>
    <td align="right">18.47</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.23</td>
    <td align="right">20.76</td>
    <td align="right">20.75</td>
    <td align="right">20.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.38</td>
    <td align="right">57.30</td>
    <td align="right">57.76</td>
    <td align="right">58.14</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.68</td>
    <td align="right">21.21</td>
    <td align="right">21.31</td>
    <td align="right">21.25</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.10</td>
    <td align="right">22.99</td>
    <td align="right">22.94</td>
    <td align="right">23.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">63.73</td>
    <td align="right">73.61</td>
    <td align="right">72.68</td>
    <td align="right">72.70</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.21</td>
    <td align="right">23.21</td>
    <td align="right">23.28</td>
    <td align="right">23.20</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.12</td>
    <td align="right">25.77</td>
    <td align="right">25.73</td>
    <td align="right">25.74</td>
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
    <td align="right">21.51</td>
    <td align="right">31.35</td>
    <td align="right">29.38</td>
    <td align="right">30.97</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.46</td>
    <td align="right">14.07</td>
    <td align="right">13.93</td>
    <td align="right">13.93</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.86</td>
    <td align="right">18.06</td>
    <td align="right">18.07</td>
    <td align="right">18.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.86</td>
    <td align="right">48.03</td>
    <td align="right">31.38</td>
    <td align="right">40.48</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.16</td>
    <td align="right">18.44</td>
    <td align="right">18.41</td>
    <td align="right">18.40</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.30</td>
    <td align="right">20.91</td>
    <td align="right">20.75</td>
    <td align="right">20.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.51</td>
    <td align="right">64.21</td>
    <td align="right">34.44</td>
    <td align="right">51.13</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.59</td>
    <td align="right">21.18</td>
    <td align="right">21.36</td>
    <td align="right">21.22</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.07</td>
    <td align="right">22.94</td>
    <td align="right">22.95</td>
    <td align="right">22.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">68.03</td>
    <td align="right">80.71</td>
    <td align="right">35.29</td>
    <td align="right">60.08</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.29</td>
    <td align="right">23.33</td>
    <td align="right">23.32</td>
    <td align="right">23.31</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.10</td>
    <td align="right">25.72</td>
    <td align="right">25.75</td>
    <td align="right">25.78</td>
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
    <td align="right">21.60</td>
    <td align="right">30.41</td>
    <td align="right">30.28</td>
    <td align="right">30.27</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.46</td>
    <td align="right">13.93</td>
    <td align="right">13.91</td>
    <td align="right">13.95</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.88</td>
    <td align="right">18.08</td>
    <td align="right">18.02</td>
    <td align="right">18.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.54</td>
    <td align="right">46.26</td>
    <td align="right">46.31</td>
    <td align="right">46.23</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.18</td>
    <td align="right">18.43</td>
    <td align="right">18.42</td>
    <td align="right">18.42</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.20</td>
    <td align="right">20.79</td>
    <td align="right">20.92</td>
    <td align="right">20.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.41</td>
    <td align="right">56.67</td>
    <td align="right">56.90</td>
    <td align="right">56.53</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.69</td>
    <td align="right">21.19</td>
    <td align="right">21.32</td>
    <td align="right">21.19</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.11</td>
    <td align="right">22.95</td>
    <td align="right">22.99</td>
    <td align="right">22.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">66.08</td>
    <td align="right">69.17</td>
    <td align="right">72.15</td>
    <td align="right">69.79</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.20</td>
    <td align="right">23.22</td>
    <td align="right">23.29</td>
    <td align="right">23.22</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.09</td>
    <td align="right">25.85</td>
    <td align="right">25.84</td>
    <td align="right">25.74</td>
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
    <td align="right">20.17</td>
    <td align="right">23.39</td>
    <td align="right">24.13</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.07</td>
    <td align="right">19.69</td>
    <td align="right">23.05</td>
    <td align="right">23.34</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.98</td>
    <td align="right">8.98</td>
    <td align="right">18.51</td>
    <td align="right">15.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">27.43</td>
    <td align="right">25.10</td>
    <td align="right">28.79</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.65</td>
    <td align="right">27.50</td>
    <td align="right">24.88</td>
    <td align="right">28.70</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.95</td>
    <td align="right">12.98</td>
    <td align="right">20.60</td>
    <td align="right">19.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.07</td>
    <td align="right">37.69</td>
    <td align="right">26.70</td>
    <td align="right">34.39</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.45</td>
    <td align="right">35.84</td>
    <td align="right">25.78</td>
    <td align="right">33.21</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.86</td>
    <td align="right">15.15</td>
    <td align="right">29.55</td>
    <td align="right">21.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.71</td>
    <td align="right">41.28</td>
    <td align="right">25.91</td>
    <td align="right">36.45</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.45</td>
    <td align="right">43.05</td>
    <td align="right">26.49</td>
    <td align="right">37.02</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.15</td>
    <td align="right">19.77</td>
    <td align="right">21.19</td>
    <td align="right">24.35</td>
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
    <td align="right">17.08</td>
    <td align="right">18.35</td>
    <td align="right">18.37</td>
    <td align="right">18.35</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.02</td>
    <td align="right">18.88</td>
    <td align="right">18.85</td>
    <td align="right">18.85</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.98</td>
    <td align="right">8.72</td>
    <td align="right">8.73</td>
    <td align="right">8.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.60</td>
    <td align="right">26.58</td>
    <td align="right">26.53</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.65</td>
    <td align="right">27.02</td>
    <td align="right">27.00</td>
    <td align="right">27.05</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.97</td>
    <td align="right">13.79</td>
    <td align="right">13.77</td>
    <td align="right">13.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.08</td>
    <td align="right">35.48</td>
    <td align="right">35.46</td>
    <td align="right">35.47</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.40</td>
    <td align="right">34.34</td>
    <td align="right">34.30</td>
    <td align="right">34.29</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.86</td>
    <td align="right">17.85</td>
    <td align="right">17.84</td>
    <td align="right">17.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.75</td>
    <td align="right">38.50</td>
    <td align="right">38.51</td>
    <td align="right">38.51</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.47</td>
    <td align="right">41.51</td>
    <td align="right">41.46</td>
    <td align="right">41.30</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.15</td>
    <td align="right">19.75</td>
    <td align="right">19.78</td>
    <td align="right">19.74</td>
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
    <td align="right">17.08</td>
    <td align="right">20.63</td>
    <td align="right">23.95</td>
    <td align="right">24.38</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.08</td>
    <td align="right">19.89</td>
    <td align="right">23.33</td>
    <td align="right">23.08</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.58</td>
    <td align="right">8.94</td>
    <td align="right">18.36</td>
    <td align="right">15.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">27.26</td>
    <td align="right">25.18</td>
    <td align="right">28.62</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.13</td>
    <td align="right">26.75</td>
    <td align="right">24.86</td>
    <td align="right">28.29</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.95</td>
    <td align="right">13.62</td>
    <td align="right">20.55</td>
    <td align="right">19.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">34.12</td>
    <td align="right">36.72</td>
    <td align="right">26.36</td>
    <td align="right">33.88</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.52</td>
    <td align="right">35.91</td>
    <td align="right">25.40</td>
    <td align="right">33.15</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.87</td>
    <td align="right">17.13</td>
    <td align="right">22.03</td>
    <td align="right">22.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.51</td>
    <td align="right">40.54</td>
    <td align="right">25.71</td>
    <td align="right">35.95</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.35</td>
    <td align="right">42.90</td>
    <td align="right">26.41</td>
    <td align="right">37.02</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.08</td>
    <td align="right">20.13</td>
    <td align="right">21.35</td>
    <td align="right">24.82</td>
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
    <td align="right">17.06</td>
    <td align="right">18.41</td>
    <td align="right">18.29</td>
    <td align="right">18.43</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.22</td>
    <td align="right">18.87</td>
    <td align="right">18.89</td>
    <td align="right">18.88</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.59</td>
    <td align="right">8.74</td>
    <td align="right">8.73</td>
    <td align="right">8.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">26.55</td>
    <td align="right">26.60</td>
    <td align="right">26.60</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.12</td>
    <td align="right">27.01</td>
    <td align="right">27.00</td>
    <td align="right">27.02</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.94</td>
    <td align="right">13.75</td>
    <td align="right">13.74</td>
    <td align="right">13.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">34.14</td>
    <td align="right">35.29</td>
    <td align="right">35.30</td>
    <td align="right">35.27</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.55</td>
    <td align="right">34.32</td>
    <td align="right">34.36</td>
    <td align="right">34.31</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.88</td>
    <td align="right">17.24</td>
    <td align="right">17.22</td>
    <td align="right">17.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.55</td>
    <td align="right">39.12</td>
    <td align="right">39.13</td>
    <td align="right">39.14</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.23</td>
    <td align="right">41.27</td>
    <td align="right">41.19</td>
    <td align="right">41.48</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.09</td>
    <td align="right">19.89</td>
    <td align="right">19.89</td>
    <td align="right">19.90</td>
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
    <td align="right">7.68</td>
    <td align="right">8.77</td>
    <td align="right">17.90</td>
    <td align="right">15.34</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.04</td>
    <td align="right">20.12</td>
    <td align="right">23.42</td>
    <td align="right">24.09</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.07</td>
    <td align="right">19.62</td>
    <td align="right">23.07</td>
    <td align="right">23.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.94</td>
    <td align="right">13.65</td>
    <td align="right">20.52</td>
    <td align="right">19.41</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">27.44</td>
    <td align="right">25.11</td>
    <td align="right">28.78</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.63</td>
    <td align="right">27.49</td>
    <td align="right">24.91</td>
    <td align="right">28.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.30</td>
    <td align="right">16.08</td>
    <td align="right">21.36</td>
    <td align="right">22.48</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.07</td>
    <td align="right">37.51</td>
    <td align="right">26.69</td>
    <td align="right">34.43</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.46</td>
    <td align="right">35.84</td>
    <td align="right">25.76</td>
    <td align="right">33.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.83</td>
    <td align="right">19.28</td>
    <td align="right">20.87</td>
    <td align="right">23.71</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.80</td>
    <td align="right">41.37</td>
    <td align="right">25.96</td>
    <td align="right">36.57</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.37</td>
    <td align="right">42.97</td>
    <td align="right">26.51</td>
    <td align="right">37.16</td>
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
    <td align="right">7.71</td>
    <td align="right">8.59</td>
    <td align="right">8.52</td>
    <td align="right">8.53</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.06</td>
    <td align="right">18.33</td>
    <td align="right">18.52</td>
    <td align="right">18.46</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.04</td>
    <td align="right">18.97</td>
    <td align="right">18.87</td>
    <td align="right">18.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.74</td>
    <td align="right">14.12</td>
    <td align="right">14.12</td>
    <td align="right">14.12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.60</td>
    <td align="right">26.59</td>
    <td align="right">26.54</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.63</td>
    <td align="right">27.03</td>
    <td align="right">27.05</td>
    <td align="right">27.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.21</td>
    <td align="right">17.23</td>
    <td align="right">17.26</td>
    <td align="right">17.25</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.14</td>
    <td align="right">35.48</td>
    <td align="right">35.52</td>
    <td align="right">35.48</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.39</td>
    <td align="right">34.31</td>
    <td align="right">34.44</td>
    <td align="right">34.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.82</td>
    <td align="right">20.07</td>
    <td align="right">20.06</td>
    <td align="right">20.07</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.78</td>
    <td align="right">38.53</td>
    <td align="right">38.50</td>
    <td align="right">38.52</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.36</td>
    <td align="right">41.51</td>
    <td align="right">41.41</td>
    <td align="right">41.27</td>
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
    <td align="right">7.10</td>
    <td align="right">8.55</td>
    <td align="right">17.88</td>
    <td align="right">14.87</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.08</td>
    <td align="right">20.61</td>
    <td align="right">23.95</td>
    <td align="right">24.45</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.16</td>
    <td align="right">19.85</td>
    <td align="right">23.34</td>
    <td align="right">23.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.82</td>
    <td align="right">13.60</td>
    <td align="right">20.38</td>
    <td align="right">19.56</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">27.00</td>
    <td align="right">25.18</td>
    <td align="right">28.60</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.13</td>
    <td align="right">26.75</td>
    <td align="right">24.88</td>
    <td align="right">28.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.21</td>
    <td align="right">16.51</td>
    <td align="right">21.26</td>
    <td align="right">22.60</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">34.11</td>
    <td align="right">36.85</td>
    <td align="right">26.39</td>
    <td align="right">33.86</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.52</td>
    <td align="right">36.09</td>
    <td align="right">25.36</td>
    <td align="right">33.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.80</td>
    <td align="right">19.21</td>
    <td align="right">20.97</td>
    <td align="right">24.44</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.53</td>
    <td align="right">40.55</td>
    <td align="right">25.67</td>
    <td align="right">35.96</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.26</td>
    <td align="right">42.91</td>
    <td align="right">26.41</td>
    <td align="right">37.01</td>
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
    <td align="right">8.54</td>
    <td align="right">8.48</td>
    <td align="right">8.50</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.04</td>
    <td align="right">18.29</td>
    <td align="right">18.41</td>
    <td align="right">18.29</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.17</td>
    <td align="right">18.88</td>
    <td align="right">18.88</td>
    <td align="right">18.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.88</td>
    <td align="right">14.12</td>
    <td align="right">14.11</td>
    <td align="right">14.12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">26.46</td>
    <td align="right">26.60</td>
    <td align="right">26.61</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">25.16</td>
    <td align="right">27.01</td>
    <td align="right">27.00</td>
    <td align="right">27.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.30</td>
    <td align="right">17.27</td>
    <td align="right">17.25</td>
    <td align="right">17.26</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">34.11</td>
    <td align="right">35.30</td>
    <td align="right">35.35</td>
    <td align="right">35.32</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.46</td>
    <td align="right">34.29</td>
    <td align="right">34.32</td>
    <td align="right">34.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.83</td>
    <td align="right">20.07</td>
    <td align="right">20.05</td>
    <td align="right">20.05</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.57</td>
    <td align="right">39.15</td>
    <td align="right">39.13</td>
    <td align="right">39.13</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.26</td>
    <td align="right">41.27</td>
    <td align="right">41.18</td>
    <td align="right">41.51</td>
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
    <td align="right">18.23</td>
    <td align="right">20.94</td>
    <td align="right">24.57</td>
    <td align="right">25.01</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.86</td>
    <td align="right">41.77</td>
    <td align="right">41.21</td>
    <td align="right">41.61</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">27.12</td>
    <td align="right">29.41</td>
    <td align="right">29.24</td>
    <td align="right">29.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.04</td>
    <td align="right">30.01</td>
    <td align="right">24.20</td>
    <td align="right">30.08</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.61</td>
    <td align="right">46.13</td>
    <td align="right">40.02</td>
    <td align="right">43.28</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.70</td>
    <td align="right">38.80</td>
    <td align="right">29.94</td>
    <td align="right">35.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.12</td>
    <td align="right">35.87</td>
    <td align="right">24.51</td>
    <td align="right">33.54</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.65</td>
    <td align="right">53.93</td>
    <td align="right">40.27</td>
    <td align="right">47.29</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.92</td>
    <td align="right">45.73</td>
    <td align="right">31.55</td>
    <td align="right">41.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.80</td>
    <td align="right">46.78</td>
    <td align="right">30.15</td>
    <td align="right">41.58</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">63.64</td>
    <td align="right">58.65</td>
    <td align="right">43.69</td>
    <td align="right">51.31</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.38</td>
    <td align="right">58.17</td>
    <td align="right">33.02</td>
    <td align="right">47.68</td>
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
    <td align="right">18.30</td>
    <td align="right">20.12</td>
    <td align="right">20.13</td>
    <td align="right">20.13</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.83</td>
    <td align="right">37.67</td>
    <td align="right">37.86</td>
    <td align="right">37.97</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">27.19</td>
    <td align="right">27.55</td>
    <td align="right">27.34</td>
    <td align="right">27.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.03</td>
    <td align="right">28.46</td>
    <td align="right">28.45</td>
    <td align="right">28.45</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.52</td>
    <td align="right">44.23</td>
    <td align="right">43.94</td>
    <td align="right">44.01</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.59</td>
    <td align="right">36.12</td>
    <td align="right">36.26</td>
    <td align="right">36.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.18</td>
    <td align="right">34.35</td>
    <td align="right">34.32</td>
    <td align="right">34.33</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">59.88</td>
    <td align="right">48.57</td>
    <td align="right">48.91</td>
    <td align="right">48.63</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.88</td>
    <td align="right">38.66</td>
    <td align="right">38.62</td>
    <td align="right">38.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.78</td>
    <td align="right">39.31</td>
    <td align="right">39.30</td>
    <td align="right">39.34</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.16</td>
    <td align="right">53.13</td>
    <td align="right">52.54</td>
    <td align="right">52.61</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.27</td>
    <td align="right">50.55</td>
    <td align="right">50.96</td>
    <td align="right">50.46</td>
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
    <td align="right">18.22</td>
    <td align="right">20.93</td>
    <td align="right">24.58</td>
    <td align="right">24.97</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">48.32</td>
    <td align="right">42.02</td>
    <td align="right">41.37</td>
    <td align="right">41.55</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.91</td>
    <td align="right">29.53</td>
    <td align="right">28.87</td>
    <td align="right">29.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.03</td>
    <td align="right">29.43</td>
    <td align="right">24.22</td>
    <td align="right">30.15</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.60</td>
    <td align="right">45.96</td>
    <td align="right">39.64</td>
    <td align="right">43.26</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.56</td>
    <td align="right">39.07</td>
    <td align="right">29.88</td>
    <td align="right">35.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.14</td>
    <td align="right">35.70</td>
    <td align="right">24.67</td>
    <td align="right">33.29</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.55</td>
    <td align="right">54.65</td>
    <td align="right">40.58</td>
    <td align="right">47.73</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.58</td>
    <td align="right">45.47</td>
    <td align="right">31.39</td>
    <td align="right">40.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.76</td>
    <td align="right">46.79</td>
    <td align="right">29.79</td>
    <td align="right">41.81</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">63.67</td>
    <td align="right">58.94</td>
    <td align="right">43.68</td>
    <td align="right">52.10</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.42</td>
    <td align="right">58.41</td>
    <td align="right">33.17</td>
    <td align="right">47.59</td>
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
    <td align="right">18.26</td>
    <td align="right">20.07</td>
    <td align="right">20.06</td>
    <td align="right">20.06</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">49.20</td>
    <td align="right">38.27</td>
    <td align="right">37.78</td>
    <td align="right">38.06</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">27.09</td>
    <td align="right">27.32</td>
    <td align="right">27.52</td>
    <td align="right">27.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.02</td>
    <td align="right">28.45</td>
    <td align="right">28.46</td>
    <td align="right">28.42</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">53.51</td>
    <td align="right">43.11</td>
    <td align="right">43.26</td>
    <td align="right">43.05</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.63</td>
    <td align="right">35.55</td>
    <td align="right">35.43</td>
    <td align="right">35.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.14</td>
    <td align="right">34.32</td>
    <td align="right">34.29</td>
    <td align="right">34.30</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">61.16</td>
    <td align="right">48.54</td>
    <td align="right">50.39</td>
    <td align="right">48.55</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.80</td>
    <td align="right">38.78</td>
    <td align="right">38.65</td>
    <td align="right">38.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.76</td>
    <td align="right">39.29</td>
    <td align="right">39.28</td>
    <td align="right">39.31</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">63.83</td>
    <td align="right">52.21</td>
    <td align="right">52.74</td>
    <td align="right">52.29</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.45</td>
    <td align="right">50.57</td>
    <td align="right">50.32</td>
    <td align="right">50.32</td>
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
    <td align="right">124.07</td>
    <td align="right">61.65</td>
    <td align="right">22.42</td>
    <td align="right">53.97</td>
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
    <td align="right">26.70</td>
    <td align="right">34.85</td>
    <td align="right">34.44</td>
    <td align="right">35.53</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.18</td>
    <td align="right">16.69</td>
    <td align="right">16.68</td>
    <td align="right">16.75</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.26</td>
    <td align="right">19.29</td>
    <td align="right">19.29</td>
    <td align="right">19.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">75.41</td>
    <td align="right">91.88</td>
    <td align="right">45.73</td>
    <td align="right">69.66</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.10</td>
    <td align="right">28.30</td>
    <td align="right">28.10</td>
    <td align="right">28.35</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.34</td>
    <td align="right">33.47</td>
    <td align="right">33.39</td>
    <td align="right">33.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">144.39</td>
    <td align="right">207.24</td>
    <td align="right">66.04</td>
    <td align="right">134.00</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">39.59</td>
    <td align="right">49.03</td>
    <td align="right">48.94</td>
    <td align="right">48.99</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.94</td>
    <td align="right">52.34</td>
    <td align="right">52.18</td>
    <td align="right">52.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">249.26</td>
    <td align="right">327.42</td>
    <td align="right">82.95</td>
    <td align="right">191.90</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">65.79</td>
    <td align="right">65.43</td>
    <td align="right">65.32</td>
    <td align="right">65.19</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">68.05</td>
    <td align="right">69.32</td>
    <td align="right">69.38</td>
    <td align="right">69.32</td>
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
    <td align="right">28.21</td>
    <td align="right">38.50</td>
    <td align="right">38.15</td>
    <td align="right">38.27</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.85</td>
    <td align="right">16.36</td>
    <td align="right">16.28</td>
    <td align="right">16.35</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">19.55</td>
    <td align="right">21.61</td>
    <td align="right">21.68</td>
    <td align="right">21.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">76.76</td>
    <td align="right">100.67</td>
    <td align="right">101.01</td>
    <td align="right">101.56</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.99</td>
    <td align="right">28.50</td>
    <td align="right">28.55</td>
    <td align="right">28.59</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.90</td>
    <td align="right">33.78</td>
    <td align="right">34.01</td>
    <td align="right">34.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">144.06</td>
    <td align="right">193.24</td>
    <td align="right">193.44</td>
    <td align="right">193.68</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">39.74</td>
    <td align="right">49.24</td>
    <td align="right">49.16</td>
    <td align="right">49.36</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">52.21</td>
    <td align="right">51.07</td>
    <td align="right">51.04</td>
    <td align="right">51.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">249.62</td>
    <td align="right">300.63</td>
    <td align="right">296.71</td>
    <td align="right">301.10</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.36</td>
    <td align="right">65.10</td>
    <td align="right">65.27</td>
    <td align="right">65.09</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.80</td>
    <td align="right">69.28</td>
    <td align="right">69.01</td>
    <td align="right">69.14</td>
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
    <td align="right">29.41</td>
    <td align="right">40.54</td>
    <td align="right">34.62</td>
    <td align="right">38.86</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.26</td>
    <td align="right">16.83</td>
    <td align="right">16.80</td>
    <td align="right">16.90</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.74</td>
    <td align="right">20.78</td>
    <td align="right">20.78</td>
    <td align="right">20.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">76.98</td>
    <td align="right">101.62</td>
    <td align="right">45.13</td>
    <td align="right">74.83</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.07</td>
    <td align="right">28.17</td>
    <td align="right">28.18</td>
    <td align="right">28.15</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">29.00</td>
    <td align="right">34.93</td>
    <td align="right">34.87</td>
    <td align="right">34.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">142.75</td>
    <td align="right">206.53</td>
    <td align="right">67.84</td>
    <td align="right">135.56</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.35</td>
    <td align="right">49.50</td>
    <td align="right">49.62</td>
    <td align="right">49.57</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.57</td>
    <td align="right">50.62</td>
    <td align="right">50.32</td>
    <td align="right">50.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">265.17</td>
    <td align="right">317.06</td>
    <td align="right">85.20</td>
    <td align="right">204.48</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.09</td>
    <td align="right">63.46</td>
    <td align="right">63.38</td>
    <td align="right">63.45</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.43</td>
    <td align="right">68.77</td>
    <td align="right">68.81</td>
    <td align="right">68.96</td>
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
    <td align="right">36.37</td>
    <td align="right">47.02</td>
    <td align="right">47.41</td>
    <td align="right">47.36</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.49</td>
    <td align="right">17.03</td>
    <td align="right">16.98</td>
    <td align="right">17.05</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.73</td>
    <td align="right">20.76</td>
    <td align="right">20.89</td>
    <td align="right">20.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">77.11</td>
    <td align="right">102.29</td>
    <td align="right">102.08</td>
    <td align="right">109.38</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.04</td>
    <td align="right">26.62</td>
    <td align="right">26.56</td>
    <td align="right">26.67</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.17</td>
    <td align="right">33.71</td>
    <td align="right">33.71</td>
    <td align="right">33.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">145.15</td>
    <td align="right">187.65</td>
    <td align="right">187.85</td>
    <td align="right">187.71</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">41.08</td>
    <td align="right">49.31</td>
    <td align="right">49.41</td>
    <td align="right">49.32</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">52.00</td>
    <td align="right">51.58</td>
    <td align="right">51.46</td>
    <td align="right">51.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">263.99</td>
    <td align="right">289.39</td>
    <td align="right">289.09</td>
    <td align="right">291.43</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.14</td>
    <td align="right">63.44</td>
    <td align="right">63.49</td>
    <td align="right">63.48</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.63</td>
    <td align="right">67.59</td>
    <td align="right">67.47</td>
    <td align="right">67.57</td>
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
    <td align="right">20.69</td>
    <td align="right">24.63</td>
    <td align="right">26.17</td>
    <td align="right">29.82</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.64</td>
    <td align="right">23.56</td>
    <td align="right">25.97</td>
    <td align="right">27.84</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">9.28</td>
    <td align="right">10.38</td>
    <td align="right">20.08</td>
    <td align="right">17.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.61</td>
    <td align="right">41.02</td>
    <td align="right">33.20</td>
    <td align="right">42.42</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.26</td>
    <td align="right">39.66</td>
    <td align="right">31.41</td>
    <td align="right">39.80</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.82</td>
    <td align="right">22.64</td>
    <td align="right">27.46</td>
    <td align="right">28.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.06</td>
    <td align="right">71.36</td>
    <td align="right">42.97</td>
    <td align="right">65.11</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.04</td>
    <td align="right">68.94</td>
    <td align="right">42.74</td>
    <td align="right">63.46</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.14</td>
    <td align="right">37.61</td>
    <td align="right">55.92</td>
    <td align="right">40.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.75</td>
    <td align="right">91.80</td>
    <td align="right">47.74</td>
    <td align="right">81.78</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.99</td>
    <td align="right">93.22</td>
    <td align="right">50.05</td>
    <td align="right">82.90</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.18</td>
    <td align="right">51.68</td>
    <td align="right">38.79</td>
    <td align="right">51.95</td>
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
    <td align="right">20.20</td>
    <td align="right">21.52</td>
    <td align="right">21.80</td>
    <td align="right">21.64</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">18.23</td>
    <td align="right">21.21</td>
    <td align="right">21.24</td>
    <td align="right">21.23</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">9.85</td>
    <td align="right">10.61</td>
    <td align="right">11.03</td>
    <td align="right">10.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.03</td>
    <td align="right">40.47</td>
    <td align="right">40.34</td>
    <td align="right">40.31</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.92</td>
    <td align="right">41.47</td>
    <td align="right">41.27</td>
    <td align="right">41.55</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">20.05</td>
    <td align="right">21.84</td>
    <td align="right">22.11</td>
    <td align="right">22.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.11</td>
    <td align="right">66.69</td>
    <td align="right">66.52</td>
    <td align="right">66.69</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.66</td>
    <td align="right">68.91</td>
    <td align="right">68.98</td>
    <td align="right">68.92</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.57</td>
    <td align="right">40.81</td>
    <td align="right">40.74</td>
    <td align="right">41.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.36</td>
    <td align="right">87.07</td>
    <td align="right">87.12</td>
    <td align="right">87.20</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">95.80</td>
    <td align="right">94.88</td>
    <td align="right">93.55</td>
    <td align="right">93.44</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">52.94</td>
    <td align="right">51.33</td>
    <td align="right">51.59</td>
    <td align="right">51.33</td>
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
    <td align="right">18.88</td>
    <td align="right">22.85</td>
    <td align="right">25.62</td>
    <td align="right">28.17</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.74</td>
    <td align="right">23.39</td>
    <td align="right">25.53</td>
    <td align="right">26.65</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">9.12</td>
    <td align="right">10.51</td>
    <td align="right">19.97</td>
    <td align="right">18.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.88</td>
    <td align="right">38.38</td>
    <td align="right">32.56</td>
    <td align="right">40.66</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.60</td>
    <td align="right">43.28</td>
    <td align="right">33.31</td>
    <td align="right">42.55</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">22.29</td>
    <td align="right">21.81</td>
    <td align="right">26.40</td>
    <td align="right">26.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">69.25</td>
    <td align="right">72.13</td>
    <td align="right">43.39</td>
    <td align="right">65.52</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">69.57</td>
    <td align="right">70.47</td>
    <td align="right">43.08</td>
    <td align="right">64.84</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">37.83</td>
    <td align="right">40.20</td>
    <td align="right">34.82</td>
    <td align="right">41.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.44</td>
    <td align="right">89.38</td>
    <td align="right">46.81</td>
    <td align="right">79.37</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.69</td>
    <td align="right">93.54</td>
    <td align="right">50.13</td>
    <td align="right">82.99</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">52.96</td>
    <td align="right">53.06</td>
    <td align="right">38.66</td>
    <td align="right">53.21</td>
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
    <td align="right">19.70</td>
    <td align="right">21.18</td>
    <td align="right">21.12</td>
    <td align="right">21.10</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.82</td>
    <td align="right">22.10</td>
    <td align="right">22.33</td>
    <td align="right">22.12</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">10.12</td>
    <td align="right">11.44</td>
    <td align="right">11.44</td>
    <td align="right">11.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.54</td>
    <td align="right">37.65</td>
    <td align="right">37.81</td>
    <td align="right">37.77</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">41.04</td>
    <td align="right">40.29</td>
    <td align="right">40.31</td>
    <td align="right">40.36</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">22.28</td>
    <td align="right">23.62</td>
    <td align="right">23.62</td>
    <td align="right">23.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.59</td>
    <td align="right">69.82</td>
    <td align="right">68.27</td>
    <td align="right">68.02</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">69.70</td>
    <td align="right">68.32</td>
    <td align="right">68.55</td>
    <td align="right">68.28</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.33</td>
    <td align="right">40.94</td>
    <td align="right">40.67</td>
    <td align="right">40.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.19</td>
    <td align="right">89.02</td>
    <td align="right">88.97</td>
    <td align="right">88.99</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.01</td>
    <td align="right">91.15</td>
    <td align="right">90.96</td>
    <td align="right">92.29</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.01</td>
    <td align="right">52.60</td>
    <td align="right">52.51</td>
    <td align="right">52.30</td>
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
    <td align="right">9.36</td>
    <td align="right">10.61</td>
    <td align="right">20.05</td>
    <td align="right">17.87</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.13</td>
    <td align="right">22.68</td>
    <td align="right">25.20</td>
    <td align="right">27.97</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">18.48</td>
    <td align="right">21.59</td>
    <td align="right">24.66</td>
    <td align="right">26.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.15</td>
    <td align="right">22.85</td>
    <td align="right">26.32</td>
    <td align="right">27.20</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.43</td>
    <td align="right">39.00</td>
    <td align="right">32.34</td>
    <td align="right">40.60</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.13</td>
    <td align="right">45.25</td>
    <td align="right">34.02</td>
    <td align="right">45.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.25</td>
    <td align="right">40.92</td>
    <td align="right">35.07</td>
    <td align="right">41.66</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.02</td>
    <td align="right">70.97</td>
    <td align="right">42.72</td>
    <td align="right">65.37</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.29</td>
    <td align="right">71.51</td>
    <td align="right">43.68</td>
    <td align="right">65.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.09</td>
    <td align="right">52.78</td>
    <td align="right">38.09</td>
    <td align="right">52.76</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.22</td>
    <td align="right">89.75</td>
    <td align="right">47.02</td>
    <td align="right">79.90</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.41</td>
    <td align="right">94.82</td>
    <td align="right">50.39</td>
    <td align="right">84.08</td>
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
    <td align="right">9.62</td>
    <td align="right">11.17</td>
    <td align="right">11.14</td>
    <td align="right">11.00</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">18.55</td>
    <td align="right">20.24</td>
    <td align="right">20.35</td>
    <td align="right">20.51</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.22</td>
    <td align="right">22.88</td>
    <td align="right">23.00</td>
    <td align="right">22.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.23</td>
    <td align="right">25.03</td>
    <td align="right">25.44</td>
    <td align="right">25.64</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.25</td>
    <td align="right">40.20</td>
    <td align="right">40.24</td>
    <td align="right">40.12</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.57</td>
    <td align="right">44.35</td>
    <td align="right">44.39</td>
    <td align="right">44.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.01</td>
    <td align="right">40.76</td>
    <td align="right">40.81</td>
    <td align="right">40.91</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.16</td>
    <td align="right">69.96</td>
    <td align="right">69.88</td>
    <td align="right">69.88</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">69.96</td>
    <td align="right">68.81</td>
    <td align="right">69.18</td>
    <td align="right">68.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">52.77</td>
    <td align="right">52.77</td>
    <td align="right">55.27</td>
    <td align="right">53.64</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.85</td>
    <td align="right">86.24</td>
    <td align="right">86.20</td>
    <td align="right">86.22</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.51</td>
    <td align="right">92.24</td>
    <td align="right">91.10</td>
    <td align="right">91.01</td>
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
    <td align="right">9.05</td>
    <td align="right">10.49</td>
    <td align="right">19.89</td>
    <td align="right">17.40</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.58</td>
    <td align="right">24.84</td>
    <td align="right">26.75</td>
    <td align="right">30.12</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.15</td>
    <td align="right">22.38</td>
    <td align="right">25.17</td>
    <td align="right">27.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">22.99</td>
    <td align="right">22.65</td>
    <td align="right">26.14</td>
    <td align="right">27.21</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.06</td>
    <td align="right">36.44</td>
    <td align="right">31.14</td>
    <td align="right">38.15</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">41.56</td>
    <td align="right">43.99</td>
    <td align="right">33.38</td>
    <td align="right">43.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.51</td>
    <td align="right">39.82</td>
    <td align="right">34.00</td>
    <td align="right">41.06</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.00</td>
    <td align="right">69.26</td>
    <td align="right">42.14</td>
    <td align="right">62.74</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.01</td>
    <td align="right">71.04</td>
    <td align="right">43.12</td>
    <td align="right">65.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.13</td>
    <td align="right">52.83</td>
    <td align="right">37.97</td>
    <td align="right">53.40</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.43</td>
    <td align="right">90.83</td>
    <td align="right">47.37</td>
    <td align="right">82.31</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.32</td>
    <td align="right">93.14</td>
    <td align="right">49.82</td>
    <td align="right">82.64</td>
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
    <td align="right">8.66</td>
    <td align="right">10.54</td>
    <td align="right">10.29</td>
    <td align="right">10.31</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">18.52</td>
    <td align="right">20.28</td>
    <td align="right">20.19</td>
    <td align="right">20.25</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.93</td>
    <td align="right">22.46</td>
    <td align="right">22.44</td>
    <td align="right">22.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.18</td>
    <td align="right">25.85</td>
    <td align="right">26.13</td>
    <td align="right">25.71</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.77</td>
    <td align="right">37.66</td>
    <td align="right">37.76</td>
    <td align="right">37.84</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.48</td>
    <td align="right">45.13</td>
    <td align="right">45.02</td>
    <td align="right">45.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.95</td>
    <td align="right">40.99</td>
    <td align="right">40.83</td>
    <td align="right">41.03</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.41</td>
    <td align="right">68.42</td>
    <td align="right">68.41</td>
    <td align="right">68.46</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">69.78</td>
    <td align="right">66.92</td>
    <td align="right">67.14</td>
    <td align="right">66.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">52.98</td>
    <td align="right">52.96</td>
    <td align="right">52.84</td>
    <td align="right">52.81</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.74</td>
    <td align="right">89.11</td>
    <td align="right">89.13</td>
    <td align="right">89.15</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">95.59</td>
    <td align="right">93.37</td>
    <td align="right">93.16</td>
    <td align="right">94.60</td>
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
    <td align="right">21.22</td>
    <td align="right">24.88</td>
    <td align="right">27.11</td>
    <td align="right">30.18</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">51.22</td>
    <td align="right">45.06</td>
    <td align="right">44.64</td>
    <td align="right">45.20</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">32.32</td>
    <td align="right">34.66</td>
    <td align="right">31.55</td>
    <td align="right">34.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.93</td>
    <td align="right">39.82</td>
    <td align="right">30.42</td>
    <td align="right">40.49</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">63.63</td>
    <td align="right">60.99</td>
    <td align="right">50.31</td>
    <td align="right">56.57</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">58.23</td>
    <td align="right">61.08</td>
    <td align="right">38.92</td>
    <td align="right">53.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">61.91</td>
    <td align="right">64.74</td>
    <td align="right">40.96</td>
    <td align="right">61.85</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">89.58</td>
    <td align="right">87.21</td>
    <td align="right">63.46</td>
    <td align="right">79.09</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.91</td>
    <td align="right">88.85</td>
    <td align="right">42.33</td>
    <td align="right">74.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.53</td>
    <td align="right">89.37</td>
    <td align="right">57.56</td>
    <td align="right">84.03</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.70</td>
    <td align="right">106.76</td>
    <td align="right">78.69</td>
    <td align="right">96.48</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">132.83</td>
    <td align="right">134.06</td>
    <td align="right">49.84</td>
    <td align="right">105.66</td>
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
    <td align="right">21.09</td>
    <td align="right">23.39</td>
    <td align="right">23.39</td>
    <td align="right">23.39</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">49.47</td>
    <td align="right">38.98</td>
    <td align="right">39.22</td>
    <td align="right">39.31</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">31.57</td>
    <td align="right">31.45</td>
    <td align="right">31.42</td>
    <td align="right">31.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.44</td>
    <td align="right">38.69</td>
    <td align="right">38.72</td>
    <td align="right">38.53</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">62.48</td>
    <td align="right">57.80</td>
    <td align="right">56.04</td>
    <td align="right">55.92</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">56.97</td>
    <td align="right">56.83</td>
    <td align="right">56.90</td>
    <td align="right">57.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.25</td>
    <td align="right">61.48</td>
    <td align="right">61.42</td>
    <td align="right">61.54</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">89.13</td>
    <td align="right">81.30</td>
    <td align="right">80.32</td>
    <td align="right">80.14</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">85.98</td>
    <td align="right">79.67</td>
    <td align="right">79.68</td>
    <td align="right">79.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.72</td>
    <td align="right">79.73</td>
    <td align="right">79.88</td>
    <td align="right">79.72</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">111.96</td>
    <td align="right">100.59</td>
    <td align="right">98.33</td>
    <td align="right">98.15</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">132.26</td>
    <td align="right">118.09</td>
    <td align="right">118.26</td>
    <td align="right">118.12</td>
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
    <td align="right">20.92</td>
    <td align="right">24.38</td>
    <td align="right">26.76</td>
    <td align="right">29.82</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">49.64</td>
    <td align="right">43.16</td>
    <td align="right">42.71</td>
    <td align="right">42.75</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">31.25</td>
    <td align="right">34.98</td>
    <td align="right">31.64</td>
    <td align="right">35.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.26</td>
    <td align="right">43.13</td>
    <td align="right">31.89</td>
    <td align="right">43.74</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">63.52</td>
    <td align="right">60.30</td>
    <td align="right">51.11</td>
    <td align="right">58.15</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">57.19</td>
    <td align="right">60.07</td>
    <td align="right">38.32</td>
    <td align="right">52.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.61</td>
    <td align="right">63.40</td>
    <td align="right">42.64</td>
    <td align="right">63.43</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">88.88</td>
    <td align="right">88.36</td>
    <td align="right">63.06</td>
    <td align="right">78.94</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">85.62</td>
    <td align="right">90.36</td>
    <td align="right">43.33</td>
    <td align="right">76.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">80.50</td>
    <td align="right">89.00</td>
    <td align="right">56.93</td>
    <td align="right">83.75</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.88</td>
    <td align="right">106.18</td>
    <td align="right">77.79</td>
    <td align="right">96.08</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">132.05</td>
    <td align="right">133.16</td>
    <td align="right">49.78</td>
    <td align="right">104.72</td>
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
    <td align="right">21.77</td>
    <td align="right">23.95</td>
    <td align="right">24.02</td>
    <td align="right">23.98</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">50.92</td>
    <td align="right">39.66</td>
    <td align="right">39.26</td>
    <td align="right">39.73</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">35.48</td>
    <td align="right">35.38</td>
    <td align="right">35.30</td>
    <td align="right">34.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.08</td>
    <td align="right">41.93</td>
    <td align="right">41.93</td>
    <td align="right">41.94</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">66.00</td>
    <td align="right">57.44</td>
    <td align="right">57.14</td>
    <td align="right">58.29</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">59.03</td>
    <td align="right">57.84</td>
    <td align="right">57.88</td>
    <td align="right">58.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.65</td>
    <td align="right">63.11</td>
    <td align="right">63.12</td>
    <td align="right">63.00</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">92.41</td>
    <td align="right">81.37</td>
    <td align="right">86.76</td>
    <td align="right">86.00</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.35</td>
    <td align="right">82.37</td>
    <td align="right">82.04</td>
    <td align="right">82.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.34</td>
    <td align="right">81.00</td>
    <td align="right">80.99</td>
    <td align="right">81.02</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.32</td>
    <td align="right">97.38</td>
    <td align="right">97.65</td>
    <td align="right">97.36</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.81</td>
    <td align="right">118.81</td>
    <td align="right">118.58</td>
    <td align="right">118.58</td>
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
    <td align="right">33.54</td>
    <td align="right">6.64</td>
    <td align="right">5.60</td>
    <td align="right">12.04</td>
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
    <td align="right">66.33</td>
    <td align="right">60.92</td>
    <td align="right">41.73</td>
    <td align="right">50.43</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.95</td>
    <td align="right">20.62</td>
    <td align="right">23.20</td>
    <td align="right">25.78</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.95</td>
    <td align="right">24.79</td>
    <td align="right">26.47</td>
    <td align="right">27.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">104.05</td>
    <td align="right">87.17</td>
    <td align="right">41.35</td>
    <td align="right">64.49</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.58</td>
    <td align="right">22.39</td>
    <td align="right">24.56</td>
    <td align="right">27.18</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.50</td>
    <td align="right">27.83</td>
    <td align="right">28.57</td>
    <td align="right">31.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">122.73</td>
    <td align="right">105.30</td>
    <td align="right">41.41</td>
    <td align="right">72.55</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.17</td>
    <td align="right">25.94</td>
    <td align="right">25.96</td>
    <td align="right">28.89</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">28.98</td>
    <td align="right">30.30</td>
    <td align="right">30.17</td>
    <td align="right">33.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">158.60</td>
    <td align="right">135.50</td>
    <td align="right">41.55</td>
    <td align="right">88.76</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.63</td>
    <td align="right">26.82</td>
    <td align="right">27.24</td>
    <td align="right">30.58</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">30.97</td>
    <td align="right">31.97</td>
    <td align="right">32.28</td>
    <td align="right">35.52</td>
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
    <td align="right">66.55</td>
    <td align="right">62.48</td>
    <td align="right">61.43</td>
    <td align="right">61.62</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.85</td>
    <td align="right">20.52</td>
    <td align="right">23.00</td>
    <td align="right">24.66</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.86</td>
    <td align="right">25.04</td>
    <td align="right">26.73</td>
    <td align="right">28.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">101.57</td>
    <td align="right">91.82</td>
    <td align="right">89.99</td>
    <td align="right">89.93</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.58</td>
    <td align="right">22.52</td>
    <td align="right">24.39</td>
    <td align="right">26.77</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.52</td>
    <td align="right">27.89</td>
    <td align="right">28.38</td>
    <td align="right">30.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">126.91</td>
    <td align="right">109.46</td>
    <td align="right">109.39</td>
    <td align="right">108.74</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.25</td>
    <td align="right">25.99</td>
    <td align="right">26.01</td>
    <td align="right">28.80</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.03</td>
    <td align="right">30.16</td>
    <td align="right">30.18</td>
    <td align="right">33.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">166.55</td>
    <td align="right">139.91</td>
    <td align="right">139.92</td>
    <td align="right">140.21</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.59</td>
    <td align="right">26.62</td>
    <td align="right">27.23</td>
    <td align="right">31.85</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">30.95</td>
    <td align="right">33.85</td>
    <td align="right">33.78</td>
    <td align="right">37.45</td>
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
    <td align="right">65.63</td>
    <td align="right">61.73</td>
    <td align="right">43.68</td>
    <td align="right">52.11</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.98</td>
    <td align="right">20.93</td>
    <td align="right">23.73</td>
    <td align="right">26.81</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.90</td>
    <td align="right">25.31</td>
    <td align="right">26.45</td>
    <td align="right">28.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">103.74</td>
    <td align="right">94.07</td>
    <td align="right">46.39</td>
    <td align="right">68.04</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.82</td>
    <td align="right">23.09</td>
    <td align="right">25.05</td>
    <td align="right">28.68</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.70</td>
    <td align="right">27.71</td>
    <td align="right">28.79</td>
    <td align="right">31.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">126.51</td>
    <td align="right">114.87</td>
    <td align="right">45.82</td>
    <td align="right">78.59</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.43</td>
    <td align="right">25.70</td>
    <td align="right">26.34</td>
    <td align="right">30.56</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.35</td>
    <td align="right">30.48</td>
    <td align="right">30.02</td>
    <td align="right">32.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">158.31</td>
    <td align="right">150.78</td>
    <td align="right">46.02</td>
    <td align="right">97.22</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.93</td>
    <td align="right">26.57</td>
    <td align="right">27.30</td>
    <td align="right">33.49</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.66</td>
    <td align="right">32.38</td>
    <td align="right">31.79</td>
    <td align="right">35.61</td>
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
    <td align="right">65.56</td>
    <td align="right">65.21</td>
    <td align="right">64.31</td>
    <td align="right">64.09</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">21.00</td>
    <td align="right">20.92</td>
    <td align="right">23.72</td>
    <td align="right">26.77</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.98</td>
    <td align="right">25.32</td>
    <td align="right">26.13</td>
    <td align="right">28.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">99.39</td>
    <td align="right">98.08</td>
    <td align="right">98.12</td>
    <td align="right">97.93</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.81</td>
    <td align="right">23.05</td>
    <td align="right">25.13</td>
    <td align="right">29.19</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.70</td>
    <td align="right">28.06</td>
    <td align="right">28.88</td>
    <td align="right">31.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">125.82</td>
    <td align="right">122.53</td>
    <td align="right">121.70</td>
    <td align="right">120.77</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.45</td>
    <td align="right">25.82</td>
    <td align="right">26.21</td>
    <td align="right">31.80</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.22</td>
    <td align="right">30.38</td>
    <td align="right">30.24</td>
    <td align="right">33.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">165.32</td>
    <td align="right">160.77</td>
    <td align="right">160.59</td>
    <td align="right">160.35</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.85</td>
    <td align="right">26.60</td>
    <td align="right">27.30</td>
    <td align="right">33.48</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.48</td>
    <td align="right">31.91</td>
    <td align="right">32.48</td>
    <td align="right">35.71</td>
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
    <td align="right">24.31</td>
    <td align="right">43.13</td>
    <td align="right">33.35</td>
    <td align="right">38.92</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.48</td>
    <td align="right">44.04</td>
    <td align="right">34.31</td>
    <td align="right">40.38</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.61</td>
    <td align="right">28.48</td>
    <td align="right">28.26</td>
    <td align="right">27.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.46</td>
    <td align="right">58.10</td>
    <td align="right">33.98</td>
    <td align="right">46.71</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.10</td>
    <td align="right">58.92</td>
    <td align="right">36.87</td>
    <td align="right">47.88</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.81</td>
    <td align="right">37.42</td>
    <td align="right">27.51</td>
    <td align="right">37.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">37.78</td>
    <td align="right">77.95</td>
    <td align="right">34.84</td>
    <td align="right">56.30</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">41.79</td>
    <td align="right">78.96</td>
    <td align="right">36.91</td>
    <td align="right">57.61</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.08</td>
    <td align="right">54.01</td>
    <td align="right">36.89</td>
    <td align="right">49.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.09</td>
    <td align="right">89.31</td>
    <td align="right">35.37</td>
    <td align="right">63.05</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">46.96</td>
    <td align="right">97.23</td>
    <td align="right">38.56</td>
    <td align="right">68.01</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.07</td>
    <td align="right">54.35</td>
    <td align="right">37.35</td>
    <td align="right">50.56</td>
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
    <td align="right">24.39</td>
    <td align="right">41.41</td>
    <td align="right">40.60</td>
    <td align="right">41.46</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.48</td>
    <td align="right">41.11</td>
    <td align="right">41.25</td>
    <td align="right">40.78</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.60</td>
    <td align="right">28.44</td>
    <td align="right">28.11</td>
    <td align="right">27.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.49</td>
    <td align="right">55.58</td>
    <td align="right">55.14</td>
    <td align="right">55.06</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.12</td>
    <td align="right">55.72</td>
    <td align="right">56.44</td>
    <td align="right">55.81</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.78</td>
    <td align="right">37.54</td>
    <td align="right">37.48</td>
    <td align="right">37.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">37.68</td>
    <td align="right">76.11</td>
    <td align="right">76.57</td>
    <td align="right">76.08</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">41.77</td>
    <td align="right">75.31</td>
    <td align="right">76.33</td>
    <td align="right">75.25</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.09</td>
    <td align="right">47.55</td>
    <td align="right">47.25</td>
    <td align="right">47.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.02</td>
    <td align="right">84.25</td>
    <td align="right">84.47</td>
    <td align="right">84.50</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">46.77</td>
    <td align="right">89.91</td>
    <td align="right">89.30</td>
    <td align="right">91.08</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.13</td>
    <td align="right">49.26</td>
    <td align="right">49.14</td>
    <td align="right">48.92</td>
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
    <td align="right">43.21</td>
    <td align="right">34.13</td>
    <td align="right">38.48</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.25</td>
    <td align="right">43.36</td>
    <td align="right">35.07</td>
    <td align="right">40.29</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.39</td>
    <td align="right">28.23</td>
    <td align="right">28.16</td>
    <td align="right">28.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.63</td>
    <td align="right">58.29</td>
    <td align="right">34.47</td>
    <td align="right">46.58</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.19</td>
    <td align="right">59.18</td>
    <td align="right">36.36</td>
    <td align="right">48.24</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.83</td>
    <td align="right">37.27</td>
    <td align="right">27.72</td>
    <td align="right">37.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">39.41</td>
    <td align="right">78.64</td>
    <td align="right">36.39</td>
    <td align="right">57.32</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">41.91</td>
    <td align="right">78.64</td>
    <td align="right">37.71</td>
    <td align="right">58.40</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.17</td>
    <td align="right">47.74</td>
    <td align="right">30.66</td>
    <td align="right">43.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.54</td>
    <td align="right">89.68</td>
    <td align="right">35.36</td>
    <td align="right">63.29</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.08</td>
    <td align="right">96.96</td>
    <td align="right">38.34</td>
    <td align="right">66.66</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.22</td>
    <td align="right">48.19</td>
    <td align="right">31.36</td>
    <td align="right">45.35</td>
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
    <td align="right">40.15</td>
    <td align="right">40.62</td>
    <td align="right">41.18</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.25</td>
    <td align="right">41.41</td>
    <td align="right">41.27</td>
    <td align="right">40.60</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.39</td>
    <td align="right">28.23</td>
    <td align="right">28.17</td>
    <td align="right">28.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.61</td>
    <td align="right">55.59</td>
    <td align="right">55.05</td>
    <td align="right">55.81</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.26</td>
    <td align="right">55.92</td>
    <td align="right">55.63</td>
    <td align="right">56.12</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.84</td>
    <td align="right">37.35</td>
    <td align="right">37.28</td>
    <td align="right">37.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">38.72</td>
    <td align="right">76.20</td>
    <td align="right">75.11</td>
    <td align="right">75.12</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">41.87</td>
    <td align="right">76.56</td>
    <td align="right">76.27</td>
    <td align="right">76.25</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.05</td>
    <td align="right">47.17</td>
    <td align="right">47.10</td>
    <td align="right">47.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.48</td>
    <td align="right">84.15</td>
    <td align="right">83.60</td>
    <td align="right">83.29</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.01</td>
    <td align="right">88.42</td>
    <td align="right">88.54</td>
    <td align="right">89.00</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.14</td>
    <td align="right">47.72</td>
    <td align="right">47.56</td>
    <td align="right">47.37</td>
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
    <td align="right">17.86</td>
    <td align="right">28.24</td>
    <td align="right">27.70</td>
    <td align="right">27.70</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.70</td>
    <td align="right">30.62</td>
    <td align="right">30.60</td>
    <td align="right">30.56</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.30</td>
    <td align="right">30.70</td>
    <td align="right">30.65</td>
    <td align="right">30.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.94</td>
    <td align="right">44.32</td>
    <td align="right">34.77</td>
    <td align="right">44.27</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.81</td>
    <td align="right">38.67</td>
    <td align="right">28.96</td>
    <td align="right">38.50</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.65</td>
    <td align="right">46.75</td>
    <td align="right">37.42</td>
    <td align="right">46.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.14</td>
    <td align="right">53.57</td>
    <td align="right">36.75</td>
    <td align="right">49.74</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.86</td>
    <td align="right">57.76</td>
    <td align="right">40.16</td>
    <td align="right">53.78</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.72</td>
    <td align="right">56.94</td>
    <td align="right">39.43</td>
    <td align="right">53.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.15</td>
    <td align="right">55.38</td>
    <td align="right">38.53</td>
    <td align="right">51.74</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.65</td>
    <td align="right">59.53</td>
    <td align="right">40.31</td>
    <td align="right">54.35</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.99</td>
    <td align="right">60.92</td>
    <td align="right">41.90</td>
    <td align="right">56.51</td>
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
    <td align="right">17.87</td>
    <td align="right">28.23</td>
    <td align="right">28.19</td>
    <td align="right">28.10</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.71</td>
    <td align="right">30.65</td>
    <td align="right">30.62</td>
    <td align="right">30.15</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.30</td>
    <td align="right">30.72</td>
    <td align="right">30.69</td>
    <td align="right">30.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.93</td>
    <td align="right">39.06</td>
    <td align="right">39.36</td>
    <td align="right">38.22</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.81</td>
    <td align="right">37.99</td>
    <td align="right">37.91</td>
    <td align="right">37.85</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.65</td>
    <td align="right">38.84</td>
    <td align="right">38.74</td>
    <td align="right">38.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.15</td>
    <td align="right">47.27</td>
    <td align="right">47.08</td>
    <td align="right">47.09</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.87</td>
    <td align="right">50.22</td>
    <td align="right">50.17</td>
    <td align="right">49.88</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.70</td>
    <td align="right">49.74</td>
    <td align="right">49.54</td>
    <td align="right">49.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.14</td>
    <td align="right">47.70</td>
    <td align="right">47.62</td>
    <td align="right">47.58</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.68</td>
    <td align="right">52.42</td>
    <td align="right">52.38</td>
    <td align="right">52.25</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.98</td>
    <td align="right">52.15</td>
    <td align="right">52.12</td>
    <td align="right">52.09</td>
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
    <td align="right">27.91</td>
    <td align="right">27.84</td>
    <td align="right">27.75</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.72</td>
    <td align="right">30.60</td>
    <td align="right">30.57</td>
    <td align="right">30.45</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.34</td>
    <td align="right">30.69</td>
    <td align="right">30.65</td>
    <td align="right">30.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.80</td>
    <td align="right">39.48</td>
    <td align="right">29.39</td>
    <td align="right">39.22</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.71</td>
    <td align="right">38.53</td>
    <td align="right">29.01</td>
    <td align="right">38.39</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.78</td>
    <td align="right">41.10</td>
    <td align="right">31.25</td>
    <td align="right">41.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.06</td>
    <td align="right">46.86</td>
    <td align="right">30.06</td>
    <td align="right">43.32</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.29</td>
    <td align="right">50.12</td>
    <td align="right">32.51</td>
    <td align="right">45.93</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.28</td>
    <td align="right">49.38</td>
    <td align="right">31.88</td>
    <td align="right">45.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.12</td>
    <td align="right">47.11</td>
    <td align="right">29.99</td>
    <td align="right">43.36</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.76</td>
    <td align="right">51.89</td>
    <td align="right">32.69</td>
    <td align="right">46.92</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.07</td>
    <td align="right">51.18</td>
    <td align="right">31.89</td>
    <td align="right">46.19</td>
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
    <td align="right">27.92</td>
    <td align="right">27.89</td>
    <td align="right">27.78</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.73</td>
    <td align="right">30.61</td>
    <td align="right">30.21</td>
    <td align="right">30.19</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.35</td>
    <td align="right">30.68</td>
    <td align="right">30.65</td>
    <td align="right">30.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.83</td>
    <td align="right">37.78</td>
    <td align="right">37.68</td>
    <td align="right">37.55</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.69</td>
    <td align="right">37.98</td>
    <td align="right">37.93</td>
    <td align="right">37.69</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.81</td>
    <td align="right">38.92</td>
    <td align="right">38.87</td>
    <td align="right">38.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.04</td>
    <td align="right">47.03</td>
    <td align="right">47.01</td>
    <td align="right">46.89</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.26</td>
    <td align="right">49.87</td>
    <td align="right">49.74</td>
    <td align="right">49.74</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.30</td>
    <td align="right">49.63</td>
    <td align="right">49.59</td>
    <td align="right">49.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.02</td>
    <td align="right">47.24</td>
    <td align="right">47.21</td>
    <td align="right">47.14</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.74</td>
    <td align="right">51.85</td>
    <td align="right">51.80</td>
    <td align="right">51.83</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.05</td>
    <td align="right">51.60</td>
    <td align="right">51.48</td>
    <td align="right">51.48</td>
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
    <td align="right">26.93</td>
    <td align="right">43.93</td>
    <td align="right">33.01</td>
    <td align="right">39.07</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.56</td>
    <td align="right">55.09</td>
    <td align="right">37.42</td>
    <td align="right">45.96</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.35</td>
    <td align="right">62.87</td>
    <td align="right">37.81</td>
    <td align="right">49.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.59</td>
    <td align="right">61.79</td>
    <td align="right">33.14</td>
    <td align="right">49.13</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">39.61</td>
    <td align="right">62.16</td>
    <td align="right">35.08</td>
    <td align="right">49.08</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.53</td>
    <td align="right">81.75</td>
    <td align="right">40.26</td>
    <td align="right">61.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.64</td>
    <td align="right">73.31</td>
    <td align="right">32.90</td>
    <td align="right">55.33</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.92</td>
    <td align="right">81.05</td>
    <td align="right">37.97</td>
    <td align="right">60.02</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">48.29</td>
    <td align="right">89.69</td>
    <td align="right">37.56</td>
    <td align="right">66.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.31</td>
    <td align="right">98.65</td>
    <td align="right">33.80</td>
    <td align="right">68.65</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">56.02</td>
    <td align="right">100.75</td>
    <td align="right">39.44</td>
    <td align="right">71.31</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">64.43</td>
    <td align="right">120.64</td>
    <td align="right">39.69</td>
    <td align="right">81.20</td>
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
    <td align="right">26.94</td>
    <td align="right">42.34</td>
    <td align="right">43.19</td>
    <td align="right">41.74</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.63</td>
    <td align="right">48.03</td>
    <td align="right">48.34</td>
    <td align="right">49.06</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.33</td>
    <td align="right">60.50</td>
    <td align="right">60.74</td>
    <td align="right">61.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.65</td>
    <td align="right">56.16</td>
    <td align="right">56.31</td>
    <td align="right">56.21</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">39.71</td>
    <td align="right">60.01</td>
    <td align="right">59.95</td>
    <td align="right">59.96</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.63</td>
    <td align="right">78.40</td>
    <td align="right">78.41</td>
    <td align="right">78.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.75</td>
    <td align="right">67.03</td>
    <td align="right">66.96</td>
    <td align="right">67.06</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.96</td>
    <td align="right">77.51</td>
    <td align="right">77.69</td>
    <td align="right">77.37</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">47.66</td>
    <td align="right">83.66</td>
    <td align="right">83.53</td>
    <td align="right">83.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.22</td>
    <td align="right">90.65</td>
    <td align="right">92.60</td>
    <td align="right">91.43</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.55</td>
    <td align="right">91.81</td>
    <td align="right">92.18</td>
    <td align="right">91.33</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">62.91</td>
    <td align="right">120.85</td>
    <td align="right">119.95</td>
    <td align="right">119.84</td>
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
    <td align="right">28.11</td>
    <td align="right">43.51</td>
    <td align="right">33.63</td>
    <td align="right">39.36</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.67</td>
    <td align="right">54.82</td>
    <td align="right">36.82</td>
    <td align="right">45.70</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">38.50</td>
    <td align="right">63.02</td>
    <td align="right">40.26</td>
    <td align="right">50.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">37.83</td>
    <td align="right">62.09</td>
    <td align="right">34.82</td>
    <td align="right">49.27</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">39.70</td>
    <td align="right">61.81</td>
    <td align="right">35.88</td>
    <td align="right">50.12</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">46.26</td>
    <td align="right">83.89</td>
    <td align="right">40.92</td>
    <td align="right">63.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">43.18</td>
    <td align="right">74.11</td>
    <td align="right">35.55</td>
    <td align="right">55.66</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.82</td>
    <td align="right">80.38</td>
    <td align="right">37.14</td>
    <td align="right">59.30</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">49.18</td>
    <td align="right">91.38</td>
    <td align="right">39.23</td>
    <td align="right">67.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">54.30</td>
    <td align="right">98.71</td>
    <td align="right">35.96</td>
    <td align="right">68.70</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.59</td>
    <td align="right">98.59</td>
    <td align="right">36.21</td>
    <td align="right">68.47</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">65.36</td>
    <td align="right">124.05</td>
    <td align="right">38.50</td>
    <td align="right">81.83</td>
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
    <td align="right">28.10</td>
    <td align="right">42.04</td>
    <td align="right">42.03</td>
    <td align="right">42.16</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.67</td>
    <td align="right">47.90</td>
    <td align="right">48.14</td>
    <td align="right">48.47</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">38.42</td>
    <td align="right">60.68</td>
    <td align="right">60.38</td>
    <td align="right">60.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">37.52</td>
    <td align="right">55.82</td>
    <td align="right">56.20</td>
    <td align="right">56.17</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">39.62</td>
    <td align="right">59.48</td>
    <td align="right">59.07</td>
    <td align="right">58.85</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">46.04</td>
    <td align="right">77.74</td>
    <td align="right">77.44</td>
    <td align="right">77.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">43.16</td>
    <td align="right">67.08</td>
    <td align="right">66.72</td>
    <td align="right">66.89</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.76</td>
    <td align="right">77.29</td>
    <td align="right">77.01</td>
    <td align="right">77.03</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">49.03</td>
    <td align="right">83.71</td>
    <td align="right">83.72</td>
    <td align="right">83.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">54.23</td>
    <td align="right">91.17</td>
    <td align="right">93.47</td>
    <td align="right">90.88</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.36</td>
    <td align="right">91.65</td>
    <td align="right">91.25</td>
    <td align="right">91.94</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">64.58</td>
    <td align="right">118.25</td>
    <td align="right">118.77</td>
    <td align="right">118.79</td>
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
    <td align="right">62.69</td>
    <td align="right">33.23</td>
    <td align="right">16.16</td>
    <td align="right">36.69</td>
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
    <td align="right">71.61</td>
    <td align="right">62.60</td>
    <td align="right">42.21</td>
    <td align="right">51.11</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.50</td>
    <td align="right">20.65</td>
    <td align="right">23.82</td>
    <td align="right">26.60</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">31.17</td>
    <td align="right">26.67</td>
    <td align="right">28.09</td>
    <td align="right">29.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">107.07</td>
    <td align="right">90.26</td>
    <td align="right">44.13</td>
    <td align="right">67.00</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">36.13</td>
    <td align="right">33.38</td>
    <td align="right">35.60</td>
    <td align="right">39.09</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">40.25</td>
    <td align="right">31.38</td>
    <td align="right">32.22</td>
    <td align="right">34.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">368.10</td>
    <td align="right">327.40</td>
    <td align="right">90.66</td>
    <td align="right">210.63</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">42.13</td>
    <td align="right">43.61</td>
    <td align="right">44.17</td>
    <td align="right">48.19</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">66.59</td>
    <td align="right">78.25</td>
    <td align="right">78.00</td>
    <td align="right">82.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">533.32</td>
    <td align="right">442.19</td>
    <td align="right">98.08</td>
    <td align="right">273.27</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">50.05</td>
    <td align="right">56.18</td>
    <td align="right">56.92</td>
    <td align="right">62.20</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">68.03</td>
    <td align="right">62.28</td>
    <td align="right">62.30</td>
    <td align="right">65.47</td>
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
    <td align="right">82.50</td>
    <td align="right">137.51</td>
    <td align="right">137.50</td>
    <td align="right">136.70</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">23.83</td>
    <td align="right">20.59</td>
    <td align="right">23.79</td>
    <td align="right">26.19</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">31.05</td>
    <td align="right">26.69</td>
    <td align="right">28.13</td>
    <td align="right">29.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">180.56</td>
    <td align="right">182.08</td>
    <td align="right">180.07</td>
    <td align="right">179.86</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">36.57</td>
    <td align="right">45.23</td>
    <td align="right">46.66</td>
    <td align="right">49.91</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">31.37</td>
    <td align="right">30.02</td>
    <td align="right">30.68</td>
    <td align="right">32.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">343.12</td>
    <td align="right">306.86</td>
    <td align="right">305.72</td>
    <td align="right">305.03</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">47.11</td>
    <td align="right">41.01</td>
    <td align="right">41.53</td>
    <td align="right">45.33</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">63.36</td>
    <td align="right">50.32</td>
    <td align="right">49.76</td>
    <td align="right">53.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">519.99</td>
    <td align="right">446.96</td>
    <td align="right">444.96</td>
    <td align="right">444.17</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">48.95</td>
    <td align="right">44.60</td>
    <td align="right">45.18</td>
    <td align="right">51.03</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">69.51</td>
    <td align="right">62.14</td>
    <td align="right">62.23</td>
    <td align="right">65.31</td>
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
    <td align="right">89.34</td>
    <td align="right">154.19</td>
    <td align="right">83.13</td>
    <td align="right">116.29</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">22.22</td>
    <td align="right">21.34</td>
    <td align="right">24.98</td>
    <td align="right">27.97</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">36.38</td>
    <td align="right">43.35</td>
    <td align="right">44.18</td>
    <td align="right">46.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">153.87</td>
    <td align="right">193.67</td>
    <td align="right">74.67</td>
    <td align="right">133.20</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">33.77</td>
    <td align="right">35.35</td>
    <td align="right">37.64</td>
    <td align="right">42.03</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">46.53</td>
    <td align="right">75.09</td>
    <td align="right">75.83</td>
    <td align="right">77.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">368.46</td>
    <td align="right">390.31</td>
    <td align="right">113.13</td>
    <td align="right">247.86</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">57.89</td>
    <td align="right">48.65</td>
    <td align="right">49.91</td>
    <td align="right">55.09</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">64.04</td>
    <td align="right">53.37</td>
    <td align="right">53.64</td>
    <td align="right">56.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">512.96</td>
    <td align="right">550.43</td>
    <td align="right">126.50</td>
    <td align="right">334.03</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">66.92</td>
    <td align="right">72.18</td>
    <td align="right">73.01</td>
    <td align="right">80.44</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">74.71</td>
    <td align="right">63.24</td>
    <td align="right">62.21</td>
    <td align="right">65.69</td>
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
    <td align="right">95.30</td>
    <td align="right">121.34</td>
    <td align="right">121.30</td>
    <td align="right">120.95</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">24.60</td>
    <td align="right">27.21</td>
    <td align="right">30.80</td>
    <td align="right">34.72</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">38.17</td>
    <td align="right">26.88</td>
    <td align="right">27.72</td>
    <td align="right">29.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">211.60</td>
    <td align="right">235.76</td>
    <td align="right">236.08</td>
    <td align="right">236.59</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">40.12</td>
    <td align="right">42.38</td>
    <td align="right">44.87</td>
    <td align="right">49.69</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">50.31</td>
    <td align="right">52.54</td>
    <td align="right">53.49</td>
    <td align="right">55.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">365.25</td>
    <td align="right">397.07</td>
    <td align="right">396.76</td>
    <td align="right">396.76</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">45.97</td>
    <td align="right">41.51</td>
    <td align="right">42.26</td>
    <td align="right">48.96</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">57.24</td>
    <td align="right">48.95</td>
    <td align="right">48.70</td>
    <td align="right">51.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">483.38</td>
    <td align="right">514.87</td>
    <td align="right">514.96</td>
    <td align="right">515.54</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">66.49</td>
    <td align="right">81.00</td>
    <td align="right">81.47</td>
    <td align="right">89.40</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">69.77</td>
    <td align="right">86.89</td>
    <td align="right">86.58</td>
    <td align="right">90.08</td>
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
    <td align="right">26.23</td>
    <td align="right">43.29</td>
    <td align="right">35.04</td>
    <td align="right">40.01</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">31.25</td>
    <td align="right">42.97</td>
    <td align="right">36.41</td>
    <td align="right">40.93</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">23.33</td>
    <td align="right">30.29</td>
    <td align="right">30.32</td>
    <td align="right">30.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.02</td>
    <td align="right">84.08</td>
    <td align="right">67.86</td>
    <td align="right">76.97</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">37.78</td>
    <td align="right">62.50</td>
    <td align="right">43.47</td>
    <td align="right">53.13</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">26.63</td>
    <td align="right">55.55</td>
    <td align="right">45.97</td>
    <td align="right">55.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">64.08</td>
    <td align="right">97.00</td>
    <td align="right">56.89</td>
    <td align="right">77.14</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">72.91</td>
    <td align="right">96.22</td>
    <td align="right">58.09</td>
    <td align="right">77.11</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">50.28</td>
    <td align="right">80.73</td>
    <td align="right">63.64</td>
    <td align="right">77.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">86.78</td>
    <td align="right">125.92</td>
    <td align="right">79.73</td>
    <td align="right">104.15</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">95.79</td>
    <td align="right">143.14</td>
    <td align="right">92.16</td>
    <td align="right">118.50</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">70.89</td>
    <td align="right">108.09</td>
    <td align="right">91.63</td>
    <td align="right">105.06</td>
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
    <td align="right">37.28</td>
    <td align="right">41.55</td>
    <td align="right">40.78</td>
    <td align="right">41.60</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">37.96</td>
    <td align="right">56.87</td>
    <td align="right">57.12</td>
    <td align="right">56.69</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">31.53</td>
    <td align="right">33.90</td>
    <td align="right">33.88</td>
    <td align="right">33.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">48.03</td>
    <td align="right">58.68</td>
    <td align="right">58.54</td>
    <td align="right">58.56</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">55.61</td>
    <td align="right">87.58</td>
    <td align="right">87.75</td>
    <td align="right">87.65</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">28.71</td>
    <td align="right">61.17</td>
    <td align="right">61.30</td>
    <td align="right">60.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.11</td>
    <td align="right">114.05</td>
    <td align="right">113.79</td>
    <td align="right">113.96</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.20</td>
    <td align="right">92.39</td>
    <td align="right">93.47</td>
    <td align="right">92.41</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">60.36</td>
    <td align="right">74.40</td>
    <td align="right">74.37</td>
    <td align="right">74.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.61</td>
    <td align="right">123.18</td>
    <td align="right">123.24</td>
    <td align="right">123.11</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">92.49</td>
    <td align="right">132.69</td>
    <td align="right">131.80</td>
    <td align="right">133.10</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">71.45</td>
    <td align="right">86.75</td>
    <td align="right">86.91</td>
    <td align="right">86.70</td>
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
    <td align="right">31.79</td>
    <td align="right">65.44</td>
    <td align="right">60.67</td>
    <td align="right">63.58</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">38.74</td>
    <td align="right">61.34</td>
    <td align="right">58.15</td>
    <td align="right">60.65</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.31</td>
    <td align="right">58.55</td>
    <td align="right">58.63</td>
    <td align="right">58.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">42.42</td>
    <td align="right">68.70</td>
    <td align="right">48.78</td>
    <td align="right">59.50</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">45.28</td>
    <td align="right">99.16</td>
    <td align="right">84.21</td>
    <td align="right">92.47</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">31.44</td>
    <td align="right">78.42</td>
    <td align="right">68.93</td>
    <td align="right">79.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.94</td>
    <td align="right">113.64</td>
    <td align="right">78.01</td>
    <td align="right">96.88</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">77.83</td>
    <td align="right">110.76</td>
    <td align="right">77.73</td>
    <td align="right">95.10</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">57.16</td>
    <td align="right">72.73</td>
    <td align="right">55.81</td>
    <td align="right">68.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.32</td>
    <td align="right">125.93</td>
    <td align="right">77.99</td>
    <td align="right">104.21</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">94.30</td>
    <td align="right">140.95</td>
    <td align="right">90.80</td>
    <td align="right">115.51</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">69.17</td>
    <td align="right">85.84</td>
    <td align="right">68.85</td>
    <td align="right">81.24</td>
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
    <td align="right">36.63</td>
    <td align="right">40.54</td>
    <td align="right">40.99</td>
    <td align="right">41.55</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">34.38</td>
    <td align="right">47.34</td>
    <td align="right">47.49</td>
    <td align="right">47.28</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">23.66</td>
    <td align="right">59.32</td>
    <td align="right">59.34</td>
    <td align="right">59.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">45.39</td>
    <td align="right">81.57</td>
    <td align="right">81.67</td>
    <td align="right">81.76</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.96</td>
    <td align="right">73.99</td>
    <td align="right">73.65</td>
    <td align="right">73.81</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">27.81</td>
    <td align="right">78.94</td>
    <td align="right">78.84</td>
    <td align="right">78.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">72.28</td>
    <td align="right">96.35</td>
    <td align="right">95.60</td>
    <td align="right">95.17</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">75.57</td>
    <td align="right">94.60</td>
    <td align="right">93.96</td>
    <td align="right">94.32</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">59.23</td>
    <td align="right">70.99</td>
    <td align="right">70.64</td>
    <td align="right">70.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">90.77</td>
    <td align="right">128.33</td>
    <td align="right">127.73</td>
    <td align="right">127.75</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">95.03</td>
    <td align="right">131.44</td>
    <td align="right">132.77</td>
    <td align="right">131.32</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">72.42</td>
    <td align="right">102.00</td>
    <td align="right">102.18</td>
    <td align="right">102.38</td>
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
    <td align="right">21.34</td>
    <td align="right">29.87</td>
    <td align="right">29.90</td>
    <td align="right">29.91</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">31.63</td>
    <td align="right">45.77</td>
    <td align="right">45.90</td>
    <td align="right">45.99</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">26.01</td>
    <td align="right">38.31</td>
    <td align="right">38.34</td>
    <td align="right">38.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">36.34</td>
    <td align="right">55.47</td>
    <td align="right">46.07</td>
    <td align="right">56.22</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">35.64</td>
    <td align="right">48.39</td>
    <td align="right">39.00</td>
    <td align="right">48.46</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">38.94</td>
    <td align="right">56.12</td>
    <td align="right">47.39</td>
    <td align="right">57.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">58.32</td>
    <td align="right">77.59</td>
    <td align="right">61.60</td>
    <td align="right">75.57</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">69.27</td>
    <td align="right">102.27</td>
    <td align="right">84.75</td>
    <td align="right">98.36</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">63.23</td>
    <td align="right">114.86</td>
    <td align="right">96.90</td>
    <td align="right">110.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">64.12</td>
    <td align="right">93.22</td>
    <td align="right">76.03</td>
    <td align="right">89.96</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">70.06</td>
    <td align="right">97.72</td>
    <td align="right">77.96</td>
    <td align="right">92.34</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">72.41</td>
    <td align="right">124.35</td>
    <td align="right">104.17</td>
    <td align="right">119.86</td>
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
    <td align="right">20.01</td>
    <td align="right">29.88</td>
    <td align="right">29.88</td>
    <td align="right">29.87</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">30.04</td>
    <td align="right">47.48</td>
    <td align="right">47.51</td>
    <td align="right">47.45</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">24.27</td>
    <td align="right">46.79</td>
    <td align="right">46.91</td>
    <td align="right">47.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">34.85</td>
    <td align="right">55.49</td>
    <td align="right">55.46</td>
    <td align="right">55.59</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">33.11</td>
    <td align="right">41.60</td>
    <td align="right">41.73</td>
    <td align="right">41.54</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">31.46</td>
    <td align="right">41.73</td>
    <td align="right">41.53</td>
    <td align="right">41.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">66.30</td>
    <td align="right">78.60</td>
    <td align="right">78.67</td>
    <td align="right">78.79</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">61.86</td>
    <td align="right">84.38</td>
    <td align="right">84.36</td>
    <td align="right">84.25</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">54.08</td>
    <td align="right">73.56</td>
    <td align="right">73.59</td>
    <td align="right">73.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">64.46</td>
    <td align="right">86.54</td>
    <td align="right">86.44</td>
    <td align="right">86.46</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">69.64</td>
    <td align="right">89.53</td>
    <td align="right">89.51</td>
    <td align="right">89.52</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">74.64</td>
    <td align="right">89.16</td>
    <td align="right">89.35</td>
    <td align="right">89.20</td>
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
    <td align="right">23.23</td>
    <td align="right">29.26</td>
    <td align="right">29.39</td>
    <td align="right">29.34</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">31.20</td>
    <td align="right">45.05</td>
    <td align="right">44.98</td>
    <td align="right">45.05</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">29.79</td>
    <td align="right">40.58</td>
    <td align="right">40.63</td>
    <td align="right">40.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">31.79</td>
    <td align="right">55.19</td>
    <td align="right">44.97</td>
    <td align="right">55.10</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">32.79</td>
    <td align="right">80.21</td>
    <td align="right">70.97</td>
    <td align="right">80.73</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">38.89</td>
    <td align="right">64.08</td>
    <td align="right">54.42</td>
    <td align="right">65.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">67.03</td>
    <td align="right">103.95</td>
    <td align="right">86.89</td>
    <td align="right">100.59</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">60.31</td>
    <td align="right">98.56</td>
    <td align="right">80.75</td>
    <td align="right">94.26</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">55.70</td>
    <td align="right">73.20</td>
    <td align="right">55.98</td>
    <td align="right">69.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">73.49</td>
    <td align="right">87.96</td>
    <td align="right">71.45</td>
    <td align="right">84.87</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">72.53</td>
    <td align="right">89.04</td>
    <td align="right">70.04</td>
    <td align="right">84.11</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">76.86</td>
    <td align="right">108.11</td>
    <td align="right">88.89</td>
    <td align="right">102.86</td>
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
    <td align="right">21.27</td>
    <td align="right">29.26</td>
    <td align="right">29.36</td>
    <td align="right">29.33</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">31.55</td>
    <td align="right">41.55</td>
    <td align="right">41.61</td>
    <td align="right">41.73</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">32.30</td>
    <td align="right">45.95</td>
    <td align="right">45.90</td>
    <td align="right">45.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">31.74</td>
    <td align="right">85.76</td>
    <td align="right">85.65</td>
    <td align="right">85.44</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">35.37</td>
    <td align="right">79.71</td>
    <td align="right">79.91</td>
    <td align="right">80.16</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">38.14</td>
    <td align="right">90.10</td>
    <td align="right">90.09</td>
    <td align="right">89.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">65.31</td>
    <td align="right">76.53</td>
    <td align="right">76.29</td>
    <td align="right">76.47</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">69.03</td>
    <td align="right">82.14</td>
    <td align="right">81.58</td>
    <td align="right">81.75</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">71.33</td>
    <td align="right">94.97</td>
    <td align="right">95.11</td>
    <td align="right">94.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">71.79</td>
    <td align="right">84.66</td>
    <td align="right">84.63</td>
    <td align="right">84.67</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">74.19</td>
    <td align="right">90.95</td>
    <td align="right">90.85</td>
    <td align="right">90.79</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">75.85</td>
    <td align="right">111.28</td>
    <td align="right">111.28</td>
    <td align="right">111.75</td>
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
    <td align="right">28.60</td>
    <td align="right">44.03</td>
    <td align="right">34.48</td>
    <td align="right">40.13</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">45.76</td>
    <td align="right">57.44</td>
    <td align="right">41.46</td>
    <td align="right">49.76</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">39.76</td>
    <td align="right">63.23</td>
    <td align="right">39.47</td>
    <td align="right">51.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">55.71</td>
    <td align="right">67.63</td>
    <td align="right">41.29</td>
    <td align="right">56.55</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">61.00</td>
    <td align="right">82.70</td>
    <td align="right">60.06</td>
    <td align="right">72.89</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">67.15</td>
    <td align="right">117.96</td>
    <td align="right">78.04</td>
    <td align="right">98.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">71.03</td>
    <td align="right">90.33</td>
    <td align="right">54.88</td>
    <td align="right">74.79</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">78.45</td>
    <td align="right">123.31</td>
    <td align="right">84.33</td>
    <td align="right">104.25</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">81.19</td>
    <td align="right">113.77</td>
    <td align="right">56.78</td>
    <td align="right">87.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">87.42</td>
    <td align="right">131.39</td>
    <td align="right">75.00</td>
    <td align="right">105.85</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">98.77</td>
    <td align="right">139.78</td>
    <td align="right">82.23</td>
    <td align="right">112.23</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">119.26</td>
    <td align="right">165.73</td>
    <td align="right">85.58</td>
    <td align="right">127.29</td>
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
    <td align="right">38.50</td>
    <td align="right">42.14</td>
    <td align="right">43.08</td>
    <td align="right">41.84</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">42.45</td>
    <td align="right">75.69</td>
    <td align="right">75.63</td>
    <td align="right">76.27</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">44.76</td>
    <td align="right">83.13</td>
    <td align="right">83.40</td>
    <td align="right">83.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">53.41</td>
    <td align="right">59.84</td>
    <td align="right">60.16</td>
    <td align="right">60.15</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">60.00</td>
    <td align="right">62.57</td>
    <td align="right">63.01</td>
    <td align="right">62.96</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">58.29</td>
    <td align="right">78.80</td>
    <td align="right">78.95</td>
    <td align="right">78.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">69.90</td>
    <td align="right">91.43</td>
    <td align="right">91.25</td>
    <td align="right">91.61</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">85.40</td>
    <td align="right">124.50</td>
    <td align="right">124.92</td>
    <td align="right">124.28</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">91.47</td>
    <td align="right">121.98</td>
    <td align="right">122.04</td>
    <td align="right">121.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">89.39</td>
    <td align="right">122.09</td>
    <td align="right">122.95</td>
    <td align="right">122.48</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">102.06</td>
    <td align="right">142.22</td>
    <td align="right">142.53</td>
    <td align="right">142.16</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">116.97</td>
    <td align="right">160.57</td>
    <td align="right">159.93</td>
    <td align="right">160.85</td>
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
    <td align="right">31.09</td>
    <td align="right">43.50</td>
    <td align="right">35.94</td>
    <td align="right">40.84</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">40.36</td>
    <td align="right">55.18</td>
    <td align="right">39.16</td>
    <td align="right">46.81</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">43.94</td>
    <td align="right">64.34</td>
    <td align="right">43.58</td>
    <td align="right">52.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">60.65</td>
    <td align="right">78.57</td>
    <td align="right">56.87</td>
    <td align="right">68.41</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">64.64</td>
    <td align="right">80.61</td>
    <td align="right">59.82</td>
    <td align="right">71.39</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">69.21</td>
    <td align="right">91.85</td>
    <td align="right">47.47</td>
    <td align="right">70.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.91</td>
    <td align="right">110.77</td>
    <td align="right">80.45</td>
    <td align="right">97.50</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">84.39</td>
    <td align="right">126.45</td>
    <td align="right">90.12</td>
    <td align="right">109.38</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">99.11</td>
    <td align="right">141.91</td>
    <td align="right">70.92</td>
    <td align="right">112.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">93.99</td>
    <td align="right">135.17</td>
    <td align="right">79.56</td>
    <td align="right">109.00</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">103.75</td>
    <td align="right">145.75</td>
    <td align="right">89.57</td>
    <td align="right">119.21</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">134.13</td>
    <td align="right">188.38</td>
    <td align="right">72.84</td>
    <td align="right">137.25</td>
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
    <td align="right">35.37</td>
    <td align="right">53.74</td>
    <td align="right">54.00</td>
    <td align="right">53.89</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.23</td>
    <td align="right">48.26</td>
    <td align="right">48.36</td>
    <td align="right">48.29</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">43.41</td>
    <td align="right">74.72</td>
    <td align="right">74.36</td>
    <td align="right">74.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">50.31</td>
    <td align="right">65.76</td>
    <td align="right">65.98</td>
    <td align="right">65.76</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">47.41</td>
    <td align="right">77.29</td>
    <td align="right">76.37</td>
    <td align="right">76.49</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">73.61</td>
    <td align="right">89.43</td>
    <td align="right">89.24</td>
    <td align="right">89.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">77.12</td>
    <td align="right">84.02</td>
    <td align="right">84.04</td>
    <td align="right">84.08</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.93</td>
    <td align="right">124.73</td>
    <td align="right">124.84</td>
    <td align="right">124.80</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">99.70</td>
    <td align="right">132.76</td>
    <td align="right">132.30</td>
    <td align="right">133.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">91.98</td>
    <td align="right">125.30</td>
    <td align="right">126.59</td>
    <td align="right">125.41</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">103.12</td>
    <td align="right">141.29</td>
    <td align="right">141.06</td>
    <td align="right">141.43</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">118.03</td>
    <td align="right">151.84</td>
    <td align="right">152.90</td>
    <td align="right">152.76</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
