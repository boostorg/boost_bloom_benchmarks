# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
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
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.21</td>
    <td align="right">5.96</td>
    <td align="right">4.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.56</td>
    <td align="right">11.64</td>
    <td align="right">17.98</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.85</td>
    <td align="right">4.58</td>
    <td align="right">4.59</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.67</td>
    <td align="right">4.95</td>
    <td align="right">4.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">19.07</td>
    <td align="right">17.49</td>
    <td align="right">18.82</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.41</td>
    <td align="right">5.05</td>
    <td align="right">5.06</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.21</td>
    <td align="right">5.47</td>
    <td align="right">5.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.18</td>
    <td align="right">20.02</td>
    <td align="right">17.70</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.99</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.85</td>
    <td align="right">5.94</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">29.50</td>
    <td align="right">25.23</td>
    <td align="right">18.16</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.60</td>
    <td align="right">5.77</td>
    <td align="right">5.77</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.27</td>
    <td align="right">6.27</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.14</td>
    <td align="right">12.28</td>
    <td align="right">18.37</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.80</td>
    <td align="right">4.62</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">5.02</td>
    <td align="right">5.14</td>
    <td align="right">5.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.82</td>
    <td align="right">18.01</td>
    <td align="right">19.34</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.28</td>
    <td align="right">5.15</td>
    <td align="right">5.15</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.09</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">19.71</td>
    <td align="right">21.73</td>
    <td align="right">18.53</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.81</td>
    <td align="right">5.71</td>
    <td align="right">5.72</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.38</td>
    <td align="right">6.13</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.69</td>
    <td align="right">27.82</td>
    <td align="right">18.60</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.13</td>
    <td align="right">6.07</td>
    <td align="right">6.07</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.89</td>
    <td align="right">6.45</td>
    <td align="right">6.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.19</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.87</td>
    <td align="right">7.05</td>
    <td align="right">7.04</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.24</td>
    <td align="right">3.40</td>
    <td align="right">3.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.08</td>
    <td align="right">7.75</td>
    <td align="right">7.74</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.21</td>
    <td align="right">9.50</td>
    <td align="right">9.50</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.57</td>
    <td align="right">3.09</td>
    <td align="right">3.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.17</td>
    <td align="right">11.32</td>
    <td align="right">11.28</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">22.38</td>
    <td align="right">13.48</td>
    <td align="right">13.48</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">6.15</td>
    <td align="right">5.84</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.31</td>
    <td align="right">13.06</td>
    <td align="right">13.08</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.09</td>
    <td align="right">15.98</td>
    <td align="right">15.94</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">6.45</td>
    <td align="right">5.90</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.04</td>
    <td align="right">5.68</td>
    <td align="right">5.69</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.91</td>
    <td align="right">6.94</td>
    <td align="right">6.93</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.25</td>
    <td align="right">2.96</td>
    <td align="right">2.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.34</td>
    <td align="right">7.91</td>
    <td align="right">7.91</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.80</td>
    <td align="right">9.35</td>
    <td align="right">9.34</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.69</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.81</td>
    <td align="right">11.33</td>
    <td align="right">11.33</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">21.56</td>
    <td align="right">13.66</td>
    <td align="right">13.66</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">6.10</td>
    <td align="right">6.07</td>
    <td align="right">4.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.58</td>
    <td align="right">13.00</td>
    <td align="right">12.98</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">12.40</td>
    <td align="right">15.89</td>
    <td align="right">15.87</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">6.15</td>
    <td align="right">6.10</td>
    <td align="right">4.32</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.24</td>
    <td align="right">3.21</td>
    <td align="right">3.21</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.62</td>
    <td align="right">5.22</td>
    <td align="right">5.21</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.70</td>
    <td align="right">5.03</td>
    <td align="right">5.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.34</td>
    <td align="right">3.32</td>
    <td align="right">3.28</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.42</td>
    <td align="right">4.47</td>
    <td align="right">4.46</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.75</td>
    <td align="right">5.17</td>
    <td align="right">5.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.59</td>
    <td align="right">5.51</td>
    <td align="right">3.94</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.57</td>
    <td align="right">8.14</td>
    <td align="right">6.26</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.86</td>
    <td align="right">7.91</td>
    <td align="right">6.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.65</td>
    <td align="right">5.56</td>
    <td align="right">3.96</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">9.10</td>
    <td align="right">9.43</td>
    <td align="right">6.32</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">9.01</td>
    <td align="right">9.11</td>
    <td align="right">6.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.23</td>
    <td align="right">2.79</td>
    <td align="right">2.79</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.59</td>
    <td align="right">4.85</td>
    <td align="right">4.84</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.72</td>
    <td align="right">4.66</td>
    <td align="right">4.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.37</td>
    <td align="right">2.87</td>
    <td align="right">2.88</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.50</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.76</td>
    <td align="right">4.75</td>
    <td align="right">4.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.43</td>
    <td align="right">5.67</td>
    <td align="right">3.92</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">8.19</td>
    <td align="right">8.32</td>
    <td align="right">6.33</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">8.58</td>
    <td align="right">7.96</td>
    <td align="right">6.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.45</td>
    <td align="right">5.72</td>
    <td align="right">3.93</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.89</td>
    <td align="right">9.65</td>
    <td align="right">6.34</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">9.27</td>
    <td align="right">9.21</td>
    <td align="right">6.22</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">47.88</td>
    <td align="right">24.32</td>
    <td align="right">15.33</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">16.81</td>
    <td align="right">14.27</td>
    <td align="right">20.23</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.08</td>
    <td align="right">6.08</td>
    <td align="right">5.84</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">6.55</td>
    <td align="right">6.39</td>
    <td align="right">6.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">46.91</td>
    <td align="right">46.53</td>
    <td align="right">25.35</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.92</td>
    <td align="right">11.54</td>
    <td align="right">11.52</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">12.82</td>
    <td align="right">12.90</td>
    <td align="right">12.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">87.38</td>
    <td align="right">82.94</td>
    <td align="right">31.23</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.57</td>
    <td align="right">18.13</td>
    <td align="right">18.14</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">20.01</td>
    <td align="right">19.68</td>
    <td align="right">19.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">126.46</td>
    <td align="right">116.78</td>
    <td align="right">36.65</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">21.86</td>
    <td align="right">21.94</td>
    <td align="right">21.93</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">25.57</td>
    <td align="right">22.72</td>
    <td align="right">22.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">15.47</td>
    <td align="right">17.22</td>
    <td align="right">21.25</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.83</td>
    <td align="right">5.69</td>
    <td align="right">5.69</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.92</td>
    <td align="right">5.96</td>
    <td align="right">6.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">42.43</td>
    <td align="right">46.30</td>
    <td align="right">26.18</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.97</td>
    <td align="right">12.16</td>
    <td align="right">12.16</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">12.64</td>
    <td align="right">13.61</td>
    <td align="right">13.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">86.18</td>
    <td align="right">94.21</td>
    <td align="right">34.44</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.41</td>
    <td align="right">18.37</td>
    <td align="right">18.38</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.78</td>
    <td align="right">19.29</td>
    <td align="right">19.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">125.07</td>
    <td align="right">134.29</td>
    <td align="right">40.13</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.42</td>
    <td align="right">22.07</td>
    <td align="right">22.07</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">23.50</td>
    <td align="right">23.68</td>
    <td align="right">23.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.48</td>
    <td align="right">6.92</td>
    <td align="right">6.92</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.95</td>
    <td align="right">9.35</td>
    <td align="right">9.31</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">5.54</td>
    <td align="right">5.98</td>
    <td align="right">6.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.18</td>
    <td align="right">14.58</td>
    <td align="right">14.55</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.96</td>
    <td align="right">17.97</td>
    <td align="right">18.07</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.89</td>
    <td align="right">9.03</td>
    <td align="right">9.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">30.15</td>
    <td align="right">30.45</td>
    <td align="right">30.42</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">38.06</td>
    <td align="right">33.43</td>
    <td align="right">33.45</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">19.24</td>
    <td align="right">20.24</td>
    <td align="right">14.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">39.07</td>
    <td align="right">38.92</td>
    <td align="right">38.93</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">40.80</td>
    <td align="right">53.27</td>
    <td align="right">52.98</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">22.39</td>
    <td align="right">23.45</td>
    <td align="right">16.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.44</td>
    <td align="right">7.20</td>
    <td align="right">7.22</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.16</td>
    <td align="right">8.33</td>
    <td align="right">8.31</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.16</td>
    <td align="right">3.90</td>
    <td align="right">3.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.12</td>
    <td align="right">14.48</td>
    <td align="right">14.43</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.28</td>
    <td align="right">18.20</td>
    <td align="right">17.99</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">8.29</td>
    <td align="right">8.62</td>
    <td align="right">8.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.45</td>
    <td align="right">30.40</td>
    <td align="right">30.41</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">37.18</td>
    <td align="right">33.43</td>
    <td align="right">33.41</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">20.86</td>
    <td align="right">21.26</td>
    <td align="right">16.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">39.81</td>
    <td align="right">39.58</td>
    <td align="right">39.53</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">41.73</td>
    <td align="right">52.13</td>
    <td align="right">53.86</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">24.07</td>
    <td align="right">24.17</td>
    <td align="right">17.85</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">4.21</td>
    <td align="right">4.24</td>
    <td align="right">4.18</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.54</td>
    <td align="right">6.16</td>
    <td align="right">6.14</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">6.01</td>
    <td align="right">6.58</td>
    <td align="right">6.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">8.18</td>
    <td align="right">9.05</td>
    <td align="right">9.04</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">8.97</td>
    <td align="right">10.66</td>
    <td align="right">10.76</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">10.20</td>
    <td align="right">12.07</td>
    <td align="right">12.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">17.95</td>
    <td align="right">18.82</td>
    <td align="right">14.57</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.51</td>
    <td align="right">26.25</td>
    <td align="right">21.57</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">25.78</td>
    <td align="right">26.69</td>
    <td align="right">21.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">20.81</td>
    <td align="right">21.40</td>
    <td align="right">16.31</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">31.95</td>
    <td align="right">35.96</td>
    <td align="right">24.94</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.54</td>
    <td align="right">33.33</td>
    <td align="right">24.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.58</td>
    <td align="right">4.23</td>
    <td align="right">4.24</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.86</td>
    <td align="right">6.25</td>
    <td align="right">6.23</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.96</td>
    <td align="right">6.02</td>
    <td align="right">6.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.95</td>
    <td align="right">8.71</td>
    <td align="right">8.77</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.55</td>
    <td align="right">9.49</td>
    <td align="right">9.48</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.10</td>
    <td align="right">12.69</td>
    <td align="right">12.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">17.07</td>
    <td align="right">20.57</td>
    <td align="right">14.70</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.59</td>
    <td align="right">26.60</td>
    <td align="right">22.04</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">25.66</td>
    <td align="right">26.21</td>
    <td align="right">21.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">19.75</td>
    <td align="right">23.72</td>
    <td align="right">16.52</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.29</td>
    <td align="right">37.02</td>
    <td align="right">25.33</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">32.35</td>
    <td align="right">36.60</td>
    <td align="right">25.02</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.15</td>
    <td align="right">5.88</td>
    <td align="right">4.29</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.59</td>
    <td align="right">10.64</td>
    <td align="right">17.12</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.59</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.11</td>
    <td align="right">4.65</td>
    <td align="right">4.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.77</td>
    <td align="right">15.46</td>
    <td align="right">18.51</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.16</td>
    <td align="right">4.66</td>
    <td align="right">4.66</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.68</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.79</td>
    <td align="right">18.61</td>
    <td align="right">17.11</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.65</td>
    <td align="right">5.07</td>
    <td align="right">5.06</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.00</td>
    <td align="right">5.94</td>
    <td align="right">5.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.92</td>
    <td align="right">23.32</td>
    <td align="right">17.97</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.00</td>
    <td align="right">5.61</td>
    <td align="right">5.61</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">3.29</td>
    <td align="right">3.49</td>
    <td align="right">3.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.65</td>
    <td align="right">11.22</td>
    <td align="right">17.66</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.82</td>
    <td align="right">4.30</td>
    <td align="right">4.30</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.22</td>
    <td align="right">4.90</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.34</td>
    <td align="right">16.29</td>
    <td align="right">19.06</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">5.23</td>
    <td align="right">4.74</td>
    <td align="right">4.74</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.82</td>
    <td align="right">5.60</td>
    <td align="right">5.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">19.27</td>
    <td align="right">20.14</td>
    <td align="right">17.62</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.84</td>
    <td align="right">5.18</td>
    <td align="right">5.18</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.14</td>
    <td align="right">6.04</td>
    <td align="right">6.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.19</td>
    <td align="right">24.74</td>
    <td align="right">18.02</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">6.11</td>
    <td align="right">5.80</td>
    <td align="right">5.80</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.46</td>
    <td align="right">3.72</td>
    <td align="right">3.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.35</td>
    <td align="right">3.89</td>
    <td align="right">3.91</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.43</td>
    <td align="right">3.76</td>
    <td align="right">3.76</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.84</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.03</td>
    <td align="right">3.90</td>
    <td align="right">3.89</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.01</td>
    <td align="right">4.04</td>
    <td align="right">4.05</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.27</td>
    <td align="right">2.32</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.98</td>
    <td align="right">6.63</td>
    <td align="right">6.47</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">6.12</td>
    <td align="right">6.51</td>
    <td align="right">6.52</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.39</td>
    <td align="right">4.35</td>
    <td align="right">3.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.51</td>
    <td align="right">7.44</td>
    <td align="right">7.46</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.94</td>
    <td align="right">7.69</td>
    <td align="right">7.68</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.43</td>
    <td align="right">4.35</td>
    <td align="right">3.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.44</td>
    <td align="right">4.15</td>
    <td align="right">4.14</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.56</td>
    <td align="right">3.99</td>
    <td align="right">4.00</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.07</td>
    <td align="right">2.82</td>
    <td align="right">2.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.92</td>
    <td align="right">4.19</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.16</td>
    <td align="right">4.36</td>
    <td align="right">4.36</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">3.26</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">6.24</td>
    <td align="right">7.08</td>
    <td align="right">7.10</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">6.47</td>
    <td align="right">6.82</td>
    <td align="right">6.81</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.66</td>
    <td align="right">4.69</td>
    <td align="right">3.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.60</td>
    <td align="right">7.52</td>
    <td align="right">7.51</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">7.12</td>
    <td align="right">7.79</td>
    <td align="right">7.77</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.71</td>
    <td align="right">4.72</td>
    <td align="right">3.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.79</td>
    <td align="right">2.36</td>
    <td align="right">2.36</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.87</td>
    <td align="right">4.11</td>
    <td align="right">4.11</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.97</td>
    <td align="right">3.93</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.90</td>
    <td align="right">2.42</td>
    <td align="right">2.41</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.21</td>
    <td align="right">3.83</td>
    <td align="right">3.83</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.13</td>
    <td align="right">4.03</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.50</td>
    <td align="right">4.29</td>
    <td align="right">3.03</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.84</td>
    <td align="right">6.30</td>
    <td align="right">5.06</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">6.07</td>
    <td align="right">6.11</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.55</td>
    <td align="right">4.30</td>
    <td align="right">3.01</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.95</td>
    <td align="right">7.14</td>
    <td align="right">5.11</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">7.26</td>
    <td align="right">6.98</td>
    <td align="right">4.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.99</td>
    <td align="right">2.64</td>
    <td align="right">2.65</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.04</td>
    <td align="right">4.43</td>
    <td align="right">4.43</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.14</td>
    <td align="right">4.17</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.12</td>
    <td align="right">2.71</td>
    <td align="right">2.72</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.96</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.35</td>
    <td align="right">4.26</td>
    <td align="right">4.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.74</td>
    <td align="right">4.54</td>
    <td align="right">3.32</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">6.25</td>
    <td align="right">6.64</td>
    <td align="right">5.24</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.40</td>
    <td align="right">6.46</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.82</td>
    <td align="right">4.58</td>
    <td align="right">3.29</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.24</td>
    <td align="right">7.64</td>
    <td align="right">5.32</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.58</td>
    <td align="right">7.39</td>
    <td align="right">5.17</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">50.68</td>
    <td align="right">23.78</td>
    <td align="right">14.61</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">12.33</td>
    <td align="right">13.28</td>
    <td align="right">19.56</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.82</td>
    <td align="right">5.41</td>
    <td align="right">5.43</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.35</td>
    <td align="right">6.07</td>
    <td align="right">6.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">45.13</td>
    <td align="right">44.57</td>
    <td align="right">25.84</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.14</td>
    <td align="right">11.01</td>
    <td align="right">10.97</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.45</td>
    <td align="right">12.77</td>
    <td align="right">12.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">71.10</td>
    <td align="right">74.16</td>
    <td align="right">29.99</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.30</td>
    <td align="right">17.64</td>
    <td align="right">17.69</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.99</td>
    <td align="right">20.74</td>
    <td align="right">20.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">104.17</td>
    <td align="right">104.45</td>
    <td align="right">35.53</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.37</td>
    <td align="right">21.56</td>
    <td align="right">21.55</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.55</td>
    <td align="right">15.35</td>
    <td align="right">15.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">13.24</td>
    <td align="right">14.10</td>
    <td align="right">20.07</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">6.78</td>
    <td align="right">6.25</td>
    <td align="right">6.29</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.85</td>
    <td align="right">6.73</td>
    <td align="right">6.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">37.55</td>
    <td align="right">38.41</td>
    <td align="right">24.61</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">12.10</td>
    <td align="right">11.19</td>
    <td align="right">11.18</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.40</td>
    <td align="right">12.73</td>
    <td align="right">12.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">81.47</td>
    <td align="right">83.47</td>
    <td align="right">30.53</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.59</td>
    <td align="right">17.75</td>
    <td align="right">17.75</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.82</td>
    <td align="right">20.57</td>
    <td align="right">20.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">122.73</td>
    <td align="right">119.82</td>
    <td align="right">36.69</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.29</td>
    <td align="right">21.62</td>
    <td align="right">21.62</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.74</td>
    <td align="right">16.69</td>
    <td align="right">16.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">4.10</td>
    <td align="right">4.73</td>
    <td align="right">4.75</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.13</td>
    <td align="right">4.61</td>
    <td align="right">4.64</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.59</td>
    <td align="right">3.44</td>
    <td align="right">3.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.07</td>
    <td align="right">9.35</td>
    <td align="right">9.29</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">10.29</td>
    <td align="right">11.82</td>
    <td align="right">11.85</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.62</td>
    <td align="right">6.92</td>
    <td align="right">6.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">19.63</td>
    <td align="right">21.51</td>
    <td align="right">21.53</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.90</td>
    <td align="right">21.71</td>
    <td align="right">21.74</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">15.10</td>
    <td align="right">16.30</td>
    <td align="right">12.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">24.22</td>
    <td align="right">26.81</td>
    <td align="right">26.84</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">24.64</td>
    <td align="right">30.23</td>
    <td align="right">30.24</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.97</td>
    <td align="right">18.18</td>
    <td align="right">13.43</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.57</td>
    <td align="right">5.37</td>
    <td align="right">5.49</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.11</td>
    <td align="right">4.54</td>
    <td align="right">4.57</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.96</td>
    <td align="right">3.81</td>
    <td align="right">3.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">9.72</td>
    <td align="right">9.85</td>
    <td align="right">9.83</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">10.31</td>
    <td align="right">11.74</td>
    <td align="right">11.78</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">9.01</td>
    <td align="right">7.77</td>
    <td align="right">7.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">20.20</td>
    <td align="right">22.06</td>
    <td align="right">22.07</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.25</td>
    <td align="right">21.81</td>
    <td align="right">21.82</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.43</td>
    <td align="right">17.41</td>
    <td align="right">12.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">24.98</td>
    <td align="right">26.88</td>
    <td align="right">26.88</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">26.54</td>
    <td align="right">30.45</td>
    <td align="right">30.42</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.87</td>
    <td align="right">19.88</td>
    <td align="right">14.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.74</td>
    <td align="right">3.45</td>
    <td align="right">3.46</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.00</td>
    <td align="right">5.46</td>
    <td align="right">5.45</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.31</td>
    <td align="right">5.54</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">7.59</td>
    <td align="right">7.64</td>
    <td align="right">7.65</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">8.43</td>
    <td align="right">9.72</td>
    <td align="right">9.71</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">9.58</td>
    <td align="right">10.88</td>
    <td align="right">10.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">15.21</td>
    <td align="right">16.43</td>
    <td align="right">11.90</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.67</td>
    <td align="right">21.29</td>
    <td align="right">16.90</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">19.90</td>
    <td align="right">22.72</td>
    <td align="right">17.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">17.27</td>
    <td align="right">18.30</td>
    <td align="right">13.20</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">24.88</td>
    <td align="right">26.90</td>
    <td align="right">19.24</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">25.05</td>
    <td align="right">26.71</td>
    <td align="right">19.33</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">5.01</td>
    <td align="right">4.84</td>
    <td align="right">4.81</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.32</td>
    <td align="right">5.87</td>
    <td align="right">5.89</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.96</td>
    <td align="right">5.12</td>
    <td align="right">5.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.83</td>
    <td align="right">8.71</td>
    <td align="right">8.76</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.90</td>
    <td align="right">9.94</td>
    <td align="right">9.93</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.35</td>
    <td align="right">11.74</td>
    <td align="right">11.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.65</td>
    <td align="right">17.58</td>
    <td align="right">12.80</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">20.57</td>
    <td align="right">22.14</td>
    <td align="right">18.46</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.47</td>
    <td align="right">21.81</td>
    <td align="right">17.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.86</td>
    <td align="right">19.93</td>
    <td align="right">14.38</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">27.77</td>
    <td align="right">29.84</td>
    <td align="right">21.53</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.23</td>
    <td align="right">30.01</td>
    <td align="right">19.70</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.66</td>
    <td align="right">2.50</td>
    <td align="right">1.96</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">6.31</td>
    <td align="right">4.38</td>
    <td align="right">11.48</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.31</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.62</td>
    <td align="right">1.28</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">9.47</td>
    <td align="right">6.63</td>
    <td align="right">11.75</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.37</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.69</td>
    <td align="right">1.41</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">12.36</td>
    <td align="right">8.16</td>
    <td align="right">11.04</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.52</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.74</td>
    <td align="right">1.56</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">15.42</td>
    <td align="right">10.66</td>
    <td align="right">11.23</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.72</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.80</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.35</td>
    <td align="right">4.16</td>
    <td align="right">11.37</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.31</td>
    <td align="right">1.25</td>
    <td align="right">1.24</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.62</td>
    <td align="right">1.28</td>
    <td align="right">1.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.40</td>
    <td align="right">6.05</td>
    <td align="right">11.94</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.40</td>
    <td align="right">1.41</td>
    <td align="right">1.42</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.69</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.57</td>
    <td align="right">7.33</td>
    <td align="right">11.17</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.75</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.87</td>
    <td align="right">9.35</td>
    <td align="right">11.39</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.80</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.80</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.27</td>
    <td align="right">1.71</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.33</td>
    <td align="right">1.76</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.03</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.16</td>
    <td align="right">1.93</td>
    <td align="right">1.92</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.81</td>
    <td align="right">2.24</td>
    <td align="right">2.19</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.50</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.09</td>
    <td align="right">2.89</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.06</td>
    <td align="right">2.94</td>
    <td align="right">2.93</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">2.90</td>
    <td align="right">2.39</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.72</td>
    <td align="right">3.70</td>
    <td align="right">3.68</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.66</td>
    <td align="right">4.35</td>
    <td align="right">4.30</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">2.93</td>
    <td align="right">2.92</td>
    <td align="right">1.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.29</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.33</td>
    <td align="right">1.77</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.00</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.17</td>
    <td align="right">1.92</td>
    <td align="right">1.91</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.72</td>
    <td align="right">2.20</td>
    <td align="right">2.19</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.51</td>
    <td align="right">1.39</td>
    <td align="right">1.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.03</td>
    <td align="right">2.86</td>
    <td align="right">2.90</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.09</td>
    <td align="right">2.99</td>
    <td align="right">2.94</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.96</td>
    <td align="right">2.40</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.50</td>
    <td align="right">3.66</td>
    <td align="right">3.64</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.72</td>
    <td align="right">4.36</td>
    <td align="right">4.30</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.90</td>
    <td align="right">2.93</td>
    <td align="right">1.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.01</td>
    <td align="right">1.69</td>
    <td align="right">1.67</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.22</td>
    <td align="right">1.70</td>
    <td align="right">1.68</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.32</td>
    <td align="right">1.75</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.07</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.15</td>
    <td align="right">1.92</td>
    <td align="right">1.92</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.78</td>
    <td align="right">2.26</td>
    <td align="right">2.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">2.85</td>
    <td align="right">2.37</td>
    <td align="right">1.73</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.08</td>
    <td align="right">2.88</td>
    <td align="right">2.88</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.05</td>
    <td align="right">2.94</td>
    <td align="right">2.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">2.88</td>
    <td align="right">2.85</td>
    <td align="right">1.73</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.60</td>
    <td align="right">3.71</td>
    <td align="right">3.71</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.70</td>
    <td align="right">4.28</td>
    <td align="right">4.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.00</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.30</td>
    <td align="right">1.73</td>
    <td align="right">1.72</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.34</td>
    <td align="right">1.76</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.04</td>
    <td align="right">1.61</td>
    <td align="right">1.62</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.22</td>
    <td align="right">1.95</td>
    <td align="right">1.95</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.84</td>
    <td align="right">2.21</td>
    <td align="right">2.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.90</td>
    <td align="right">2.42</td>
    <td align="right">1.77</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.17</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.08</td>
    <td align="right">2.95</td>
    <td align="right">2.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.91</td>
    <td align="right">2.90</td>
    <td align="right">1.75</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.58</td>
    <td align="right">3.69</td>
    <td align="right">3.69</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.69</td>
    <td align="right">4.38</td>
    <td align="right">4.36</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.36</td>
    <td align="right">11.04</td>
    <td align="right">5.78</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">7.81</td>
    <td align="right">6.54</td>
    <td align="right">13.18</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">2.08</td>
    <td align="right">2.06</td>
    <td align="right">2.07</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.21</td>
    <td align="right">2.18</td>
    <td align="right">2.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">13.03</td>
    <td align="right">11.15</td>
    <td align="right">15.91</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">3.63</td>
    <td align="right">3.48</td>
    <td align="right">3.88</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">3.46</td>
    <td align="right">3.25</td>
    <td align="right">3.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">31.49</td>
    <td align="right">25.27</td>
    <td align="right">18.06</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">7.11</td>
    <td align="right">6.30</td>
    <td align="right">6.23</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.85</td>
    <td align="right">6.20</td>
    <td align="right">6.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">54.83</td>
    <td align="right">39.52</td>
    <td align="right">20.52</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.92</td>
    <td align="right">7.51</td>
    <td align="right">7.71</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.49</td>
    <td align="right">6.45</td>
    <td align="right">6.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.82</td>
    <td align="right">6.45</td>
    <td align="right">13.29</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.15</td>
    <td align="right">2.10</td>
    <td align="right">2.13</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.21</td>
    <td align="right">2.14</td>
    <td align="right">2.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.25</td>
    <td align="right">11.74</td>
    <td align="right">16.36</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.54</td>
    <td align="right">3.56</td>
    <td align="right">3.58</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.30</td>
    <td align="right">3.22</td>
    <td align="right">3.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">28.43</td>
    <td align="right">23.10</td>
    <td align="right">18.37</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">6.73</td>
    <td align="right">6.52</td>
    <td align="right">6.47</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.79</td>
    <td align="right">6.18</td>
    <td align="right">6.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">52.00</td>
    <td align="right">40.22</td>
    <td align="right">20.82</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.25</td>
    <td align="right">8.05</td>
    <td align="right">8.06</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.77</td>
    <td align="right">6.64</td>
    <td align="right">6.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.76</td>
    <td align="right">2.68</td>
    <td align="right">2.75</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.80</td>
    <td align="right">2.74</td>
    <td align="right">2.80</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.48</td>
    <td align="right">2.70</td>
    <td align="right">2.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.06</td>
    <td align="right">4.58</td>
    <td align="right">4.62</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.31</td>
    <td align="right">4.97</td>
    <td align="right">4.99</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.22</td>
    <td align="right">3.59</td>
    <td align="right">3.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.46</td>
    <td align="right">9.38</td>
    <td align="right">9.77</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">10.69</td>
    <td align="right">9.37</td>
    <td align="right">9.25</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.78</td>
    <td align="right">7.48</td>
    <td align="right">5.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.25</td>
    <td align="right">14.00</td>
    <td align="right">14.49</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.28</td>
    <td align="right">16.39</td>
    <td align="right">16.19</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.49</td>
    <td align="right">11.17</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.78</td>
    <td align="right">2.67</td>
    <td align="right">2.73</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.80</td>
    <td align="right">2.74</td>
    <td align="right">2.78</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.45</td>
    <td align="right">2.70</td>
    <td align="right">2.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">4.05</td>
    <td align="right">4.73</td>
    <td align="right">4.99</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.25</td>
    <td align="right">4.69</td>
    <td align="right">4.70</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.78</td>
    <td align="right">3.37</td>
    <td align="right">3.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">10.88</td>
    <td align="right">9.54</td>
    <td align="right">9.57</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">11.32</td>
    <td align="right">9.54</td>
    <td align="right">9.18</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.97</td>
    <td align="right">8.48</td>
    <td align="right">5.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">15.66</td>
    <td align="right">14.16</td>
    <td align="right">14.15</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">16.08</td>
    <td align="right">16.68</td>
    <td align="right">16.79</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">10.75</td>
    <td align="right">11.09</td>
    <td align="right">6.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">2.44</td>
    <td align="right">2.67</td>
    <td align="right">2.70</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.78</td>
    <td align="right">2.65</td>
    <td align="right">2.71</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.80</td>
    <td align="right">2.73</td>
    <td align="right">2.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.08</td>
    <td align="right">3.11</td>
    <td align="right">3.35</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.36</td>
    <td align="right">4.41</td>
    <td align="right">4.76</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.36</td>
    <td align="right">5.26</td>
    <td align="right">4.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.99</td>
    <td align="right">8.34</td>
    <td align="right">5.66</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.89</td>
    <td align="right">9.99</td>
    <td align="right">9.44</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.49</td>
    <td align="right">9.51</td>
    <td align="right">9.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.86</td>
    <td align="right">11.36</td>
    <td align="right">6.30</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.33</td>
    <td align="right">14.71</td>
    <td align="right">14.95</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.68</td>
    <td align="right">16.35</td>
    <td align="right">15.66</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.39</td>
    <td align="right">2.60</td>
    <td align="right">2.65</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.73</td>
    <td align="right">2.62</td>
    <td align="right">2.68</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.75</td>
    <td align="right">2.68</td>
    <td align="right">2.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.79</td>
    <td align="right">2.94</td>
    <td align="right">3.07</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.69</td>
    <td align="right">4.08</td>
    <td align="right">4.07</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.12</td>
    <td align="right">4.76</td>
    <td align="right">4.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.33</td>
    <td align="right">7.43</td>
    <td align="right">5.15</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.53</td>
    <td align="right">8.74</td>
    <td align="right">8.78</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.52</td>
    <td align="right">8.51</td>
    <td align="right">8.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.47</td>
    <td align="right">10.22</td>
    <td align="right">5.97</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.18</td>
    <td align="right">13.14</td>
    <td align="right">13.14</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.65</td>
    <td align="right">15.24</td>
    <td align="right">15.23</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.05</td>
    <td align="right">8.03</td>
    <td align="right">3.63</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.24</td>
    <td align="right">10.48</td>
    <td align="right">13.81</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.69</td>
    <td align="right">3.42</td>
    <td align="right">3.43</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.26</td>
    <td align="right">4.09</td>
    <td align="right">4.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.56</td>
    <td align="right">14.57</td>
    <td align="right">14.22</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.31</td>
    <td align="right">3.81</td>
    <td align="right">3.79</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.92</td>
    <td align="right">4.73</td>
    <td align="right">4.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.38</td>
    <td align="right">17.85</td>
    <td align="right">13.61</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.95</td>
    <td align="right">4.28</td>
    <td align="right">4.26</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.59</td>
    <td align="right">5.12</td>
    <td align="right">5.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.31</td>
    <td align="right">22.83</td>
    <td align="right">14.01</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.61</td>
    <td align="right">4.61</td>
    <td align="right">4.62</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.16</td>
    <td align="right">5.51</td>
    <td align="right">5.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.25</td>
    <td align="right">11.28</td>
    <td align="right">14.28</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.81</td>
    <td align="right">3.56</td>
    <td align="right">3.56</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.34</td>
    <td align="right">4.15</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.09</td>
    <td align="right">16.17</td>
    <td align="right">14.72</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.38</td>
    <td align="right">3.96</td>
    <td align="right">3.93</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.03</td>
    <td align="right">4.77</td>
    <td align="right">4.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.21</td>
    <td align="right">20.27</td>
    <td align="right">13.94</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.06</td>
    <td align="right">4.37</td>
    <td align="right">4.32</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.67</td>
    <td align="right">5.13</td>
    <td align="right">5.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.80</td>
    <td align="right">24.98</td>
    <td align="right">14.34</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.71</td>
    <td align="right">4.71</td>
    <td align="right">4.70</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.28</td>
    <td align="right">5.59</td>
    <td align="right">5.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.27</td>
    <td align="right">4.30</td>
    <td align="right">4.29</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">7.85</td>
    <td align="right">4.57</td>
    <td align="right">4.59</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.85</td>
    <td align="right">2.10</td>
    <td align="right">2.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.16</td>
    <td align="right">6.98</td>
    <td align="right">6.85</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">14.06</td>
    <td align="right">6.86</td>
    <td align="right">6.68</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.77</td>
    <td align="right">2.91</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.47</td>
    <td align="right">9.89</td>
    <td align="right">9.75</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">12.85</td>
    <td align="right">10.63</td>
    <td align="right">10.41</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.25</td>
    <td align="right">4.36</td>
    <td align="right">3.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.54</td>
    <td align="right">11.06</td>
    <td align="right">11.03</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">13.91</td>
    <td align="right">12.27</td>
    <td align="right">12.23</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.30</td>
    <td align="right">4.41</td>
    <td align="right">3.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.37</td>
    <td align="right">4.36</td>
    <td align="right">4.37</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.46</td>
    <td align="right">4.68</td>
    <td align="right">4.68</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.85</td>
    <td align="right">2.19</td>
    <td align="right">2.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.23</td>
    <td align="right">7.11</td>
    <td align="right">7.05</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.72</td>
    <td align="right">7.00</td>
    <td align="right">6.83</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.74</td>
    <td align="right">2.93</td>
    <td align="right">2.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.48</td>
    <td align="right">10.07</td>
    <td align="right">10.00</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.13</td>
    <td align="right">10.54</td>
    <td align="right">10.43</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.26</td>
    <td align="right">4.42</td>
    <td align="right">3.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.74</td>
    <td align="right">11.05</td>
    <td align="right">11.03</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.89</td>
    <td align="right">12.37</td>
    <td align="right">12.28</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.29</td>
    <td align="right">4.41</td>
    <td align="right">3.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.79</td>
    <td align="right">1.90</td>
    <td align="right">1.90</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.70</td>
    <td align="right">3.19</td>
    <td align="right">3.19</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.75</td>
    <td align="right">2.99</td>
    <td align="right">2.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.22</td>
    <td align="right">3.27</td>
    <td align="right">2.63</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.21</td>
    <td align="right">3.81</td>
    <td align="right">3.20</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">5.98</td>
    <td align="right">4.51</td>
    <td align="right">3.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.36</td>
    <td align="right">4.20</td>
    <td align="right">2.88</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.79</td>
    <td align="right">6.24</td>
    <td align="right">4.80</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.19</td>
    <td align="right">6.18</td>
    <td align="right">4.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.40</td>
    <td align="right">4.21</td>
    <td align="right">2.88</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.41</td>
    <td align="right">6.87</td>
    <td align="right">4.84</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.72</td>
    <td align="right">6.64</td>
    <td align="right">4.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.80</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.71</td>
    <td align="right">3.25</td>
    <td align="right">3.24</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.76</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.23</td>
    <td align="right">3.44</td>
    <td align="right">2.76</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.16</td>
    <td align="right">3.79</td>
    <td align="right">3.20</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.66</td>
    <td align="right">4.65</td>
    <td align="right">3.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.34</td>
    <td align="right">4.27</td>
    <td align="right">2.97</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.92</td>
    <td align="right">7.67</td>
    <td align="right">6.18</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.67</td>
    <td align="right">6.24</td>
    <td align="right">4.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.41</td>
    <td align="right">4.32</td>
    <td align="right">2.98</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.81</td>
    <td align="right">7.04</td>
    <td align="right">5.04</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.02</td>
    <td align="right">6.87</td>
    <td align="right">5.09</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">40.13</td>
    <td align="right">23.20</td>
    <td align="right">12.49</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">9.96</td>
    <td align="right">11.01</td>
    <td align="right">15.23</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.03</td>
    <td align="right">3.66</td>
    <td align="right">3.64</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.61</td>
    <td align="right">4.40</td>
    <td align="right">4.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">16.12</td>
    <td align="right">16.70</td>
    <td align="right">15.92</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.49</td>
    <td align="right">6.09</td>
    <td align="right">5.75</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">7.31</td>
    <td align="right">6.99</td>
    <td align="right">6.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">64.33</td>
    <td align="right">74.08</td>
    <td align="right">24.77</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">15.12</td>
    <td align="right">13.39</td>
    <td align="right">13.44</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.17</td>
    <td align="right">15.86</td>
    <td align="right">15.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">96.83</td>
    <td align="right">109.71</td>
    <td align="right">29.66</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.47</td>
    <td align="right">16.72</td>
    <td align="right">16.51</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">20.47</td>
    <td align="right">22.70</td>
    <td align="right">22.76</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">11.10</td>
    <td align="right">11.76</td>
    <td align="right">15.71</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.27</td>
    <td align="right">3.82</td>
    <td align="right">3.77</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.78</td>
    <td align="right">4.56</td>
    <td align="right">4.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">17.61</td>
    <td align="right">18.37</td>
    <td align="right">16.56</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.88</td>
    <td align="right">6.40</td>
    <td align="right">6.03</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">7.14</td>
    <td align="right">6.88</td>
    <td align="right">6.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.06</td>
    <td align="right">78.88</td>
    <td align="right">25.83</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.48</td>
    <td align="right">13.55</td>
    <td align="right">13.60</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.51</td>
    <td align="right">15.84</td>
    <td align="right">15.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">102.67</td>
    <td align="right">118.22</td>
    <td align="right">31.32</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.61</td>
    <td align="right">18.21</td>
    <td align="right">18.30</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.75</td>
    <td align="right">22.58</td>
    <td align="right">22.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.97</td>
    <td align="right">4.67</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">8.62</td>
    <td align="right">5.00</td>
    <td align="right">4.91</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.18</td>
    <td align="right">2.28</td>
    <td align="right">2.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.65</td>
    <td align="right">9.24</td>
    <td align="right">9.03</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.87</td>
    <td align="right">9.86</td>
    <td align="right">9.36</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">4.97</td>
    <td align="right">5.15</td>
    <td align="right">4.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">26.50</td>
    <td align="right">26.27</td>
    <td align="right">26.27</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">29.61</td>
    <td align="right">28.65</td>
    <td align="right">28.63</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">13.94</td>
    <td align="right">15.35</td>
    <td align="right">10.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">36.13</td>
    <td align="right">35.81</td>
    <td align="right">35.93</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">40.05</td>
    <td align="right">38.09</td>
    <td align="right">38.01</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.39</td>
    <td align="right">17.84</td>
    <td align="right">12.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.12</td>
    <td align="right">4.74</td>
    <td align="right">4.66</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">8.56</td>
    <td align="right">5.07</td>
    <td align="right">5.00</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.14</td>
    <td align="right">2.36</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.59</td>
    <td align="right">9.70</td>
    <td align="right">9.36</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.86</td>
    <td align="right">9.57</td>
    <td align="right">9.24</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.93</td>
    <td align="right">8.78</td>
    <td align="right">7.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">25.82</td>
    <td align="right">25.19</td>
    <td align="right">25.34</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.55</td>
    <td align="right">28.67</td>
    <td align="right">28.64</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.03</td>
    <td align="right">15.34</td>
    <td align="right">10.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.00</td>
    <td align="right">35.39</td>
    <td align="right">35.49</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.70</td>
    <td align="right">38.04</td>
    <td align="right">37.99</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.33</td>
    <td align="right">17.77</td>
    <td align="right">12.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.13</td>
    <td align="right">2.08</td>
    <td align="right">2.00</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.05</td>
    <td align="right">3.39</td>
    <td align="right">3.35</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.15</td>
    <td align="right">3.18</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">5.30</td>
    <td align="right">5.48</td>
    <td align="right">4.37</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">6.13</td>
    <td align="right">5.72</td>
    <td align="right">4.93</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">8.06</td>
    <td align="right">6.80</td>
    <td align="right">5.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">14.28</td>
    <td align="right">15.08</td>
    <td align="right">10.72</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">22.53</td>
    <td align="right">18.81</td>
    <td align="right">15.76</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">23.54</td>
    <td align="right">18.89</td>
    <td align="right">15.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">17.80</td>
    <td align="right">17.79</td>
    <td align="right">12.24</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">29.42</td>
    <td align="right">26.67</td>
    <td align="right">18.80</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.93</td>
    <td align="right">24.42</td>
    <td align="right">18.79</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.12</td>
    <td align="right">2.23</td>
    <td align="right">2.15</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.09</td>
    <td align="right">3.49</td>
    <td align="right">3.43</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.18</td>
    <td align="right">3.33</td>
    <td align="right">3.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.37</td>
    <td align="right">9.64</td>
    <td align="right">8.00</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">6.33</td>
    <td align="right">5.94</td>
    <td align="right">5.48</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">8.13</td>
    <td align="right">7.20</td>
    <td align="right">5.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.88</td>
    <td align="right">17.05</td>
    <td align="right">11.88</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.00</td>
    <td align="right">18.95</td>
    <td align="right">16.05</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.68</td>
    <td align="right">18.94</td>
    <td align="right">16.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.84</td>
    <td align="right">17.92</td>
    <td align="right">12.37</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.75</td>
    <td align="right">27.07</td>
    <td align="right">19.06</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.84</td>
    <td align="right">26.96</td>
    <td align="right">19.05</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">73.99</td>
    <td align="right">34.12</td>
    <td align="right">14.26</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.88</td>
    <td align="right">44.29</td>
    <td align="right">37.71</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">13.33</td>
    <td align="right">18.29</td>
    <td align="right">18.29</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">17.25</td>
    <td align="right">20.11</td>
    <td align="right">20.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">41.83</td>
    <td align="right">68.01</td>
    <td align="right">41.05</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">18.35</td>
    <td align="right">21.70</td>
    <td align="right">21.36</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.05</td>
    <td align="right">18.92</td>
    <td align="right">19.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">51.04</td>
    <td align="right">83.15</td>
    <td align="right">38.92</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.43</td>
    <td align="right">19.31</td>
    <td align="right">19.09</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">17.42</td>
    <td align="right">21.11</td>
    <td align="right">21.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">64.95</td>
    <td align="right">106.16</td>
    <td align="right">39.91</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.49</td>
    <td align="right">20.58</td>
    <td align="right">20.57</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.20</td>
    <td align="right">22.06</td>
    <td align="right">23.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.80</td>
    <td align="right">44.11</td>
    <td align="right">37.61</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.32</td>
    <td align="right">16.21</td>
    <td align="right">16.10</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.59</td>
    <td align="right">17.92</td>
    <td align="right">17.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.53</td>
    <td align="right">67.45</td>
    <td align="right">40.40</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.49</td>
    <td align="right">18.35</td>
    <td align="right">18.30</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.08</td>
    <td align="right">19.05</td>
    <td align="right">19.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.23</td>
    <td align="right">81.88</td>
    <td align="right">39.07</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.38</td>
    <td align="right">20.48</td>
    <td align="right">20.49</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.07</td>
    <td align="right">21.05</td>
    <td align="right">21.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">73.35</td>
    <td align="right">100.78</td>
    <td align="right">40.59</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.66</td>
    <td align="right">22.19</td>
    <td align="right">22.20</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.59</td>
    <td align="right">22.15</td>
    <td align="right">22.09</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.51</td>
    <td align="right">22.08</td>
    <td align="right">22.01</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.61</td>
    <td align="right">25.55</td>
    <td align="right">25.55</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">12.11</td>
    <td align="right">15.53</td>
    <td align="right">15.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">26.07</td>
    <td align="right">29.63</td>
    <td align="right">29.67</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.31</td>
    <td align="right">32.54</td>
    <td align="right">32.61</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">14.19</td>
    <td align="right">17.86</td>
    <td align="right">17.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">32.11</td>
    <td align="right">35.47</td>
    <td align="right">35.51</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.38</td>
    <td align="right">48.12</td>
    <td align="right">48.20</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">16.41</td>
    <td align="right">20.85</td>
    <td align="right">20.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.36</td>
    <td align="right">39.89</td>
    <td align="right">40.02</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.80</td>
    <td align="right">56.33</td>
    <td align="right">56.67</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.73</td>
    <td align="right">25.20</td>
    <td align="right">25.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.88</td>
    <td align="right">22.79</td>
    <td align="right">22.80</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.23</td>
    <td align="right">26.33</td>
    <td align="right">26.43</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.30</td>
    <td align="right">15.59</td>
    <td align="right">15.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.49</td>
    <td align="right">30.21</td>
    <td align="right">30.23</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.05</td>
    <td align="right">34.62</td>
    <td align="right">34.62</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.82</td>
    <td align="right">18.37</td>
    <td align="right">18.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.32</td>
    <td align="right">36.74</td>
    <td align="right">36.72</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.65</td>
    <td align="right">48.10</td>
    <td align="right">48.19</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">16.83</td>
    <td align="right">20.83</td>
    <td align="right">20.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">38.00</td>
    <td align="right">41.92</td>
    <td align="right">42.06</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.51</td>
    <td align="right">56.50</td>
    <td align="right">56.60</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.67</td>
    <td align="right">25.94</td>
    <td align="right">26.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">14.09</td>
    <td align="right">16.71</td>
    <td align="right">15.76</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.44</td>
    <td align="right">22.29</td>
    <td align="right">22.08</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.61</td>
    <td align="right">25.56</td>
    <td align="right">25.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">18.89</td>
    <td align="right">19.55</td>
    <td align="right">19.29</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">26.00</td>
    <td align="right">29.61</td>
    <td align="right">29.60</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.33</td>
    <td align="right">32.56</td>
    <td align="right">32.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">23.70</td>
    <td align="right">24.38</td>
    <td align="right">23.64</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">32.00</td>
    <td align="right">35.53</td>
    <td align="right">35.53</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.39</td>
    <td align="right">48.12</td>
    <td align="right">48.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">30.89</td>
    <td align="right">32.22</td>
    <td align="right">32.17</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.09</td>
    <td align="right">40.01</td>
    <td align="right">39.96</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.86</td>
    <td align="right">56.33</td>
    <td align="right">56.70</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.05</td>
    <td align="right">17.11</td>
    <td align="right">16.95</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.71</td>
    <td align="right">22.81</td>
    <td align="right">22.79</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.25</td>
    <td align="right">26.35</td>
    <td align="right">26.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.28</td>
    <td align="right">20.49</td>
    <td align="right">20.48</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.54</td>
    <td align="right">30.23</td>
    <td align="right">30.18</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.11</td>
    <td align="right">34.60</td>
    <td align="right">34.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">22.55</td>
    <td align="right">24.05</td>
    <td align="right">24.06</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.25</td>
    <td align="right">36.89</td>
    <td align="right">36.88</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.60</td>
    <td align="right">48.07</td>
    <td align="right">48.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.05</td>
    <td align="right">34.66</td>
    <td align="right">34.65</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.37</td>
    <td align="right">41.96</td>
    <td align="right">42.04</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.47</td>
    <td align="right">56.52</td>
    <td align="right">56.59</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">108.16</td>
    <td align="right">127.19</td>
    <td align="right">27.14</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">34.21</td>
    <td align="right">54.16</td>
    <td align="right">46.91</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">15.12</td>
    <td align="right">21.66</td>
    <td align="right">20.92</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">20.25</td>
    <td align="right">26.19</td>
    <td align="right">26.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">88.93</td>
    <td align="right">128.55</td>
    <td align="right">60.01</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">27.81</td>
    <td align="right">30.28</td>
    <td align="right">30.45</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">25.09</td>
    <td align="right">31.34</td>
    <td align="right">31.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">173.19</td>
    <td align="right">252.72</td>
    <td align="right">79.31</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.71</td>
    <td align="right">47.67</td>
    <td align="right">49.12</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">38.95</td>
    <td align="right">49.93</td>
    <td align="right">49.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">268.99</td>
    <td align="right">404.66</td>
    <td align="right">97.92</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">47.42</td>
    <td align="right">62.25</td>
    <td align="right">62.52</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">61.08</td>
    <td align="right">63.92</td>
    <td align="right">64.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">33.83</td>
    <td align="right">48.55</td>
    <td align="right">43.86</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.26</td>
    <td align="right">19.41</td>
    <td align="right">19.64</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.46</td>
    <td align="right">20.85</td>
    <td align="right">20.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">96.32</td>
    <td align="right">127.44</td>
    <td align="right">61.07</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.41</td>
    <td align="right">26.49</td>
    <td align="right">26.18</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.36</td>
    <td align="right">28.09</td>
    <td align="right">28.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">189.54</td>
    <td align="right">247.91</td>
    <td align="right">78.37</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.26</td>
    <td align="right">46.37</td>
    <td align="right">46.40</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.26</td>
    <td align="right">49.64</td>
    <td align="right">49.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.82</td>
    <td align="right">405.77</td>
    <td align="right">98.97</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.08</td>
    <td align="right">63.78</td>
    <td align="right">63.78</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">62.09</td>
    <td align="right">64.20</td>
    <td align="right">63.20</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">24.33</td>
    <td align="right">27.21</td>
    <td align="right">27.14</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">28.67</td>
    <td align="right">30.16</td>
    <td align="right">29.75</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">13.27</td>
    <td align="right">18.02</td>
    <td align="right">17.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">39.24</td>
    <td align="right">43.38</td>
    <td align="right">43.35</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">52.73</td>
    <td align="right">46.95</td>
    <td align="right">45.60</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">23.94</td>
    <td align="right">28.92</td>
    <td align="right">28.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">65.28</td>
    <td align="right">70.32</td>
    <td align="right">69.67</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">101.92</td>
    <td align="right">81.62</td>
    <td align="right">81.67</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">40.84</td>
    <td align="right">44.96</td>
    <td align="right">45.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.62</td>
    <td align="right">92.66</td>
    <td align="right">92.77</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">134.62</td>
    <td align="right">107.43</td>
    <td align="right">107.64</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">69.32</td>
    <td align="right">75.82</td>
    <td align="right">75.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.51</td>
    <td align="right">26.54</td>
    <td align="right">26.47</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.28</td>
    <td align="right">31.65</td>
    <td align="right">32.03</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">14.63</td>
    <td align="right">18.55</td>
    <td align="right">18.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.45</td>
    <td align="right">44.36</td>
    <td align="right">44.25</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.39</td>
    <td align="right">48.77</td>
    <td align="right">48.54</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.43</td>
    <td align="right">29.29</td>
    <td align="right">28.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.91</td>
    <td align="right">71.36</td>
    <td align="right">71.37</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.16</td>
    <td align="right">81.23</td>
    <td align="right">81.02</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">41.49</td>
    <td align="right">44.59</td>
    <td align="right">44.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.70</td>
    <td align="right">94.78</td>
    <td align="right">94.80</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.23</td>
    <td align="right">108.17</td>
    <td align="right">108.33</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.85</td>
    <td align="right">77.06</td>
    <td align="right">76.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">14.99</td>
    <td align="right">17.70</td>
    <td align="right">16.84</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">23.94</td>
    <td align="right">26.65</td>
    <td align="right">26.61</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">30.35</td>
    <td align="right">32.21</td>
    <td align="right">31.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">30.92</td>
    <td align="right">31.79</td>
    <td align="right">31.67</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">41.67</td>
    <td align="right">46.20</td>
    <td align="right">46.23</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">54.63</td>
    <td align="right">53.63</td>
    <td align="right">51.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">48.24</td>
    <td align="right">48.52</td>
    <td align="right">48.56</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">65.62</td>
    <td align="right">70.46</td>
    <td align="right">69.63</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">102.88</td>
    <td align="right">83.32</td>
    <td align="right">83.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">80.53</td>
    <td align="right">85.92</td>
    <td align="right">84.65</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.42</td>
    <td align="right">90.76</td>
    <td align="right">90.90</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">135.05</td>
    <td align="right">107.92</td>
    <td align="right">108.16</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">16.00</td>
    <td align="right">19.70</td>
    <td align="right">19.59</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.02</td>
    <td align="right">26.89</td>
    <td align="right">26.93</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.93</td>
    <td align="right">31.45</td>
    <td align="right">31.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.45</td>
    <td align="right">32.13</td>
    <td align="right">31.89</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.50</td>
    <td align="right">42.50</td>
    <td align="right">42.48</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.40</td>
    <td align="right">53.06</td>
    <td align="right">53.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">47.23</td>
    <td align="right">48.66</td>
    <td align="right">48.64</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">69.43</td>
    <td align="right">73.89</td>
    <td align="right">73.80</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.37</td>
    <td align="right">81.84</td>
    <td align="right">83.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">81.60</td>
    <td align="right">87.24</td>
    <td align="right">87.17</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.25</td>
    <td align="right">94.90</td>
    <td align="right">94.79</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.20</td>
    <td align="right">109.13</td>
    <td align="right">109.30</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">78.95</td>
    <td align="right">14.05</td>
    <td align="right">8.57</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">15.89</td>
    <td align="right">22.95</td>
    <td align="right">26.68</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.08</td>
    <td align="right">13.44</td>
    <td align="right">13.50</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">14.86</td>
    <td align="right">16.23</td>
    <td align="right">16.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">22.28</td>
    <td align="right">33.94</td>
    <td align="right">29.01</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">15.34</td>
    <td align="right">16.60</td>
    <td align="right">16.60</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">17.13</td>
    <td align="right">18.77</td>
    <td align="right">18.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">27.94</td>
    <td align="right">48.41</td>
    <td align="right">29.11</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.68</td>
    <td align="right">19.19</td>
    <td align="right">19.12</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">20.70</td>
    <td align="right">21.60</td>
    <td align="right">21.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">35.62</td>
    <td align="right">54.89</td>
    <td align="right">30.03</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">21.05</td>
    <td align="right">22.02</td>
    <td align="right">22.05</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">23.28</td>
    <td align="right">24.37</td>
    <td align="right">24.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.51</td>
    <td align="right">28.75</td>
    <td align="right">29.34</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.46</td>
    <td align="right">14.07</td>
    <td align="right">14.03</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.85</td>
    <td align="right">17.98</td>
    <td align="right">17.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.80</td>
    <td align="right">42.89</td>
    <td align="right">31.25</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.03</td>
    <td align="right">18.42</td>
    <td align="right">18.42</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.22</td>
    <td align="right">20.68</td>
    <td align="right">20.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.57</td>
    <td align="right">64.96</td>
    <td align="right">32.25</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.57</td>
    <td align="right">21.20</td>
    <td align="right">21.20</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.03</td>
    <td align="right">22.95</td>
    <td align="right">22.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">63.33</td>
    <td align="right">85.85</td>
    <td align="right">33.07</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.17</td>
    <td align="right">23.24</td>
    <td align="right">23.25</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.03</td>
    <td align="right">25.69</td>
    <td align="right">25.70</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">17.27</td>
    <td align="right">17.28</td>
    <td align="right">17.03</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.10</td>
    <td align="right">17.19</td>
    <td align="right">17.21</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.83</td>
    <td align="right">8.70</td>
    <td align="right">8.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.94</td>
    <td align="right">25.89</td>
    <td align="right">26.07</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.28</td>
    <td align="right">26.06</td>
    <td align="right">26.10</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.06</td>
    <td align="right">12.43</td>
    <td align="right">12.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.31</td>
    <td align="right">36.44</td>
    <td align="right">36.39</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.39</td>
    <td align="right">35.59</td>
    <td align="right">35.74</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.57</td>
    <td align="right">15.40</td>
    <td align="right">15.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.44</td>
    <td align="right">38.82</td>
    <td align="right">38.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.62</td>
    <td align="right">40.53</td>
    <td align="right">40.70</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">17.77</td>
    <td align="right">20.28</td>
    <td align="right">20.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.05</td>
    <td align="right">18.33</td>
    <td align="right">18.33</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.04</td>
    <td align="right">18.89</td>
    <td align="right">18.90</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">8.00</td>
    <td align="right">8.72</td>
    <td align="right">8.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.71</td>
    <td align="right">26.51</td>
    <td align="right">26.61</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.59</td>
    <td align="right">26.96</td>
    <td align="right">26.95</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.92</td>
    <td align="right">13.75</td>
    <td align="right">13.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.17</td>
    <td align="right">35.30</td>
    <td align="right">35.45</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.58</td>
    <td align="right">34.52</td>
    <td align="right">34.24</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.84</td>
    <td align="right">17.80</td>
    <td align="right">17.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.53</td>
    <td align="right">38.27</td>
    <td align="right">38.31</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.54</td>
    <td align="right">41.14</td>
    <td align="right">41.14</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.13</td>
    <td align="right">19.73</td>
    <td align="right">19.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">7.46</td>
    <td align="right">8.64</td>
    <td align="right">8.86</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">17.27</td>
    <td align="right">17.04</td>
    <td align="right">17.03</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.15</td>
    <td align="right">17.19</td>
    <td align="right">17.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">10.97</td>
    <td align="right">12.18</td>
    <td align="right">12.18</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.94</td>
    <td align="right">25.87</td>
    <td align="right">26.06</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.27</td>
    <td align="right">26.07</td>
    <td align="right">26.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.05</td>
    <td align="right">15.31</td>
    <td align="right">15.22</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.33</td>
    <td align="right">36.42</td>
    <td align="right">36.40</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.30</td>
    <td align="right">35.68</td>
    <td align="right">35.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">17.54</td>
    <td align="right">19.08</td>
    <td align="right">19.07</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.46</td>
    <td align="right">38.83</td>
    <td align="right">38.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.66</td>
    <td align="right">40.58</td>
    <td align="right">40.76</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.38</td>
    <td align="right">8.49</td>
    <td align="right">8.77</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">18.33</td>
    <td align="right">18.36</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.04</td>
    <td align="right">19.00</td>
    <td align="right">18.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.94</td>
    <td align="right">14.09</td>
    <td align="right">14.10</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">26.55</td>
    <td align="right">26.58</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.59</td>
    <td align="right">26.95</td>
    <td align="right">26.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.21</td>
    <td align="right">17.23</td>
    <td align="right">17.21</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.17</td>
    <td align="right">35.31</td>
    <td align="right">35.34</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.58</td>
    <td align="right">34.51</td>
    <td align="right">35.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.83</td>
    <td align="right">20.03</td>
    <td align="right">20.03</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.57</td>
    <td align="right">38.30</td>
    <td align="right">38.30</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.40</td>
    <td align="right">41.05</td>
    <td align="right">41.17</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">124.19</td>
    <td align="right">61.78</td>
    <td align="right">22.91</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">22.78</td>
    <td align="right">32.00</td>
    <td align="right">32.33</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">15.27</td>
    <td align="right">16.71</td>
    <td align="right">16.75</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">19.32</td>
    <td align="right">20.65</td>
    <td align="right">20.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">55.84</td>
    <td align="right">74.66</td>
    <td align="right">41.65</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">25.84</td>
    <td align="right">26.97</td>
    <td align="right">26.90</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">27.25</td>
    <td align="right">31.15</td>
    <td align="right">31.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">115.29</td>
    <td align="right">165.47</td>
    <td align="right">58.41</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.82</td>
    <td align="right">45.51</td>
    <td align="right">45.53</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">50.46</td>
    <td align="right">51.18</td>
    <td align="right">51.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">164.87</td>
    <td align="right">247.60</td>
    <td align="right">70.91</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">62.81</td>
    <td align="right">63.84</td>
    <td align="right">66.31</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">66.75</td>
    <td align="right">65.35</td>
    <td align="right">65.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">26.41</td>
    <td align="right">34.71</td>
    <td align="right">34.33</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.66</td>
    <td align="right">16.15</td>
    <td align="right">16.10</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.63</td>
    <td align="right">20.80</td>
    <td align="right">20.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">70.81</td>
    <td align="right">88.01</td>
    <td align="right">44.90</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.41</td>
    <td align="right">25.55</td>
    <td align="right">25.55</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">29.21</td>
    <td align="right">35.19</td>
    <td align="right">35.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">141.42</td>
    <td align="right">203.60</td>
    <td align="right">65.59</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">39.51</td>
    <td align="right">49.07</td>
    <td align="right">49.18</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">50.61</td>
    <td align="right">51.07</td>
    <td align="right">51.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">251.90</td>
    <td align="right">358.27</td>
    <td align="right">90.13</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.07</td>
    <td align="right">63.10</td>
    <td align="right">63.33</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.43</td>
    <td align="right">67.27</td>
    <td align="right">67.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">21.00</td>
    <td align="right">20.62</td>
    <td align="right">20.57</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">19.56</td>
    <td align="right">20.93</td>
    <td align="right">20.91</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">9.54</td>
    <td align="right">10.40</td>
    <td align="right">10.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">34.68</td>
    <td align="right">40.22</td>
    <td align="right">40.40</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">43.24</td>
    <td align="right">44.50</td>
    <td align="right">44.52</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">19.80</td>
    <td align="right">19.59</td>
    <td align="right">19.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">68.42</td>
    <td align="right">69.51</td>
    <td align="right">69.55</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">68.63</td>
    <td align="right">68.78</td>
    <td align="right">68.80</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">36.85</td>
    <td align="right">38.51</td>
    <td align="right">38.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.46</td>
    <td align="right">88.44</td>
    <td align="right">88.46</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">94.58</td>
    <td align="right">93.00</td>
    <td align="right">94.66</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">52.85</td>
    <td align="right">52.58</td>
    <td align="right">52.59</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.56</td>
    <td align="right">22.25</td>
    <td align="right">22.44</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.98</td>
    <td align="right">22.70</td>
    <td align="right">22.71</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">10.28</td>
    <td align="right">11.14</td>
    <td align="right">11.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.00</td>
    <td align="right">38.81</td>
    <td align="right">38.90</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.99</td>
    <td align="right">44.79</td>
    <td align="right">44.74</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.05</td>
    <td align="right">20.94</td>
    <td align="right">21.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">69.33</td>
    <td align="right">69.18</td>
    <td align="right">69.34</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.86</td>
    <td align="right">68.14</td>
    <td align="right">68.15</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.25</td>
    <td align="right">41.19</td>
    <td align="right">41.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.30</td>
    <td align="right">85.03</td>
    <td align="right">85.05</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.60</td>
    <td align="right">91.51</td>
    <td align="right">92.60</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.22</td>
    <td align="right">52.55</td>
    <td align="right">52.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">8.75</td>
    <td align="right">9.93</td>
    <td align="right">9.88</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">20.80</td>
    <td align="right">20.71</td>
    <td align="right">21.03</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">19.20</td>
    <td align="right">20.63</td>
    <td align="right">20.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">19.78</td>
    <td align="right">21.03</td>
    <td align="right">20.21</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">35.34</td>
    <td align="right">41.56</td>
    <td align="right">41.41</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">39.89</td>
    <td align="right">41.81</td>
    <td align="right">41.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">36.25</td>
    <td align="right">39.14</td>
    <td align="right">38.20</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">68.89</td>
    <td align="right">69.69</td>
    <td align="right">69.73</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">68.27</td>
    <td align="right">68.89</td>
    <td align="right">68.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">51.51</td>
    <td align="right">52.67</td>
    <td align="right">52.59</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.95</td>
    <td align="right">87.14</td>
    <td align="right">89.50</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">94.75</td>
    <td align="right">91.44</td>
    <td align="right">92.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.79</td>
    <td align="right">11.27</td>
    <td align="right">11.47</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">21.10</td>
    <td align="right">22.60</td>
    <td align="right">22.85</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.86</td>
    <td align="right">23.42</td>
    <td align="right">23.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">22.65</td>
    <td align="right">24.61</td>
    <td align="right">24.44</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.32</td>
    <td align="right">40.66</td>
    <td align="right">40.69</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.29</td>
    <td align="right">40.67</td>
    <td align="right">40.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.92</td>
    <td align="right">40.23</td>
    <td align="right">40.21</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.10</td>
    <td align="right">68.15</td>
    <td align="right">68.10</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.53</td>
    <td align="right">68.46</td>
    <td align="right">68.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.03</td>
    <td align="right">52.82</td>
    <td align="right">52.86</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.44</td>
    <td align="right">87.08</td>
    <td align="right">88.40</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.18</td>
    <td align="right">92.61</td>
    <td align="right">93.90</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.87</td>
    <td align="right">6.65</td>
    <td align="right">5.58</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">51.48</td>
    <td align="right">45.50</td>
    <td align="right">32.65</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.30</td>
    <td align="right">18.41</td>
    <td align="right">21.56</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">22.30</td>
    <td align="right">22.26</td>
    <td align="right">24.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">73.95</td>
    <td align="right">65.47</td>
    <td align="right">34.08</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">19.52</td>
    <td align="right">19.69</td>
    <td align="right">21.63</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.06</td>
    <td align="right">25.28</td>
    <td align="right">26.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">92.41</td>
    <td align="right">79.37</td>
    <td align="right">33.65</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">23.14</td>
    <td align="right">23.06</td>
    <td align="right">24.30</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">27.38</td>
    <td align="right">27.22</td>
    <td align="right">28.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">121.00</td>
    <td align="right">99.65</td>
    <td align="right">34.12</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">24.32</td>
    <td align="right">24.36</td>
    <td align="right">25.24</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">29.26</td>
    <td align="right">29.00</td>
    <td align="right">29.61</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">67.60</td>
    <td align="right">59.73</td>
    <td align="right">40.21</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.91</td>
    <td align="right">20.60</td>
    <td align="right">22.96</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.59</td>
    <td align="right">25.10</td>
    <td align="right">26.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">99.48</td>
    <td align="right">86.36</td>
    <td align="right">42.14</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.20</td>
    <td align="right">21.91</td>
    <td align="right">23.10</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.53</td>
    <td align="right">27.68</td>
    <td align="right">28.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">121.87</td>
    <td align="right">105.03</td>
    <td align="right">41.14</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.31</td>
    <td align="right">25.17</td>
    <td align="right">25.79</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.05</td>
    <td align="right">29.82</td>
    <td align="right">29.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">158.68</td>
    <td align="right">133.66</td>
    <td align="right">41.10</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.47</td>
    <td align="right">26.74</td>
    <td align="right">27.21</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.84</td>
    <td align="right">31.55</td>
    <td align="right">31.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">21.12</td>
    <td align="right">39.05</td>
    <td align="right">40.26</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">23.55</td>
    <td align="right">38.93</td>
    <td align="right">39.18</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">16.03</td>
    <td align="right">27.69</td>
    <td align="right">27.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.82</td>
    <td align="right">54.41</td>
    <td align="right">54.48</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">30.06</td>
    <td align="right">54.42</td>
    <td align="right">54.72</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">15.52</td>
    <td align="right">37.18</td>
    <td align="right">27.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">35.67</td>
    <td align="right">72.22</td>
    <td align="right">72.19</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">41.24</td>
    <td align="right">74.77</td>
    <td align="right">71.85</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">25.62</td>
    <td align="right">54.27</td>
    <td align="right">36.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">39.65</td>
    <td align="right">82.13</td>
    <td align="right">82.17</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">46.42</td>
    <td align="right">86.86</td>
    <td align="right">86.12</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">25.54</td>
    <td align="right">54.51</td>
    <td align="right">37.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.49</td>
    <td align="right">41.18</td>
    <td align="right">41.79</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.40</td>
    <td align="right">42.07</td>
    <td align="right">42.74</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.53</td>
    <td align="right">27.99</td>
    <td align="right">27.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.42</td>
    <td align="right">56.93</td>
    <td align="right">56.76</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">31.84</td>
    <td align="right">57.46</td>
    <td align="right">57.01</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.76</td>
    <td align="right">37.16</td>
    <td align="right">27.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">38.16</td>
    <td align="right">76.23</td>
    <td align="right">74.60</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.04</td>
    <td align="right">75.04</td>
    <td align="right">74.57</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.16</td>
    <td align="right">53.77</td>
    <td align="right">36.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">40.91</td>
    <td align="right">84.50</td>
    <td align="right">86.00</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">46.69</td>
    <td align="right">89.77</td>
    <td align="right">89.74</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.19</td>
    <td align="right">53.94</td>
    <td align="right">37.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">16.53</td>
    <td align="right">27.48</td>
    <td align="right">27.40</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">18.54</td>
    <td align="right">29.61</td>
    <td align="right">29.60</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">19.20</td>
    <td align="right">29.63</td>
    <td align="right">29.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">16.56</td>
    <td align="right">43.90</td>
    <td align="right">34.24</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">17.43</td>
    <td align="right">38.44</td>
    <td align="right">28.79</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">19.04</td>
    <td align="right">46.81</td>
    <td align="right">37.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">26.53</td>
    <td align="right">53.78</td>
    <td align="right">36.35</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">29.99</td>
    <td align="right">57.71</td>
    <td align="right">39.62</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">30.84</td>
    <td align="right">57.39</td>
    <td align="right">39.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">26.12</td>
    <td align="right">54.19</td>
    <td align="right">37.05</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">31.52</td>
    <td align="right">59.24</td>
    <td align="right">49.07</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">32.04</td>
    <td align="right">59.45</td>
    <td align="right">39.96</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.86</td>
    <td align="right">28.15</td>
    <td align="right">27.71</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.71</td>
    <td align="right">30.68</td>
    <td align="right">30.66</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.31</td>
    <td align="right">30.75</td>
    <td align="right">30.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.92</td>
    <td align="right">44.27</td>
    <td align="right">34.28</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.79</td>
    <td align="right">38.51</td>
    <td align="right">28.98</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.67</td>
    <td align="right">46.36</td>
    <td align="right">36.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.12</td>
    <td align="right">53.60</td>
    <td align="right">36.80</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">32.09</td>
    <td align="right">57.32</td>
    <td align="right">39.77</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.72</td>
    <td align="right">57.46</td>
    <td align="right">39.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.10</td>
    <td align="right">53.78</td>
    <td align="right">36.99</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.67</td>
    <td align="right">59.57</td>
    <td align="right">40.36</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.00</td>
    <td align="right">58.70</td>
    <td align="right">39.81</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.63</td>
    <td align="right">33.24</td>
    <td align="right">16.73</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">55.21</td>
    <td align="right">48.10</td>
    <td align="right">35.41</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">18.95</td>
    <td align="right">20.78</td>
    <td align="right">24.18</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">31.93</td>
    <td align="right">25.64</td>
    <td align="right">27.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">112.00</td>
    <td align="right">84.76</td>
    <td align="right">41.03</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">21.61</td>
    <td align="right">21.93</td>
    <td align="right">23.91</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">30.55</td>
    <td align="right">28.51</td>
    <td align="right">29.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">218.91</td>
    <td align="right">187.60</td>
    <td align="right">58.28</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">36.01</td>
    <td align="right">35.04</td>
    <td align="right">36.44</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">47.41</td>
    <td align="right">46.40</td>
    <td align="right">47.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">356.32</td>
    <td align="right">299.54</td>
    <td align="right">74.26</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">42.43</td>
    <td align="right">42.48</td>
    <td align="right">43.60</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">59.32</td>
    <td align="right">58.94</td>
    <td align="right">60.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">71.08</td>
    <td align="right">62.01</td>
    <td align="right">42.03</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.16</td>
    <td align="right">21.48</td>
    <td align="right">24.52</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.88</td>
    <td align="right">27.17</td>
    <td align="right">28.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">144.27</td>
    <td align="right">155.75</td>
    <td align="right">59.86</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.25</td>
    <td align="right">29.45</td>
    <td align="right">30.68</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">32.43</td>
    <td align="right">30.42</td>
    <td align="right">30.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">260.14</td>
    <td align="right">218.76</td>
    <td align="right">64.84</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.79</td>
    <td align="right">37.59</td>
    <td align="right">38.37</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">48.23</td>
    <td align="right">49.27</td>
    <td align="right">48.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">437.91</td>
    <td align="right">354.34</td>
    <td align="right">79.20</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.33</td>
    <td align="right">44.87</td>
    <td align="right">45.69</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.93</td>
    <td align="right">62.44</td>
    <td align="right">62.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">30.42</td>
    <td align="right">47.83</td>
    <td align="right">48.92</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">25.97</td>
    <td align="right">39.23</td>
    <td align="right">39.41</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">16.32</td>
    <td align="right">30.47</td>
    <td align="right">30.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">30.97</td>
    <td align="right">56.39</td>
    <td align="right">56.55</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">36.81</td>
    <td align="right">56.03</td>
    <td align="right">56.43</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">18.65</td>
    <td align="right">40.40</td>
    <td align="right">30.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">56.22</td>
    <td align="right">86.44</td>
    <td align="right">86.47</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">64.02</td>
    <td align="right">91.50</td>
    <td align="right">89.00</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">46.02</td>
    <td align="right">79.05</td>
    <td align="right">62.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">74.28</td>
    <td align="right">105.08</td>
    <td align="right">105.17</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">83.60</td>
    <td align="right">115.40</td>
    <td align="right">114.83</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">57.66</td>
    <td align="right">91.93</td>
    <td align="right">74.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">27.49</td>
    <td align="right">41.29</td>
    <td align="right">41.98</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.69</td>
    <td align="right">42.43</td>
    <td align="right">43.06</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.16</td>
    <td align="right">30.36</td>
    <td align="right">30.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">46.88</td>
    <td align="right">72.19</td>
    <td align="right">72.06</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">48.82</td>
    <td align="right">62.46</td>
    <td align="right">62.21</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">18.53</td>
    <td align="right">46.53</td>
    <td align="right">36.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">58.54</td>
    <td align="right">88.94</td>
    <td align="right">87.38</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">64.60</td>
    <td align="right">91.73</td>
    <td align="right">91.29</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">46.73</td>
    <td align="right">77.73</td>
    <td align="right">60.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">75.53</td>
    <td align="right">106.69</td>
    <td align="right">107.76</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">84.59</td>
    <td align="right">117.60</td>
    <td align="right">117.73</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.58</td>
    <td align="right">89.55</td>
    <td align="right">73.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">16.72</td>
    <td align="right">29.11</td>
    <td align="right">29.04</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">23.43</td>
    <td align="right">47.28</td>
    <td align="right">47.25</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">19.69</td>
    <td align="right">30.97</td>
    <td align="right">30.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">18.61</td>
    <td align="right">48.92</td>
    <td align="right">38.15</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.04</td>
    <td align="right">40.72</td>
    <td align="right">30.95</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">21.66</td>
    <td align="right">57.20</td>
    <td align="right">48.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">52.19</td>
    <td align="right">82.88</td>
    <td align="right">67.49</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">51.43</td>
    <td align="right">82.14</td>
    <td align="right">63.85</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">53.15</td>
    <td align="right">83.44</td>
    <td align="right">65.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">62.61</td>
    <td align="right">95.03</td>
    <td align="right">79.59</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">61.32</td>
    <td align="right">97.28</td>
    <td align="right">81.61</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">62.67</td>
    <td align="right">97.71</td>
    <td align="right">78.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.26</td>
    <td align="right">29.88</td>
    <td align="right">29.84</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.04</td>
    <td align="right">31.99</td>
    <td align="right">31.95</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.73</td>
    <td align="right">31.92</td>
    <td align="right">31.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.11</td>
    <td align="right">48.08</td>
    <td align="right">38.05</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">21.32</td>
    <td align="right">41.15</td>
    <td align="right">31.45</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">23.56</td>
    <td align="right">49.95</td>
    <td align="right">40.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">50.02</td>
    <td align="right">77.82</td>
    <td align="right">61.07</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.84</td>
    <td align="right">81.78</td>
    <td align="right">64.18</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.53</td>
    <td align="right">82.13</td>
    <td align="right">64.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.49</td>
    <td align="right">92.22</td>
    <td align="right">75.16</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.39</td>
    <td align="right">97.62</td>
    <td align="right">77.66</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">64.89</td>
    <td align="right">97.56</td>
    <td align="right">78.04</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
